#Author: Sabria Fafach
#Date: May 2, 2025
#Title: edit_phonebook.py


import sqlite3


def Insert_rows():

    #Get data that user wants to enter:
    name=input("Enter the name that you want to add to the Phonebook database:")

    number=input(f"Enter {name}'s phone number:")

    #Connect to the database:
    conn=sqlite3.connect("phonebook.db")

    #Get a cursor:
    cur=conn.cursor()

    #Add the data to the Entries table:
    cur.execute('''INSERT INTO Entries (name, number) VALUES(?,?)''',(name,number,))

    #Commit the changes:
    conn.commit()

    #CLose the connection:
    conn.close()

    return

def Show_rows():

    name=input("Enter the name of the person whose number you want:")

    conn=sqlite3.connect("phonebook.db")

    cur=conn.cursor()

    cur.execute('''SELECT * FROM Entries WHERE name==?''',(name,))

    results=cur.fetchall()

    if len(results)>0:
        print(f"Here are all the contacts named {name}:")
        print()
        for row in results:
            print(f"{row[1]:30} {row[2]:>5}")

    else:
        print(f"There are no contacts named {name}.")

        conn.close()


    return


def Update_rows():


    conn=sqlite3.connect("phonebook.db")
    cur=conn.cursor()

    contact=input("Enter the name of the contact you want to update:")

    cur.execute('''SELECT * FROM Entries WHERE name==?''',(contact,))

    results=cur.fetchone()

    if results != None:
        new_number=input(f"Enter the new number for {contact}:")

        cur.execute('''UPDATE Entries SET number=?
        WHERE name==?''',(new_number,contact,))

        conn.commit()
        print("The number has been changed,")
    else:
        print(f"Sorry, {contact} was not found.")

    conn.close()

    return


def Delete_rows():


    conn=sqlite3.connect("phonebook.db")
    cur=conn.cursor()
    contact=input("Enter the name of the contact you want to delete:")

    cur.execute('''SELECT * FROM Entries WHERE name==?''',(contact,))

    results=cur.fetchone()

    if results != None:
        sure=input(f"Are you sure you want to delete {results[0]} y = yes:")

        if sure.lower()=='y':
            cur.execute('''DELETE FROM Entries WHERE name==?''',(contact,))

        conn.commit()
        print(f"{contact} was deleted.")
    else:
        print(f"{contact} was not found.")

    conn.close()
    return


def main():
    insert=input("Do you want to enter a contact? y/n:")
    while insert=="y":
        Insert_rows()
        insert=input("Do you want to enter another contact? y/n:")

    show=input("Do you want to view a contact? y/n:")
    while show=="y":
        Show_rows()
        show=input("Do you want to view another contact? y/n:")

    update=input("Do you want to update a contact? y/n:")
    while update=="y":
        Update_rows()
        update=input("Do you want to update another contact? y/n:")

    delete=input("Do you want to delete a contact? y/n:")
    while delete=="y":
        Delete_rows()
        delete=input("Do you want to delete another contact? y/n:")

if __name__ == '__main__':
    main()







