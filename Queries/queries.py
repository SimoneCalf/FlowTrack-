# connect to the database
import sqlite3



# function to validate the user
def validate_user(username, password):
    # Connect to the database (creates 'database.db' if it doesn't exist)
    conn = sqlite3.connect('Database/FlowTrackDB.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Execute a SQL command
    cursor.execute("SELECT Username, Password FROM Users WHERE Username = ? AND Password = ?", (username, password))
    result = cursor.fetchone()
    print(result)
    # Close the connection
    conn.close()
    # when the user is not found
    if result is None:
        return False
    else:
        return True

    

   