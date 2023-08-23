import os
while(True):
    input_ip = input("Do you want to enter IPs into file: ")
    if input_ip.lower() == "yes":
        ip = input("Enter IP: ")
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            print(f"IP address {ip} pinging successfully.")
            print("------------------------------------------")
        else:
            print(f"Pinging IP address {ip} unsuccessful.")
            print("------------------------------------------")
    elif input_ip.lower() == "no" or "exit":
        print("EXITED")
        print("------------------------------------------")
        break
    else:
        print("Enter valid input.")
        print("------------------------------------------")
