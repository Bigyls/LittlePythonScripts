import pwn

r = pwn.remote('challenge01.root-me.org', 52002)

# Multipy the square root of number1 by number2
def multiply(square, number2):
    return square * number2

# Catch first message and print it
msg = r.recv().decode('UTF-8')
print(msg)

# Extract numbers of the messages
number1 = int(pwn.re.findall(r'\d+', msg)[1])
number2 = int(pwn.re.findall(r'\d+', msg)[2])

# Send result
r.send(f"{round(multiply(pwn.math.sqrt(number1), number2), 2)}\n".encode('UTF-8'))

# Print flag
print(r.recv().decode('UTF-8'))