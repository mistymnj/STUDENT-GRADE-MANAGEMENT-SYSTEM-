
def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Main program
marks = []

for i in range(1, 6):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

average = calculate_average(marks)
grade = get_grade(average)

print("\n--- Student Grade Report ---")
print(f"Average Marks: {average:.1f}")
print(f"Grade: {grade}")
