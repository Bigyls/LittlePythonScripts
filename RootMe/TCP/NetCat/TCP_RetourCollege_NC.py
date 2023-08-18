import socket, re, math

# Server connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('challenge01.root-me.org', 52002))

# Multipy the square root of number1 by number2
def multiply(square, number2):
    return square * number2

# Catch first message and print it
msg = server.recv(2048).decode('UTF-8')
print(msg)

# Extract numbers of the messages
number1 = int(re.findall(r'\d+', msg)[1])
number2 = int(re.findall(r'\d+', msg)[2])

# Send result
server.send(f"{round(multiply(math.sqrt(number1), number2), 2)}\n".encode('UTF-8'))

# Print flag
print(server.recv(2048).decode('UTF-8'))