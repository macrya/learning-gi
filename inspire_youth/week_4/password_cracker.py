import random
import string
from multiprocessing import Pool, cpu_count
import time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def crack_password_worker(args):
    password, length = args
    attempts = 0
    while True:
        guess = generate_random_string(length)
        attempts += 1
        if guess == password:
            return attempts

def crack_password(password):
    length = len(password)
    processes = min(cpu_count(), 4)  # Limiting to a maximum of 4 processes
    with Pool(processes) as pool:
        start_time = time.time()
        results = pool.map(crack_password_worker, [(password, length)] * processes)
        end_time = time.time()
        total_attempts = sum(results)
        elapsed_time = end_time - start_time
        print(f"password zcx cracked in {total_attempts} attempts.")
        print(f"Time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    password = input("Enter the password to crack: ")
    print("Cracking password...")
    crack_password(password)

