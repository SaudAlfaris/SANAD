from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, RadioField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, Length, AnyOf, Regexp


class SignUpForm(FlaskForm):
    name = StringField("الاسم الثنائي:", validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField(":البريد الإلكتروني", validators=[DataRequired(), Length(min=1, max=90)])
    phone = StringField(":رقم الجوال", validators=[DataRequired(), Length(min=9, max=9)])
    gender = SelectField(":الجنس", validators=[DataRequired(), Length(max=30)], choices=[('M', 'ذكر'), ('F', 'أنثى')])
    password = PasswordField(":كلمة المرور", validators=[DataRequired(), Length(max=30)])
    repeatedPassword = PasswordField(":تأكيد كلمة المرور", validators=[DataRequired(), Length(max=30)])
    register = SubmitField("تسجيل حساب")

class SignInForm(FlaskForm):
    email = StringField(":البريد الإلكتروني", validators=[DataRequired(), Length(min=1, max=90)])
    password = PasswordField(":كلمة المرور", validators=[DataRequired(), Length(max=30)])
    sign = SubmitField("تسجيل الدخول")

class AppearanceForm(FlaskForm):
    appearance = SelectField("حالة الظهور:", validators=[DataRequired()], choices=[
        ('SHOW', 'الظهور في محرك البحث'),
        ('HIDE', 'عدم الظهور في محرك بالبحث')
    ])
    confirm = SubmitField("تأكيد")

class MentorSearchForm(FlaskForm):
    major = SelectMultipleField("التخصص:", validators=[DataRequired()], choices=[
        ('MATH', 'الرياضيات'),
        ('AS', 'العلوم الإكتوارية'),
        ('COE', 'هندسة الحاسب'),
        ('ICS', 'علوم الحاسب'),
        ('SWE', 'هندسة البرمجيات'),
        ('ISE', 'الهندسة الصناعية'),
        ('EE', 'الهندسة الكهربائية'),
        ('ME', 'الهندسة الميكانيكية'),
        ('AE', 'هندسة الطيران والفضاء'),
        ('PHYS', 'الفيزياء'),
        ('CIE', 'هندسة التحكم والقياس'),
        ('FIN', 'المالية'),
        ('ACCT', 'المحاسبة'),
        ('MIS', 'نظم المعلومات الإدارية'),
        ('MGT', 'الإدارة'),
        ('MKT', 'التسويق'),
        ('CHEM', 'الكيمياء'),
        ('CHE', 'الهندسة الكيميائية'),
        ('MSE', 'هندسة المواد'),
        ('ARE', 'الهندسة المعمارية'),
        ('ARC', 'العمارة'),
        ('CE', 'الهندسة المدنية'),
        ('PETE', 'هندسة البترول'),
        ('GEO', 'الجيولوجيا'),
        ('GEOP', 'الجيوفيزياء'),

    ])
    standing = SelectMultipleField("المستوى:", validators=[DataRequired()], choices=[
        ('prep', 'تحضيري'),
        ('freshmen', 'السنة الأولى'),
        ('sophomore', 'السنة الثانية'),
        ('junior', 'السنة الثالثة'),
        ('senior', 'السنة الرابعة'),
        ('graduate', 'خريج')
    ])
    history = SelectMultipleField("الأداء الأكاديمي:", validators=[DataRequired()], choices=[
        ('low', 'منخفض دائمًا'),
        ('high_then_low', 'مرتفع ثم منخفض'),
        ('low_then_high', 'منخفض ثم مرتفع'),
        ('always_high', 'مرتفع دائمًا')
    ])
    city = SelectMultipleField("المدينة:", validators=[DataRequired()], choices=[
        ('MCC', 'مكة'),
        ('MDN', 'المدينة المنورة'),
        ('RYD', 'الرياض'),
        ('JED', 'جدة'),
        ('DMM', 'الدمام'),
        ('HAS', 'الأحساء'),
        ('JUB', 'الجبيل'),
        ('TAF', 'الطائف'),
        ('ULA', 'العلا'),
        ('TBK', 'تبوك'),
        ('AJF', 'الجوف'),
        ('HAI', 'حائل'),
        ('HAF', 'حفر الباطن'),
        ('QSM', 'القصيم'),
        ('ASR', 'عسير'),
        ('BAH', 'الباحة'),
        ('JZN', 'جازان'),
        ('NJN', 'نجران')
    ])
    housing = SelectMultipleField("نوع السكن:", validators=[DataRequired()], choices=[
        ('on-campus', 'داخل الحرم الجامعي'),
        ('out-of-campus', 'خارج الحرم الجامعي')
    ])
    register = SubmitField("البحث عن مرشد")

class MentorRegistrationForm(FlaskForm):
    major = SelectField("التخصص:", validators=[DataRequired()], choices=[
        ('MATH', 'الرياضيات'),
        ('AS', 'العلوم الإكتوارية'),
        ('COE', 'هندسة الحاسب'),
        ('ICS', 'علوم الحاسب'),
        ('SWE', 'هندسة البرمجيات'),
        ('ISE', 'الهندسة الصناعية'),
        ('EE', 'الهندسة الكهربائية'),
        ('ME', 'الهندسة الميكانيكية'),
        ('AE', 'هندسة الطيران والفضاء'),
        ('PHYS', 'الفيزياء'),
        ('CIE', 'هندسة التحكم والقياس'),
        ('FIN', 'المالية'),
        ('ACCT', 'المحاسبة'),
        ('MIS', 'نظم المعلومات الإدارية'),
        ('MGT', 'الإدارة'),
        ('MKT', 'التسويق'),
        ('CHEM', 'الكيمياء'),
        ('CHE', 'الهندسة الكيميائية'),
        ('MSE', 'هندسة المواد'),
        ('ARE', 'الهندسة المعمارية'),
        ('ARC', 'العمارة'),
        ('CE', 'الهندسة المدنية'),
        ('PETE', 'هندسة البترول'),
        ('GEO', 'الجيولوجيا'),
        ('GEOP', 'الجيوفيزياء'),

    ])
    standing = SelectField("المستوى:", validators=[DataRequired()], choices=[
        ('prep', 'تحضيري'),
        ('freshmen', 'السنة الأولى'),
        ('sophomore', 'السنة الثانية'),
        ('junior', 'السنة الثالثة'),
        ('senior', 'السنة الرابعة'),
        ('graduate', 'خريج')
    ])
    history = SelectField("الأداء الأكاديمي:", validators=[DataRequired()], choices=[
        ('low', 'منخفض دائمًا'),
        ('high_then_low', 'مرتفع ثم منخفض'),
        ('low_then_high', 'منخفض ثم مرتفع'),
        ('always_high', 'مرتفع دائمًا')
    ])
    city = SelectField("المدينة:", validators=[DataRequired()], choices=[
        ('MCC', 'مكة'),
        ('MDN', 'المدينة المنورة'),
        ('RYD', 'الرياض'),
        ('JED', 'جدة'),
        ('DMM', 'الدمام'),
        ('HAS', 'الأحساء'),
        ('JUB', 'الجبيل'),
        ('TAF', 'الطائف'),
        ('ULA', 'العلا'),
        ('TBK', 'تبوك'),
        ('AJF', 'الجوف'),
        ('HAI', 'حائل'),
        ('HAF', 'حفر الباطن'),
        ('QSM', 'القصيم'),
        ('ASR', 'عسير'),
        ('BAH', 'الباحة'),
        ('JZN', 'جازان'),
        ('NJN', 'نجران')
    ])
    housing = SelectField("نوع السكن:", validators=[DataRequired()], choices=[
        ('on-campus', 'داخل الحرم الجامعي'),
        ('out-of-campus', 'خارج الحرم الجامعي')
    ])
    register = SubmitField("تسجيل كمرشد")



class MentorRatingForm(FlaskForm):


    rating = SelectField("التقييم:", validators=[DataRequired()], choices=[
        (0, 'لم يتم التواصل'),
        (1, 'سيء'),
        (2, 'مقبول'),
        (3, 'جيد'),
        (4, 'ممتاز')
    ])
    rate = SubmitField("تقييم المرشد")

