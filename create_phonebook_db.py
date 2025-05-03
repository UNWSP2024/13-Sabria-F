#Author: Sabria Fafach
#Date: May 2, 2025
#Title: create_phonebook_db.py



import sqlite3


def main():
    #Connect to the database:
    conn=sqlite3.connect('phonebook.db')

    #Get a database cursor:
    cur=conn.cursor()

    #Add the Entries table:
    add_entries_table(cur)

    #Commit the changes:
    conn.commit()

    #Display the cities:
    display_entries(cur)

    #Close the connection:
    conn.close()


#The add_entries_table adds the Entries table to the database:
def add_entries_table(cur):
    #If the table already exists, drop it:
    cur.execute('DROP TABLE IF EXISTS entries')

    #Create the table.
    cur.execute('''CREATE TABLE Entries (PhoneID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        Number TEXT)''')


# The display_entries function displays the contents of the Entries table:
def display_entries(cur):
    print('Contents of entries.db/Entries table:')
    cur.execute('SELECT * FROM entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]}')



if __name__ == '__main__':
    main()
