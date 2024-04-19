import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Import functions
from management_function import add_khmer_food, add_italian_food, add_french_food, add_japanese_food, view_khmer_food, view_italian_food, view_french_food, view_japanese_food, search_khmer_food, search_italian_food, search_french_food, search_japanese_food

# Function to handle button click for adding food
def add_food_click():
    cuisine = cuisine_var.get()
    name = food_name_entry.get()
    recipe = food_recipe_entry.get()

    if cuisine == "Khmer":
        result = add_khmer_food(name, recipe)
    elif cuisine == "Italian":
        result = add_italian_food(name, recipe)
    elif cuisine == "French":
        result = add_french_food(name, recipe)
    elif cuisine == "Japanese":
        result = add_japanese_food(name, recipe)
    else:
        result = "Please select a cuisine."

    messagebox.showinfo("Result", result)

    # Clear input fields
    food_name_entry.delete(0, tk.END)
    food_recipe_entry.delete(0, tk.END)

# Function to handle button click for searching food
def search_food_click():
    cuisine = cuisine_var.get()
    name = food_search_entry.get()

    if cuisine == "Khmer":
        result = search_khmer_food(name)
    elif cuisine == "Italian":
        result = search_italian_food(name)
    elif cuisine == "French":
        result = search_french_food(name)
    elif cuisine == "Japanese":
        result = search_japanese_food(name)
    else:
        result = "Please select a cuisine."

    if isinstance(result, str):
        messagebox.showinfo("Result", result)
    else:
        show_search_results(result)

    # Clear input field
    food_search_entry.delete(0, tk.END)

# Function to display search results in a separate window
def show_search_results(results):
    result_window = tk.Toplevel(root)
    result_window.title("Search Results")
    result_text = scrolledtext.ScrolledText(result_window, width=50, height=10, font=("Helvetica", 14))
    result_text.pack(expand=True, fill='both')

    for row in results:
        result_text.insert(tk.END, f"{row}\n")

# Function to handle button click for viewing food
def view_food_click():
    cuisine = cuisine_var.get()

    if cuisine == "Khmer":
        result = view_khmer_food()
    elif cuisine == "Italian":
        result = view_italian_food()
    elif cuisine == "French":
        result = view_french_food()
    elif cuisine == "Japanese":
        result = view_japanese_food()
    else:
        result = "Please select a cuisine."

    show_view_results(result)

# Function to display view results in a separate window
def show_view_results(results):
    result_window = tk.Toplevel(root)
    result_window.title("View Results")
    result_text = scrolledtext.ScrolledText(result_window, width=50, height=10, font=("Helvetica", 14))
    result_text.pack(expand=True, fill='both')

    for row in results:
        result_text.insert(tk.END, f"{row}\n")

# Create the main tkinter window
root = tk.Tk()
root.title("Recipe Manager")

# Cuisine selection
cuisine_label = tk.Label(root, text="Select Cuisine:", font=("Helvetica", 16))
cuisine_label.grid(row=0, column=0)
cuisine_var = tk.StringVar()
cuisine_var.set("Khmer")
cuisine_option = tk.OptionMenu(root, cuisine_var, "Khmer", "Italian", "French", "Japanese")
cuisine_option.config(font=("Helvetica", 14))
cuisine_option.grid(row=0, column=1)

# Food details
food_name_label = tk.Label(root, text="Name:", font=("Helvetica", 16))
food_name_label.grid(row=1, column=0)
food_name_entry = tk.Entry(root, font=("Helvetica", 14))
food_name_entry.grid(row=1, column=1)

food_recipe_label = tk.Label(root, text="Recipe:", font=("Helvetica", 16))
food_recipe_label.grid(row=2, column=0)
food_recipe_entry = tk.Entry(root, font=("Helvetica", 14))
food_recipe_entry.grid(row=2, column=1)

# Buttons for actions
add_food_button = tk.Button(root, text="Add", command=add_food_click, font=("Helvetica", 16))
add_food_button.grid(row=3, column=0, columnspan=2, pady=10)

food_search_label = tk.Label(root, text="Search:", font=("Helvetica", 16))
food_search_label.grid(row=4, column=0)
food_search_entry = tk.Entry(root, font=("Helvetica", 14))
food_search_entry.grid(row=4, column=1)

search_food_button = tk.Button(root, text="Search", command=search_food_click, font=("Helvetica", 16))
search_food_button.grid(row=5, column=0, columnspan=2, pady=10)



view_food_button = tk.Button(root, text="View All", command=view_food_click, font=("Helvetica", 16))
view_food_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()