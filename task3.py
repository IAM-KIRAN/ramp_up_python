import os
import re

def valid_ip(ip):
    pattern = r"(\d{1,3}\.){3}\d{1,3}"
    return re.match(pattern, ip)


while True:
    input_ip = input("Do you want to enter IPs into file: ")
    if input_ip.lower() == "yes":
        ip = input("Enter IP: ")
        if valid_ip(ip):
            response = os.popen(f"ping {ip}").read()
            if "Received = 4" in response:
                print(f"IP address {ip} pinging successfully.")
                with open("ip.txt", "a") as file:
                    file.write(ip + '\n')
                    print("IP added to the file.")
                print("------------------------------------------")
            else:
                print(f"Pinging IP address {ip} unsuccessful.")
                with open("invalid_ip.txt", "a") as file:
                    file.write(ip + '\n')
                    print("IP added to the file.")
                print("------------------------------------------")
        else:
            print("Please Enter valid input.")
            print("------------------------------------------")
    elif input_ip.lower() == "no" or input_ip.lower() == "exit":
        print("EXITED")
        print("-------------Valid IPs in file-------------")
        file_path = "IP.txt"
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("------------Invalid IPs in file------------")
        file_path2 = "invalid_ip.txt"
        try:
            with open(file_path2, "r") as file:
                file_content2 = file.read()
                print(file_content2)
        except FileNotFoundError:
            print(f"File '{file_path2}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("------------------------------------------")

        break
    else:
        print("Enter valid input.")




