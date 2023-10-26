import time
import random
import matplotlib.pyplot as plt


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def counting_sort(arr):
    return arr


def quick_sort(arr):
    def partition(arr, low, high):
        pass

    return arr


def bubble_sort(arr):
    return arr


def merge_sort(arr):
    def merge(arr, left, mid, right):
        pass

    def merge_sort_helper(arr, left, right):
        pass

    return arr


def radix_sort(arr):
    return arr


#  Test function to verify sorting algorithms
def test_sorting_algorithm(sort_func, n=10):
    # Perform n random test cases
    for _ in range(n):
        length = random.randint(10, 100)
        arr = [random.randint(100, 100_000) for _ in range(length)]
        expected = sorted(arr)
        # Verify that the sorted array matches the expected result
        assert sort_func(arr) == expected

    print("All test cases passed")


test_sorting_algorithm(insertion_sort)
length = 10
random.sample(range(length ** 3), length)


# Function to plot the performance of sorting algorithms
def plot_sorting_performance(algorithms):
    # Define the lengths of arrays for performance testing
    lengths = [100, 500, 1_000, 5_000, 10_000, 15_000, 20_000]
    for algo_name, algo_func in algorithms.items():
        execution_times = []
        for length in lengths:
            arr = random.sample(range(length ** 3), length)
            start_time = time.time()
            algo_func(arr)
            end_time = time.time()
            execution_times.append(end_time - start_time)

        # Plot the execution times for each array length
        plt.plot(lengths, execution_times, label=algo_name)

    plt.xlabel("Array Length")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.show()
