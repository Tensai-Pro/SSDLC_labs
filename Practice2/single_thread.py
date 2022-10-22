import os.path
import time
import itertools
import hashlib


class SingleThread(object):
    def __init__(self, hash):
        self.hash = bytes().fromhex(hash)
        self.ascii_from = 97
        self.ascii_to = 123


    def start_bruteforce(self):
        start = time.time()
        letters = bytearray(5)
        for letters[0] in range(self.ascii_from, self.ascii_to):
            for letters[1] in range(self.ascii_from, self.ascii_to):
                for letters[2] in range(self.ascii_from, self.ascii_to):
                    for letters[3] in range(self.ascii_from, self.ascii_to):
                        for letters[4] in range(self.ascii_from, self.ascii_to):
                            digest = hashlib.sha256(letters).digest()
                            if digest == self.hash:
                                password = "".join(chr(x) for x in letters)
                                print(f"\nPassword: {password}")
                                print(f"Time for single thread bruteforce attack:: {time.time() - start} sec.")
                                return 0


#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     isFound = False
#     combinations = list(itertools.product(alphabet, repeat=5))

#     start = time.time()

#     for combination in combinations:
#         guess = ''.join(combination)
#         hashed_guess = hashlib.sha256(guess.encode())
#         if hashed_guess.hexdigest() == hash:
#             print('\nPassword:', guess)
#             isFound = True
#             break

#     if isFound == False:
#         print('\nPassword not found')
#     else:
#         end = time.time()
#         print(f"Time for single thread bruteforce attack: {end - start}.")
