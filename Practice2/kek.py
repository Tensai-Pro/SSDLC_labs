import hashlib
import itertools
import time
from string import ascii_lowercase


hash = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'
# TODO range ASCII
alphabet = 'abcdefghijklmnopqrstuvwxyz'
isFound = False
        
combinations = list(itertools.product(alphabet, repeat=5))
print(len(combinations))    #11881376
start = time.time()



# print(hashlib.sha256(''.join(combinations[0]).encode('utf-8')).hexdigest())
for combination in combinations:
    guess = ''.join(combination)
    hashed = hashlib.sha256(guess.encode())
    if hashed.hexdigest() == hash:
        print('Password:', guess)
        isFound = True
        break

if isFound == False:
    print('Password not found')

end = time.time()
print(f"Time for single thread operation: {end - start}")




# print(chr(ord(alphabet[0]) + 3))
# def get_permutation(k, n=123):
#     combinations = []
#     combinations.append('a' * k)
#     while True:
#         for i in range(k-1, -1, -1):
#             if ord(combinations[-1][i]) < n - 1:
#                 break
#             else:
#                 combination = combinations[-1][0:4] + chr(ord(combinations[-1][i]) + 1)
#                 for j in range(i + 1, k):
#                     combination = combination + 
#         else:
#             return combinations
        