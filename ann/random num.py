import time
import getch

def random_number(max_number):
    start_time = time.time()
    getch.getch()
    end_time = time.time()
    elapsed_time = end_time - start_time
    random_number = int(elapsed_time * 1000000) % max_number
    return random_number

print(random_number(100))