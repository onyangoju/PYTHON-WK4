def read_and_modify_file():
    filename = input("Enter the filename to read (e.g., pauline_onyango.txt): ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()  # Example modification: Convert to uppercase

        new_filename = f"pauline_onyango_modified.txt"
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content saved to {new_filename}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Check file permissions.")

read_and_modify_file()



