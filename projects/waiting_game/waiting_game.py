import random
import time
from getkey import key, getkey


def waiting_game():
    seconds = random.randint(1, 10)
    print(f"You goal is to wait for {seconds} seconds")
    print(
        f"Press ENTER to start and ENTER again to stop after {seconds} seconds of waiting"
    )

    start = getkey()

    if start == key.ENTER:
        print("Be patient...")
        start_time = time.time()

    if getkey() == key.ENTER:
        print("You're done!")
        end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time is: {elapsed_time:.2f} seconds")

    if round(elapsed_time, 2) == 0:
        print("You smashed it!")
    elif elapsed_time < seconds:
        print(f"You were {(seconds - elapsed_time):.2f} seconds too fast")
    else:
        print(f"You were {(elapsed_time - seconds):.2f} seconds too slow")


def main():
    waiting_game()


if __name__ == "__main__":
    main()
