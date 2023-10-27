import requests
import time
import socket

# Define the initial number and starting port
current_number = 0.00  # Initialize as a float with two decimal places
current_port = 1337

# Define the base URL
base_url = f"http://10.10.218.6:{current_port}"

# Function to perform an operation and return the result
def perform_operation(operation, number):
    if operation == "add":
        return round(current_number + number, 2)
    elif operation == "minus":
        return round(current_number - number, 2)
    elif operation == "multiply":
        return round(current_number * number, 2)
    elif operation == "divide":
        if number == 0:
            raise ValueError("Division by zero")
        return round(current_number / number, 2)
    else:
        raise ValueError("Invalid operation")

# Function to check if a port is open
def isPortOpen(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for the connection attempt
            result = s.connect_ex(('10.10.218.6', port))
            return result == 0  # Port is open if the result is 0
    except Exception as e:
        return False  # Port is not open in case of any exception

# Wait for port 1337 to be open
while not isPortOpen(current_port):
    print(f"Waiting for port {current_port} to open...")
    time.sleep(5)

print(f"Port {current_port} is open. Proceeding to the main loop.")

# Main loop
while True:
    try:
        # Make the request
        response = requests.get(base_url)
        print(response.text)
        if response.text.strip().startswith("STOP"):
            break

        # Parse the response
        data = response.text.strip().split()
        operation, number, next_port = data[0], float(data[1]), int(data[2])

        # Perform the operation and update the current number
        current_number = perform_operation(operation, number)

        # Update the current port and URL
        current_port = next_port
        base_url = f"http://10.10.218.6:{current_port}"
        time.sleep(5)
        print(current_number)

    except Exception as e:
        print("Error:", str(e))

print("Reached port 9765 or received STOP signal. Exiting.")
print("Final current_number:", current_number)
