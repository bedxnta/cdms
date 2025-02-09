import mysql.connector as sqltor
import sqlfunctions as sqlf


mycon = sqltor.connect(host="localhost", user="root", password="123456", database="charity")
cursor = mycon.cursor()


# Welcome Screen
print("Welcome to CDMS!")
print("Developed by Bedanta Dey | V.0.0.1")
print("Please proceed with appropriate inputs to continue.")
print("")

while True:
    print("Enter an input:")
    print("1. Login")
    print("2. Create an Account")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # User Login
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user = sqlf.check_credentials(username, password)

        if user:
            print("Login successful!")
            print("")
            print("")
            while True:
                print("\nCDMS Menu:")
                print("1. Add Donor")
                print("2. Make Donation")
                print("3. View Donors")
                print("4. View Donations")
                print("5. Delete Donor")
                print("6. Logout")
                option = input("Enter your choice: ")

            # set id feature does not work - it does work now
                if option == "1":
                    name = input("Enter donor's name: ")
                    email = input("Enter donor's email: ")
                    donor_id = input("Set donor ID: ")
                    sqlf.add_donor(name, email, donor_id)

                elif option == "2":
                    donor_id = int(input("Enter donor ID: "))
                    amount = float(input("Enter donation amount: "))
                    donation_date = input("Enter donation date (YYYY-MM-DD): ")
                    sqlf.make_donation(donor_id, amount, donation_date)

                elif option == "3":
                    sqlf.view_donors()

                elif option == "4":
                    sqlf.view_donations()
                
                elif option == "5":
                    donor_id = input("Enter donor's ID: ")
                    sqlf.delete_donor(int(donor_id))

                elif option == "6":
                    print("Logged out. Goodbye!")
                    print("")
                    print("")
                    break

                else:
                    print("Invalid choice. Please choose a valid option.")
                    print("")
                    print("")

        else:
            print("Invalid username or password. Please try again.")
            print("")
            print("")

    elif choice == "2":
        # User Registration
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username already taken. Please choose another username.")
            print("")
            print("")
        else:
            sqlf.create_user(username, password)
            print("Account created successfully! You can now log in.")
            print("")
            print("")

    elif choice == "3":
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
        print("")
        print("")


mycon.close()
