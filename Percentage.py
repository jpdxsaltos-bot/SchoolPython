total_marks = input("Enter total marks: ")
obtained_marks = input("Enter obtained marks: ")

total_marks = float(total_marks)
obtained_marks = float(obtained_marks)

percentage = (obtained_marks / total_marks) * 100

int_percentage = int(percentage)

print("Percentage with decimal:", percentage, "%")
print("Percentage as integer:", int_percentage, "%")
