#Author: Sabria Fafach
#Date: May 1, 2025
#Title: Display_cities.py


import sqlite3


def main():
    #Connect to the database:
    conn=sqlite3.connect("cities.db")

    #Get a cursor:
    cur=conn.cursor()

    #Get all columns:
    cur.execute("SELECT * FROM Cities")

    #Fetch the results of the SELECT statement:
    results=cur.fetchall()

    #Iterate over the rows and display the results:
    for row in results:
        print(f"{row[0]:30} {row[1]:5}     {row[2]:5}")

    #CLose the database connection:
    conn.close()

if __name__ == '__main__':
    main()



