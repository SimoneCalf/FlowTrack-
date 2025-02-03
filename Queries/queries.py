# connect to the database
import sqlite3



# function to validate the user
def validate_user(username, password):
    # Connect to the database (creates 'database.db' if it doesn't exist)
    conn = sqlite3.connect('Database/FlowTrackDB.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Execute a SQL command
    cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
    result = cursor.fetchone()
    print(result)
    # Close the connection
    conn.close()
    # when the user is not found
    if result is None:
        return False
    else:
        return result[0]
    
def add_mutation(amount, account, date, comment, category, user_id):
    # Connect to the database (creates 'database.db' if it doesn't exist)
    conn = sqlite3.connect('Database/FlowTrackDB.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Execute a SQL command
    cursor.execute("INSERT INTO Mutations (Amount, Account, Date, Comment, Category, User) VALUES (?, ?, ?, ?, ?, ?)", (amount, account, date, comment, category, user_id))
    conn.commit()
    # Close the connection
    conn.close()

# get all mutations from the user
def get_mutations(user_id):
    # Connect to the database
    conn = sqlite3.connect('Database/FlowTrackDB.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Execute a SQL command
    cursor.execute("SELECT * FROM Mutations WHERE User = ?", (user_id,))
    result = cursor.fetchall()
    # Close the connection
    conn.close()
    
    # Create a list of dictionaries
    list_mutations = []
 
    
    for row in result:
        mutation = {
            'mutation_id': row[0],
            'amount': row[1],
            'account': row[2],
            'date': row[3],
            'description': row[4],
            'category': row[5],
            'user': row[6]
        }
        list_mutations.append(mutation)

        # Sort the list of mutations by date in descending order
        list_mutations.sort(key=lambda x: x['date'])
    
    
    return list_mutations

# get the categories from the user
def get_categories(user_id):
    # Connect to the database
    conn = sqlite3.connect('Database/FlowTrackDB.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Execute a SQL command to get categories for the user's mutations
    cursor.execute('''
        SELECT DISTINCT c.category_id, c.name
        FROM Categories c
        JOIN Mutations m ON c.mutation = m.Mutation_id
        WHERE m.User = ?
    ''', (user_id,))
    result = cursor.fetchall()
    # Close the connection
    conn.close()
    
    # Create a list of dictionaries
    list_categories = []
    print(f'query_result: {result}')
    
    for row in result:
        category = {
            'category_id': row[0],
            'name': row[1]
        }
        list_categories.append(category)
    
    print(f'lijst: {list_categories}')
    return list_categories



    

   