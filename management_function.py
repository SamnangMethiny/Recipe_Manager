import sqlite3
import os
from pprint import pprint

db_path = 'data/database.sqlite'
if not os.path.exists(db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)

#-----------------Create tables in database-----------------
def initialize():
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS khmer_foods(
            khmer_food_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            khmer_food_name CHAR(50) NOT NULL,
            khmer_food_recipe CHAR(100) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS italian_foods(
            italian_food_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            italian_food_name CHAR(50) NOT NULL,
            italian_food_recipe CHAR(100) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS french_foods(
            french_food_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            french_food_name CHAR(50) NOT NULL,
            french_food_recipe CHAR(100) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS japanese_foods(
            japanese_food_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            japanese_food_name CHAR(50) NOT NULL,
            japanese_food_recipe CHAR(100) NOT NULL
        );
''')


# ---------------Add data to database-----------------
def add_khmer_food(khmer_food_name:str,khmer_food_recipe:str)->str:

    # Check if inputs are not empty and are strings
    if not khmer_food_name or not khmer_food_recipe or \
            not isinstance(khmer_food_name, str) or not isinstance(khmer_food_recipe, str):
        return 'Invalid input. Please provide valid name and recipe.'

    # Check if khmer food name contains only alphabetic characters
    if not khmer_food_name.isalpha():
        return 'Name should contain only alphabetic characters.'

    # Construct and execute a parameterized query to prevent SQL injection
    query = 'INSERT INTO khmer_foods (khmer_food_name, khmer_food_recipe) VALUES (?, ?)'
    try:
        conn.execute(query, (khmer_food_name, khmer_food_recipe))
        conn.commit()
        return 'New recipe added successfully!'
    except Exception as e:
        # Handle any exceptions, such as database errors
        return f'Error: {str(e)}'


def add_italian_food(italian_food_name: str, italian_food_recipe: str) -> str:
    # Check if inputs are not empty and are strings
    if not italian_food_name or not italian_food_recipe or \
            not isinstance(italian_food_name, str) or not isinstance(italian_food_recipe, str):
        return 'Invalid input. Please provide valid name and recipe.'

    # Check if Italian food name contains only alphabetic characters
    if not italian_food_name.isalpha():
        return 'Name should contain only alphabetic characters.'

    # Construct and execute a parameterized query to prevent SQL injection
    query = 'INSERT INTO italian_foods (italian_food_name, italian_food_recipe) VALUES (?, ?)'
    try:
        conn.execute(query, (italian_food_name, italian_food_recipe))
        conn.commit()
        return 'New recipe added successfully!'
    except Exception as e:
        # Handle any exceptions, such as database errors
        return f'Error: {str(e)}'


def add_french_food(french_food_name:str,french_food_recipe:str)->str:

    # Check if inputs are not empty and are strings
    if not french_food_name or not french_food_recipe or \
            not isinstance(french_food_name, str) or not isinstance(french_food_recipe, str):
        return 'Invalid input. Please provide valid name and recipe.'

    # Check if french food name contains only alphabetic characters
    if not french_food_name.isalpha():
        return 'Name should contain only alphabetic characters.'

    # Construct and execute a parameterized query to prevent SQL injection
    query = 'INSERT INTO french_foods (french_food_name, french_food_recipe) VALUES (?, ?)'
    try:
        conn.execute(query, (french_food_name, french_food_recipe))
        conn.commit()
        return 'New recipe added successfully!'
    except Exception as e:
        # Handle any exceptions, such as database errors
        return f'Error: {str(e)}'
    

def add_japanese_food(japanese_food_name:str,japanese_food_recipe:str)->str:

    # Check if inputs are not empty and are strings
    if not japanese_food_name or not japanese_food_recipe or \
            not isinstance(japanese_food_name, str) or not isinstance(japanese_food_recipe, str):
        return 'Invalid input. Please provide valid name and recipe.'

    # Check if japanese food name contains only alphabetic characters
    if not japanese_food_name.isalpha():
        return 'Name should contain only alphabetic characters.'

    # Construct and execute a parameterized query to prevent SQL injection
    query = 'INSERT INTO japanese_foods (japanese_food_name, japanese_food_recipe) VALUES (?, ?)'
    try:
        conn.execute(query, (japanese_food_name, japanese_food_recipe))
        conn.commit()
        return 'New recipe added successfully!'
    except Exception as e:
        # Handle any exceptions, such as database errors
        return f'Error: {str(e)}'
    

# -------------Retrieve all data from database-----------------
def display_data_format(result):
    formatted_result = []
    for row in result:
        formatted_row = [
            f"ID: {row[0]}",  
            f"Name: {row[1]}", 
            f"Ingredient: {row[2]}"  
        ]
        formatted_result.append('\n'.join(formatted_row))
    return formatted_result

def view_khmer_food():
    command = conn.execute('SELECT * FROM khmer_foods')
    result = command.fetchall()

    return display_data_format(result)

# pprint(view_khmer_food())

def view_italian_food():
    command = conn.execute('SELECT * FROM italian_foods')
    result = command.fetchall()

    return display_data_format(result)

# pprint(view_italian_food())

def view_french_food():
    command = conn.execute('SELECT * FROM french_foods')
    result = command.fetchall()

    return display_data_format(result)
        
# pprint(view_french_food())

def view_japanese_food():
    command = conn.execute('SELECT * FROM japanese_foods')
    result = command.fetchall()

    return display_data_format(result)

# pprint(view_japanese_food())

# -------------Retrieve data from database using name-----------------

def search_khmer_food(khmer_food_name: str) -> list:
        
        if not isinstance(khmer_food_name, str):
            return 'Please enter a recipe name'
        else:
            command = conn.execute(f"SELECT * FROM khmer_foods WHERE khmer_food_name LIKE '%{khmer_food_name}%'")
            result = command.fetchall()

        if result:
            return display_data_format(result)
        else:
            return 'Sorry, we do not have this recipe.'

# print(search_khmer_food("noodle"))

def search_italian_food(italian_food_name: str) -> list:

        if not isinstance(italian_food_name, str):
            return 'Please enter a recipe name'
        else:
            command = conn.execute(f"SELECT * FROM italian_foods WHERE italian_food_name LIKE '%{italian_food_name}%'")
            result = command.fetchall()

        if result:
            return display_data_format(result)
        else:
            return 'Sorry, we do not have this recipe.'
        
# print(search_italian_food("spaghetti"))

def search_french_food(french_food_name: str) -> list:
        
        if not isinstance(french_food_name, str):
            return 'Please enter a recipe name'
        else:
            command = conn.execute(f"SELECT * FROM french_foods WHERE french_food_name LIKE '%{french_food_name}%'")
            result = command.fetchall()

        if result:
            return display_data_format(result)
        else:
            return 'Sorry, we do not have this recipe.'
        
# print(search_french_food("co"))

def search_japanese_food(japanese_food_name: str) -> list:
        
        if not isinstance(japanese_food_name, str):
            return 'Please enter a recipe name'
        else:
            command = conn.execute(f"SELECT * FROM japanese_foods WHERE japanese_food_name LIKE '%{japanese_food_name}%'")
            result = command.fetchall()

        if result:
            return display_data_format(result)
        else:
            return 'Sorry, we do not have this recipe.'
        
# print(search_japanese_food("ro"))

if __name__ == '__main__':
    initialize()
    print(f'data initialization: Ok')