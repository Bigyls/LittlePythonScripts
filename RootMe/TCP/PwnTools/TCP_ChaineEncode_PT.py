import pwn

r = pwn.remote('challenge01.root-me.org', 52023)

# Catch first message and print it
msg = r.recv().decode('UTF-8')
print(msg)

# Decode base64 message
decoded = pwn.base64.b64decode(msg.split("'")[1].replace("'", '')).decode('UTF-8')

# Send result
r.send(f"{decoded}\n".encode('UTF-8'))

# Print flag
print(r.recv().decode('UTF-8'))