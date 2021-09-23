"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3
db = 'juggling_db.sqlite'

def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        create_table() # Call this function to create table
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


""" Create the juggling table if it does not already exist """
def create_table(): 
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS juggling (name text, country text, num_of_catches int)')
    conn.close()

""" Function that will display all the records in table when called """
def display_all_records():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM juggling')
    for row in results:
        print(row)
    conn.close()

""" Function that will add new a record to the table when called """
def add_new_record():
    name = input('Enter juggler name: ')
    country = input('Enter juggler\'s country: ')
    catches_num = int(input('Enter juggler\'s amount of catches: '))
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO juggling VALUES (?, ?, ?)', (name, country, catches_num))
    conn.close()

""" Function that will update an existing record when called """
def edit_existing_record():
    update_juggler = input('Enter Juggler\'s name to update: ')
    catches_num = int(input('Enter new amount of catches: '))
    
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE juggling SET num_of_catches = ? WHERE name = ? ', (catches_num, update_juggler))
    conn.close()

""" Fuinction that will delete a record from table when called """
def delete_record():
    update_juggler = input('Enter Juggler\'s name to delete record: ')
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE FROM juggling WHERE name = ?', (update_juggler,))
    conn.close()

if __name__ == '__main__':
    main()