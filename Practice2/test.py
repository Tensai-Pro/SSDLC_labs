import multiprocessing
from hashlib import sha256
import time

# h1 = bytes().fromhex("1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad")
h2 = bytes().fromhex("3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b")
# h3 = bytes().fromhex("74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f")

# def brute():
#     global h1, h2, h3
#     letters = bytearray(5)
#     for letters[0] in range(97, 97 + 26):
#         for letters[1] in range(97, 97 + 26):
#             for letters[2] in range(97, 97 + 26):
#                 for letters[3] in range(97, 97 + 26):
#                     for letters[4] in range(97, 97 + 26):
#                         digest = sha256(letters).digest()
#                         if digest == h3:
#                             password = "".join(chr(x) for x in letters)
#                             print(password + " => " + digest.hex())
#                             return 0

isFound = multiprocessing.Value('i', 0)

def brute(firstletterascii: int):
    global h1, h2, h3
    letters = bytearray(5)
    letters[0] = firstletterascii
    for letters[1] in range(97, 97 + 26):
        for letters[2] in range(97, 97 + 26):
            for letters[3] in range(97, 97 + 26):
                for letters[4] in range(97, 97 + 26):
                    digest = sha256(letters).digest()
                    if digest == h2:
                        isFound.value = 1
                        password = "".join(chr(x) for x in letters)
                        print(password + " => " + digest.hex())
                        return 0
                if isFound.value == True: return 0
            if isFound.value == True: return 0
        if isFound.value == True: return 0
    if isFound.value == True: return 0


# def quit(i):
#     print(f"quitting with {i}")
#     p.terminate()

def main():
    start = time.time()

    # global p
    # p = multiprocessing.Pool()
    # p.map_async(brute, range(97, 123), callback=quit)
    # p.close()
    # p.join()

    with multiprocessing.Pool() as p:
        p.map(brute, range(97, 97 + 26))

    # brute()
    print(time.time() - start)

if __name__ == "__main__":
    main()
