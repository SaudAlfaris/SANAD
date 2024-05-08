import sqlite3

def connect_db():
    return sqlite3.connect('mentorship_database.db')

# Add a new user
def add_user(email, name, phone, gender, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (Email, Name, Phone, Gender, Password) VALUES (?, ?, ?, ?, ?)", 
                   (email, name, phone, gender, password))
    conn.commit()
    conn.close()

# Update user details
def update_user(email, name=None, phone=None, gender=None, password=None):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE User SET "
    params = []
    if name:
        query += "Name = ?, "
        params.append(name)
    if phone:
        query += "Phone = ?, "
        params.append(phone)
    if gender:
        query += "Gender = ?, "
        params.append(gender)
    if password:
        query += "Password = ?, "
        params.append(password)
    query = query.rstrip(", ") + " WHERE Email = ?"
    params.append(email)
    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()

# Delete a user
def delete_user(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM User WHERE Email = ?", (email,))
    conn.commit()
    conn.close()

# Add a new mentor
def add_mentor(email, major, standing, history, city, housing, appearance):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Mentor (Email, Major, Standing, History, City, Housing, Appearance) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                   (email, major, standing, history, city, housing, appearance))
    conn.commit()
    conn.close()

# Update mentor details
def update_mentor(email, major=None, standing=None, history=None, city=None, housing=None, appearance=None):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE Mentor SET "
    params = []
    if major:
        query += "Major = ?, "
        params.append(major)
    if standing:
        query += "Standing = ?, "
        params.append(standing)
    if history:
        query += "History = ?, "
        params.append(history)
    if city:
        query += "City = ?, "
        params.append(city)
    if housing:
        query += "Housing = ?, "
        params.append(housing)
    if appearance:
        query += "Appearance = ?, "
        params.append(appearance)
    query = query.rstrip(", ") + " WHERE Email = ?"
    params.append(email)
    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()

# Delete a mentor
def delete_mentor(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Mentor WHERE Email = ?", (email,))
    conn.commit()
    conn.close()


# Get user by attribute(s)
def get_user(**kwargs):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM User WHERE "
    params = []
    for key, value in kwargs.items():
        query += f"{key} = ? AND "
        params.append(value)
    query = query.rstrip("AND ")
    cursor.execute(query, tuple(params))
    user = cursor.fetchone()
    conn.close()
    return user

# Get mentor by attribute(s)
def get_mentor(**kwargs):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM Mentor WHERE "
    conditions = []
    params = []
    
    for key, value in kwargs.items():
        if isinstance(value, list):
            placeholders = ','.join(['?' for _ in value])
            conditions.append(f"{key} IN ({placeholders})")
            params.extend(value)
        else:
            conditions.append(f"{key} = ?")
            params.append(value)
    
    query += ' AND '.join(conditions)
    cursor.execute(query, tuple(params))
    mentor = cursor.fetchall()
    conn.close()
    returned_list = []
    for m in mentor:
        returned_list += [m+get_user(email=m[0])[1:-1]]
        print('XXX', get_rated_engagements_average(email=m[0])) 
    return returned_list

def search_mentor(searchingEmail, **kwargs):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM Mentor WHERE "
    conditions = []
    params = []
    
    for key, value in kwargs.items():
        if isinstance(value, list):
            placeholders = ','.join(['?' for _ in value])
            conditions.append(f"{key} IN ({placeholders})")
            params.extend(value)
        else:
            conditions.append(f"{key} = ?")
            params.append(value)
    
    query += ' AND '.join(conditions)
    cursor.execute(query, tuple(params))
    mentor = cursor.fetchall()
    conn.close()
    returned_list = []
    for m in mentor:
        if m[0] != searchingEmail and m[6] == "SHOW":
            returned_list += [list(m+get_user(email=m[0])[1:-1]) + [get_rated_engagements_average(email=m[0])]]
    return returned_list

# Get engagement by attribute(s)
def get_engagement(**kwargs):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM Engagement WHERE "
    params = []
    for key, value in kwargs.items():
        query += f"{key} = ? AND "
        params.append(value)
    query = query.rstrip("AND ")
    cursor.execute(query, tuple(params))
    engagement = cursor.fetchone()
    conn.close()
    return engagement





# Add a new engagement
def add_engagement(user_email, mentor_email, status):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Engagement (Email, Mentor_Email, Status) VALUES (?, ?, ?)", 
                    (user_email, mentor_email, status))
        conn.commit()
    except:
        pass
    conn.close()

# Update engagement status
def update_engagement(user_email, mentor_email, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Engagement SET Status = ? WHERE Email = ? AND Mentor_Email = ?", 
                   (status, user_email, mentor_email))
    conn.commit()
    conn.close()

# Delete an engagement
def delete_engagement(user_email, mentor_email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Engagement WHERE Email = ? AND Mentor_Email = ?", (user_email, mentor_email))
    conn.commit()
    conn.close()


# Get unrated engagements
def get_unrated_engagements(email):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT Mentor_Email FROM Engagement WHERE Email = ? AND Status IS NULL", (email,))
        unrated_engagements = cursor.fetchall()
    except Exception as e:
        print(f"Error occurred: {e}")
        unrated_engagements = []
    conn.close()
    returned_list = []
    for e in unrated_engagements:
        returned_list += [get_mentor(email=e[0])[0]]
    return returned_list

# Get average rating of rated engagements
def get_rated_engagements_average(email):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT AVG(Status) FROM Engagement WHERE Mentor_Email = ? AND Status IS NOT NULL AND Status > 0 AND Status < 5;", (email,))
        avg_rating = cursor.fetchone()[0]
        if avg_rating is None:
            avg_rating = 4
    except Exception as e:
        print(f"Error occurred: {e}")
        avg_rating = 4
    conn.close()
    return avg_rating

