#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
   lists all cities of that state, using the database hbtn_0e_4_usa
"""

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

    cursor.execute("""SELECT a.name
            FROM cities a
            LEFT JOIN states b
            ON a.state_id = b.id 
            WHERE b.name = %s
            ORDER BY a.id ASC
            """, (sys.argv[4],))

    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    connection.close()
