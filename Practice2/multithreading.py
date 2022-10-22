import itertools
import multiprocessing
import hashlib
import time


isFound = multiprocessing.Value('i', 0)
class Multithreading(object):
    def __init__(self, hash):
        self.hash = bytes().fromhex(hash)
        self.ascii_from = 97
        self.ascii_to = 123


    def attack(self, firstletterascii: int):
        letters = bytearray(5)
        letters[0] = firstletterascii
        for letters[1] in range(self.ascii_from, self.ascii_to):
            for letters[2] in range(self.ascii_from, self.ascii_to):
                for letters[3] in range(self.ascii_from, self.ascii_to):
                    for letters[4] in range(self.ascii_from, self.ascii_to):
                        digest = hashlib.sha256(letters).digest()
                        if digest == self.hash:
                            isFound.value = 1
                            password = "".join(chr(x) for x in letters)
                            print(f"\nPassword: {password}")
                            return 0
                    if isFound.value == 1: return 0
                if isFound.value == 1: return 0
            if isFound.value == 1: return 0


    def start_bruteforce(self):
        start = time.time()
        with multiprocessing.Pool() as p:
            p.map(self.attack, range(self.ascii_from, self.ascii_to))
        print(f"Time for multithreading bruteforce attack:: {time.time() - start} sec.")




    # cores_count = multiprocessing.cpu_count()
    # print(f"\nYou have {cores_count} cores. How many do you want to use for multithreading?")
    # cores = int(input("Enter a number: "))

    # if cores <= 4 or cores > 0:
    #     get_processes(cores, hash)
    # else:
    #     print("\n\tInvalid input. Try again.")
    #     start_bruteforce(hash)


# def get_processes(cores, hash):
#     processes = []
#     op_cnt = len(combinations) // 4
#     start_arr = 0
#     isFound = multiprocessing.Value('i', 0)
#     start = time.time()

#     with multiprocessing.Pool() as pool:
#         pool.map(attack(hash), combinations)

#     # for core in range(cores):
#     #     if core == cores - 1:
#     #         comb = combinations[start_arr:-1]
#     #         proc = multiprocessing.Process(target=attack, args=(core+1, hash, comb, isFound, start))
#     #         processes.append(proc)
#     #         # proc.start()
#     #     else:
#     #         comb = combinations[start_arr:start_arr + op_cnt - 1]
#     #         proc = multiprocessing.Process(target=attack, args=(core+1, hash, comb, isFound, start))
#     #         processes.append(proc)
#     #         start_arr += op_cnt
#     #         # proc.start()

    
#     # for proc in processes:
#     #     proc.start()

#     # for proc in processes:
#     #     proc.join()

#     # if finished_time.value != 0.0:
#     #     print(f"Time for multithreading to bruteforce attack: {finished_time.value}.")
#     # else:
#     #     print('\nPassword not found')


# def attack(comb, hash):
#     isFound = False
#     # print(f"Thread {number} started")
#     # start = time.time()

#     # for combination in own_combinations:
#         guess = ''.join(comb)
#         # print(f"Thread {number} is trying: {guess}")
#         hashed_guess = hashlib.sha256(guess.encode())

#         if flag.value == 1:
#             print(f"\nThread{number} finished because of flag. Last guess on position: {own_combinations.index(tuple(guess))}")
#             break

#         if hashed_guess.hexdigest() == hash:
#             isFound = True
#             print(f'\nThread{number} guessed password:', guess)
#             end = time.time()
#             print(f"Time for thread {number} to bruteforce attack: {end - start}.")
#             break

#     print(f"Thread {number} finished")  
#     # end = time.time()

#     # if isFound == True:
#     #     print(f"Time for thread #{number} to bruteforce attack: {end - start}.")
