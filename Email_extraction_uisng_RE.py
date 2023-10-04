import re

email_pattern = r'\B[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,7}\B'

try:
    with open('emails.txt', 'r') as file:
        text = file.read()

    email_addresses = re.findall(email_pattern, text)

    if email_addresses:
        for email in email_addresses:
            print(email)
    else:
        print("No email addresses found in the text.")

except FileNotFoundError:
    print("The file 'emails.txt' was not found.")
except IOError:
    print("An error occurred while reading the file.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")