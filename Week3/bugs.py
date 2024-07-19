# This program has a few bugs
# It should calculate the average of the numbers 1, 2, 3, 4, and 5...

def main():
    num_list = [1, 2, 3, 4, 5]
    print("The numbers are: ", num_list)
    avg = calculate_average(num_list)
    print("The average is: ", avg)

def calculate_average(numbers):
    total = 0
    for i in range(0, 4):
        total += numbers[i]

    average = total / len(numbers)

    return average

if __name__ == "__main__":
    main()
