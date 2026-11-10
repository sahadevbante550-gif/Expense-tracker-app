"""
Number Analyzer and Sorting System
Finds largest/smallest values and sorts numbers without sorted() or sort().
"""

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest


def bubble_sort(numbers, descending=False):
    result = numbers.copy()
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            should_swap = (
                result[j] < result[j + 1]
                if descending
                else result[j] > result[j + 1]
            )
            if should_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


def find_second_largest(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    if len(unique_numbers) < 2:
        return None

    ordered = bubble_sort(unique_numbers, descending=True)
    return ordered[1]


def main():
    print("=" * 45)
    print("       NUMBER ANALYZER & SORTING SYSTEM")
    print("=" * 45)

    raw_input = input("Enter numbers separated by spaces: ").strip()

    try:
        numbers = [float(value) for value in raw_input.split()]
        if not numbers:
            print("Please enter at least one number.")
            return
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print("\nOriginal numbers :", numbers)
    print("Largest number   :", find_largest(numbers))
    print("Smallest number  :", find_smallest(numbers))

    second = find_second_largest(numbers)
    print("Second largest   :", second if second is not None else "Not available")

    print("Ascending order  :", bubble_sort(numbers))
    print("Descending order :", bubble_sort(numbers, descending=True))


if __name__ == "__main__":
    main()
