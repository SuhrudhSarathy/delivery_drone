from threading import Thread
from time import sleep

thread1_val = True
thread2_val = True
thread1_thread = None
thread2_thread = None

# Write threads that do multiple stuff and cancel other threads
def thread1():
    # loop at 10Hz
    try:
        while thread1_val:
            print("Looping thread 1, 10Hz")
            sleep(0.1)
    except KeyboardInterrupt:
        close_threads()

def thread2():
    try:
        while thread2_val:
            # loop at 1 Hz
            print("Looping thread 2, 1Hz")
            sleep(1)
    except KeyboardInterrupt:
        close_threads()

def main():
    global thread1_val
    global thread2_val
    global thread1_thread
    global thread2_thread

    # Starts the threads and waits for the input
    thread1_thread = Thread(target=thread1)
    thread2_thread = Thread(target=thread2)

    thread2_thread.start()
    thread1_thread.start()
    try:
        while True:
            print("Running at 0.5 Hz")
            sleep(2)
    except KeyboardInterrupt as e:
        # close all the threads
        # Print a message after all the threads are closed
        print(e)
        # Stopping thread 1
        thread1_val = False
        thread1_thread.join()
        print("Closed thread 1")

        sleep(2)

    finally:
        # Join all threads here
        thread2_val = False
        thread2_thread.join()
        print("Closed thread 2 too")

def close_threads():
    print("Closing F Threads")
    global thread1_val
    global thread2_val
    global thread1_thread
    global thread2_thread

    thread1_val = False
    thread1_thread.join()
    print("Closed thread 1")


    thread2_val = False
    thread2_thread.join()
    print("Closed thread 2 too")

if __name__ == "__main__":
    main()