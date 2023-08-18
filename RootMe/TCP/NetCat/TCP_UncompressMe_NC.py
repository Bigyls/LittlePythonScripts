import socket, zlib, base64

# Server connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('challenge01.root-me.org', 52022))

while True:
    # Catch first message and print it
    msg = server.recv(2048).decode('UTF-8')
    print(msg)

    # Decode base64 message
    decoded = base64.b64decode(msg.split("'")[1].replace("'", ''))

    # Decompress decoded message
    decompressed = zlib.decompress(decoded).decode('UTF-8')

    # Send result
    server.send(f"{decompressed}\n".encode('UTF-8'))