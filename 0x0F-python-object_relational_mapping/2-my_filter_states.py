#!/usr/bin/python3
""" Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":

    import MySQLdb
    import sys

    if len(sys.argv) == 5:
        username = sys.argv[1]
        upassword = sys.argv[2]
        dbname = sys.argv[3]
        sSearch = sys.argv[4]
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=upassword,
            db=dbname,
            port=3306)

        cursor = db.cursor()
        squery = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(
            sSearch)

        cursor.execute(squery)
        query_rows = cursor.fetchall()
        for row in query_rows:
            print("({}, '{}'".format(row[0], row[1]))

        cursor.close()
        db.close()
