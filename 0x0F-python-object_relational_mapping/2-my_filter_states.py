#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cursor = connection.cursor()

    searched_state = sys.argv[4]

    cursor.execute(
            "SELECT * FROM states WHERE name = %s" % f"'{searched_state}'"
            )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
