import socket

# Server connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('challenge01.root-me.org', 52021))

# Decode rot13 message
def rot13(ciphertext):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

# Catch first message and print it
msg = server.recv(2048).decode('UTF-8')
print(msg)

decoded = rot13(msg.split("'")[1].replace("'", ''))

# Send result
server.send(f"{decoded}\n".encode('UTF-8'))

# Print flag
print(server.recv(2048).decode('UTF-8'))