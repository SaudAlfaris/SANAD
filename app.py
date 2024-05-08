from flask import Flask, render_template, redirect, url_for, request
from database import *
from forms import *
from utilities import dictOfDicts
app = Flask(__name__) 
app.config["SECRET_KEY"] = "SANAD"



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/user/<email>/profile", methods=("GET", "POST"))
def userProfile(email): 
    user = get_user(Email=email)
    return render_template("userProfile.html", user=user)


@app.route("/signup", methods=("GET", "POST"))
def signup():
    form  = SignUpForm()
    if form.validate_on_submit():
        if get_user(Email=form.email.data) == None and form.password.data == form.repeatedPassword.data:
            add_user(name=form.name.data, email=form.email.data, phone=form.phone.data, gender=form.gender.data, password=form.password.data)
            return redirect(url_for("userProfile", email=form.email.data))
    return render_template("signup.html", form=form)

@app.route("/signin", methods=("GET", "POST"))
def signin():
    form  = SignInForm()
    if form.validate_on_submit():
        profile = get_user(Email=form.email.data)
        if profile != None and profile[-1]==form.password.data:
            return redirect(url_for("userProfile", email=form.email.data))
    return render_template("signin.html", form=form)



@app.route("/user/<email>/mentorreg", methods=("GET", "POST"))
def mentorRegistration(email): 
    profile = get_mentor(email=email)
    if len(profile) != 0:
        profile = profile[0]
    form = MentorRegistrationForm()
    form2 = AppearanceForm()
    if form.validate_on_submit():
        if profile != []:
            update_mentor(email=email, major=form.major.data,standing=form.standing.data,history=form.history.data,city=form.city.data,housing=form.housing.data)
        else:
            add_mentor(email=email, major=form.major.data,standing=form.standing.data,history=form.history.data,city=form.city.data,housing=form.housing.data, appearance="SHOW")
            print("a",profile)
        return redirect(url_for("mentorRegistration", email=email))
    if form2.validate_on_submit():
        update_mentor(email=email, appearance=form2.appearance.data)
        return redirect(url_for("mentorRegistration", email=email))
    return render_template("mentorReg.html", dictOfDicts=dictOfDicts, profile=profile,form=form, form2=form2)


@app.route("/user/<email>/mentorsearch", methods=("GET", "POST"))
def mentorSearch(email):
    form = MentorSearchForm()
    if form.validate_on_submit():
        searchResult = search_mentor(searchingEmail=email,major=form.major.data, standing=form.standing.data, history=form.history.data, city=form.city.data, housing=form.housing.data)
        return redirect(url_for("mentorSearchR", email=email, result=searchResult))
    return render_template("mentorSearch.html", form=form)

@app.route("/user/<email>/mentorsearchr", methods=("GET", "POST"))
def mentorSearchR(email, result=None):
    result = [eval(r) for r in request.args.getlist('result')]
    # print(result)
    return render_template("mentorSearchResult.html", dictOfDicts=dictOfDicts, result=result, email=email)

@app.route("/user/<email>/contact/<mentorEmail>", methods=("GET", "POST"))
def contactMentor(email,mentorEmail, result=None):
    add_engagement(user_email=email, mentor_email=mentorEmail, status=None)
    return redirect("https://wa.me/966"+get_user(email=mentorEmail)[2])

@app.route("/user/<email>/ratings", methods=("GET", "POST"))
def mentorRatings(email):
    result = get_unrated_engagements(email)
    return render_template("mentorRatings.html", dictOfDicts=dictOfDicts ,result=result, email=email)

@app.route("/user/<email>/rate/<mentorEmail>", methods=("GET", "POST"))
def rateMentor(email,mentorEmail):
    form = MentorRatingForm()
    if form.validate_on_submit():
        update_engagement(user_email=email, mentor_email=mentorEmail, status=form.rating.data)
        return redirect(url_for("mentorRatings", email=email))
    return render_template("mentorRating.html", form=form, email=email, r=get_mentor(email=mentorEmail), dictOfDicts=dictOfDicts)

@app.route("/user/<email>/signout", methods=("GET", "POST"))
def signout(email):
    return redirect(url_for("home"))

app.run(debug=True,host='0.0.0.0', port=5000)

