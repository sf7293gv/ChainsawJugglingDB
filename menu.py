"""
A menu - you need to add the database and fill in the functions. 
"""


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

def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()