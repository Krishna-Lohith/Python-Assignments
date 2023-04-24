import multiprocessing
import time
import datetime
import random

def wait_and_print():
    # Wait for a random number of seconds between 1 and 5
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)

    # Print the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Process {multiprocessing.current_process().name} waited {wait_time} seconds and printed at {current_time}")

if __name__ == "__main__":
    # Create three separate processes
    process1 = multiprocessing.Process(target=wait_and_print, name="Process 1")
    process2 = multiprocessing.Process(target=wait_and_print, name="Process 2")
    process3 = multiprocessing.Process(target=wait_and_print, name="Process 3")

    # Start the processes
    process1.start()
    process2.start()
    process3.start()

    # Wait for the processes to finish
    process1.join()
    process2.join()
    process3.join()
