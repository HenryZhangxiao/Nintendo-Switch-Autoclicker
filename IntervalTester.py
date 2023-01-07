import time
start_time = time.time()
keypress_times = []

if __name__ == '__main__':
    while (True):
        _input = input("Waiting for keyboard input...")
        if _input == 'q' or _input == 'Q':
            current_time = time.time()
            elapsed_time = current_time - start_time
            keypress_times.append(elapsed_time)
            print("Elapsed time since last keypress: " + str(elapsed_time))
            running_total = 0
            for timing in keypress_times:
                running_total += timing
            print("The fastest time between keypresses was " + str(min(keypress_times)) + " seconds")
            print("The slowest time between keypresses was " + str(max(keypress_times)) + " seconds")
            print("The average time between keypresses was " + str(running_total/len(keypress_times)) + " seconds")
            exit()
        current_time = time.time()
        elapsed_time = current_time - start_time
        keypress_times.append(elapsed_time)
        start_time = current_time
        print("Elapsed time since last keypress: " + str(elapsed_time))
