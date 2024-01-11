#BÀI 1
def find_nearest_to_average(arr):
    # Calculate the average of the array
    average = sum(arr) / len(arr)

    # Find the element closest to the average
    closest_element = min(arr, key=lambda x: abs(x - average))

    # Find the position of the closest element
    position = arr.index(closest_element)

    return position

# Input array from the user
n = int(input("Enter the number of elements in the array: "))
array = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

# Find and display the position of the element closest to the average
result = find_nearest_to_average(array)
print(f"The position of the element closest to the average is: {result + 1}")

