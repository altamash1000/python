import os

def write_file():
    file_name = input("Enter the name of the file to write: ")
    content = input("Enter the content for the file: ")
    with open(file_name, 'w') as file:
        file.write(content)
    print("File written successfully.")

def read_file():
    file_name = input("Enter the name of the file to read: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File does not exist.")

def rename_file():
    old_name = input("Enter the current name of the file: ")
    new_name = input("Enter the new name for the file: ")
    try:
        os.rename(old_name, new_name)
        print("File renamed successfully.")
    except FileNotFoundError:
        print("File does not exist.")

def delete_file():
    file_name = input("Enter the name of the file to delete: ")
    try:
        os.remove(file_name)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File does not exist.")

def edit_file():
    file_name = input("Enter the name of the file to edit: ")
    try:
        with open(file_name, 'r+') as file:
            content = file.read()
            print("Current file content:")
            print(content)
            new_content = input("Enter the new content: ")
            file.seek(0)
            file.write(new_content)
            file.truncate()
        print("File edited successfully.")
    except FileNotFoundError:
        print("File does not exist.")

def main():
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")
    
    while True:
        print("\nOptions:")
        print("1. Write a file")
        print("2. Read a file")
        print("3. Rename a file")
        print("4. Delete a file")
        print("5. Edit a file")
        print("6. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            write_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            rename_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            edit_file()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
