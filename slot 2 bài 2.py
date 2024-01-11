#BÀI 2
def convert_to_alphabetic_grade(decimal_grade):
    if 90 <= decimal_grade <= 100:
        return 'A'
    elif 80 <= decimal_grade < 90:
        return 'B'
    elif 70 <= decimal_grade < 80:
        return 'C'
    elif 60 <= decimal_grade < 70:
        return 'D'
    elif 0 <= decimal_grade < 60:
        return 'F'
    else:
        return 'Invalid input'

def convert_to_4th_system(decimal_grade):
    if 90 <= decimal_grade <= 100:
        return '4.0'
    elif 80 <= decimal_grade < 90:
        return '3.0'
    elif 70 <= decimal_grade < 80:
        return '2.0'
    elif 60 <= decimal_grade < 70:
        return '1.0'
    elif 0 <= decimal_grade < 60:
        return '0.0'
    else:
        return 'Invalid input'

# Input grade from the user
while True:
    try:
        decimal_grade = float(input("Enter the grade in decimal system (0-100): "))
        if 0 <= decimal_grade <= 100:
            break
        else:
            print("Invalid input. Please enter a grade between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")

# Convert and print the grade in alphabetic and 4th system
alphabetic_grade = convert_to_alphabetic_grade(decimal_grade)
fourth_system_grade = convert_to_4th_system(decimal_grade)

print(f"The corresponding alphabetic grade is: {alphabetic_grade}")
print(f"The corresponding 4th system grade is: {fourth_system_grade}")


