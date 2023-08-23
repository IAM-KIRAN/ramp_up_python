import re

while True:
    input_string = input("Do you want to enter emails into file: ")
    if input_string.lower() == "yes":
        input_email = input("Enter email: ")
        pattern = r"[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        match = re.findall(pattern, input_email)
        if match:
            print("Valid email address.")
            try:
                with open("email.txt", "a") as file:
                    file.write(input_email + '\n')
                    print("Email added to the file.")
            except FileNotFoundError:
                print("File not found")
            except PermissionError:
                print("Permission denied")

        else:
            print("Invalid email address.")
    elif input_string.lower() == "no" or "exit":
        print("Exited")
        file_path = "email.txt"  # Replace with your file path
        try:
            with open(file_path, "r") as file:
                # Read the content of the file
                file_content = file.read()

                # Print the content
                print(file_content)

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        break
    else:
        print("Enter valid input.")

