# https://trycrack.me/chall?ch=8
import pwn
import string
import itertools

password= bytes.fromhex("3a2a2e1e3659113a5f1a3c335d1b1a3a2d590d031b5b064413")

# Generate all possible input
alphabet = list(string.ascii_lowercase)
alphabet_permutation = itertools.permutations(alphabet, 4)

# Loop for try all input possiblities
for permutation in alphabet_permutation:
    your_input = "".join(permutation) # hint: (4 characters)
    enc_password = pwn.xor(password, your_input)

    # If condition for check the flag
    if "TCM{X0r_1s" in str(enc_password):
        print("Your input: " + your_input)
        print("Good Job!")

    # Else conitnue brute force
    else:
        continue