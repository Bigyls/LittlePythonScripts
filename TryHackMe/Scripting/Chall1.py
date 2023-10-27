import pwn
import os

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'assets/b64.txt')
i = 0

with open(file, "r", encoding="utf-8") as f:
    b64 = f.read()
    # Decode base64
    decoded = pwn.base64.b64decode(b64)
    decoded = pwn.base64.b64decode(decoded)
    decoded = pwn.base64.b64decode(decoded)
    while True:
        try:
            i += 1
            decoded = pwn.base64.b64decode(decoded)
            if i >= 47:
                print(decoded)
        except Exception as e:
            print(e)
            break