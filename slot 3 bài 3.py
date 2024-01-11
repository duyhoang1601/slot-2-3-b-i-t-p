
#BÀI 3
def find_unique_numbers(arr):
    unique_numbers = []
    for num in arr:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Input array from the user
input_str = input("Enter the values of the array separated by spaces: ")
input_list = list(map(int, input_str.split()))

# Find and display the unique numbers
unique_numbers = find_unique_numbers(input_list)
output_str = ' '.join(map(str, unique_numbers))

print(f"Input: {input_str}")
print(f"Output: {output_str}")