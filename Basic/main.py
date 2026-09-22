import mysql.connector

# Connect to MySQL
dbConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="studentdb"
)

print("MySQL Connected Successfully")

dbCommand = dbConnection.cursor()

def get_student():
    dbCommand.execute("SELECT * FROM student")

    result = dbCommand.fetchall()

    for row in result:
        print(row)

get_student()

dbCommand.close()
dbConnection.close()