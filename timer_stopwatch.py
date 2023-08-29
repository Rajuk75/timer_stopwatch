#timer and stopwatch

#using time module

import time

def countdown_timer(seconds):
    print(f"Countdown timer started for {seconds} seconds.")
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def stopwatch():
    input("Press Enter to start the stopwatch.")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            print(f"{int(hours):02}:{int(mins):02}:{int(secs):02}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")

def main():
    print("Timer and Stopwatch Program")
    while True:
        print("1. Countdown Timer")
        print("2. Stopwatch")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            seconds = int(input("Enter the countdown time in seconds: "))
            countdown_timer(seconds)
        elif choice == "2":
            stopwatch()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
