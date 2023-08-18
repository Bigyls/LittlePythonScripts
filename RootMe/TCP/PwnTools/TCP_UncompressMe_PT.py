import pwn, zlib

r = pwn.remote('challenge01.root-me.org', 52022)

while True:
    # Catch first message and print it
    msg = r.recv().decode('UTF-8')
    print(msg)

    # Decode base64 message
    decoded = pwn.base64.b64decode(msg.split("'")[1].replace("'", ''))

    # Decompress decoded message
    decompressed = zlib.decompress(decoded).decode('UTF-8')

    # Send result
    r.send(f"{decompressed}\n".encode('UTF-8'))