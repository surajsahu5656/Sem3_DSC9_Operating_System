""" Write a program to calculate sum of n numbers using thread library."""

import threading

# Function to calculate sum of a sublist
def calculate_sum(sublist, result, index):
    result[index] = sum(sublist)

def main():
    # Input list of numbers and number of threads
    numbers = list(range(1, 101)) # Example list of numbers from 1 to 100
    n_threads = 4

    # Calculate the size of each sublist
    sublist_size = len(numbers) // n_threads

    # Create result list to store sum of each sublist
    result = [0] * n_threads
    threads = []

    # Create threads
    for i in range(n_threads):
        start_index = i * sublist_size
        # If it's the last thread, include the remaining elements
        end_index = None if i == n_threads - 1 else (i + 1) * sublist_size
        thread = threading.Thread(target=calculate_sum, args=(numbers[start_index:end_index], result, i))
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Calculate the total sum
    total_sum = sum(result)
    print(f"Sum of numbers: {total_sum}")

if __name__ == "__main__":
    main()
