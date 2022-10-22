import single_thread
import multithreading

import os.path


def main():
    is_from_console = choose_hash()
    choose_thread(is_from_console)
    

def choose_hash():
    print("\n\nDo you want to read hash from the console or file?")
    print("1. Console.")
    print("2. File.")
    answer = input("Enter a number: ")

    if answer == '1':
        return True
    elif answer == '2':
        return False
    else:
        print("\n\tInvalid input. Try again.")
        choose_hash()


def choose_thread(is_from_console):
    print("\nHow do you want to execute this program?")
    print("1. Single thread.")
    print("2. Multithreading.")
    answer = input("Enter a number: ")

    if answer == '1':
        if is_from_console:
            hash = input("\nEnter hash: ")
            st = single_thread.SingleThread(hash)
            print("\nProcessing...")
            st.start_bruteforce()
        else:
            hash = take_hash()
            if hash != '': 
                st = single_thread.SingleThread(hash)
                print("\nProcessing...")
                st.start_bruteforce()
    elif answer == '2':
        if is_from_console:
            hash = input("\nEnter hash: ")
            mt = multithreading.Multithreading(hash)
            print("\nProcessing...")
            mt.start_bruteforce()
        else:
            hash = take_hash()
            if hash != '': 
                mt = multithreading.Multithreading(hash)
                print("\nProcessing...")
                mt.start_bruteforce()
    else:
        print("\n\tInvalid input. Try again.")
        choose_thread(is_from_console)


def take_hash():
    while True:
        print("\nMake sure your file contains only one hash value.")
        path = input("Enter path to hash: ")
        if os.path.exists(path):
            with open(path, 'r') as file_handler:
                hash = file_handler.read()
                if hash != '':
                    return hash.replace('\n', '')
                else:
                    print("\n\tFile is empty. Try again.")
        else:
            print("\n\tFile not found. Try again.")


if __name__ == "__main__":
    main()