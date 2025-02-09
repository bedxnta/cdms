"""All functions for a smooth sailing charity donation experience"""
"""This is NOT an external library. This was made by me."""
import mysql.connector as sqltor

mycon = sqltor.connect(host="localhost", user="root", password="123456", database="charity")
cursor = mycon.cursor()

def create_user(username, password):
    '''Creates a USER for the CDMS'''
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(query, values)
    mycon.commit()

def check_credentials(username, password):
    '''Validates username and password against the database'''
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)
    user = cursor.fetchone()
    return user

def add_donor(name, email, donor_id):
    '''Adds a donor'''
    query = "INSERT INTO donors (name, email, donor_id) VALUES (%s, %s, %s)"
    values = (name, email,donor_id)
    cursor.execute(query, values)
    mycon.commit()
    print("Donor added successfully!")
    print("")
    print("")

def make_donation(donor_id, amount, donation_date):
    '''Makes a donation'''
    query = "INSERT INTO donations (donor_id, amount, donation_date) VALUES (%s, %s, %s)"
    values = (donor_id, amount, donation_date)
    cursor.execute(query, values)
    mycon.commit()
    print("Donation recorded successfully!")
    print("")
    print("")

def delete_donor(donor_id):
    '''Deletes a donor'''
    delete_donations_query = "DELETE FROM donations WHERE donor_id = %s"
    cursor.execute(delete_donations_query, (donor_id,))
    mycon.commit()

    delete_donor_query = "DELETE FROM donors WHERE donor_id = %s"
    cursor.execute(delete_donor_query, (donor_id,))
    mycon.commit()
    print(f"User '{donor_id}' deleted successfully.")

# DISPLAY FUNCtions
def view_donors():
    '''Views donors'''
    query = "SELECT * FROM donors"
    cursor.execute(query)
    donors = cursor.fetchall()
    print("")
    print("")
    for x in donors:
        for y in x:
            print(y, end="   ")
        print()
    print("")

def view_donations():
    '''Views donations'''
    query = "SELECT * FROM donations"
    cursor.execute(query)
    donations = cursor.fetchall()
    print("")
    print("")
    for x in donations:
        for y in x:
            print(y, end="   ")
        print()
    print("")