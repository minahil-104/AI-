#Q:9 Total Marks, Percentage, and Average Calculator

def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / (len(marks) * 100)) * 100
    return total, percentage, average

# Taking marks input from user
marks = []
for i in range(1, 6):
    mark = float(input("Enter marks for subject (out of 100): "))
    marks.append(mark)

# Calculating results
total, percentage, average = calculate_results(marks)

# Displaying the results
print("\nTotal Marks:/500",total)
print("Percentage:%",percentage)
print("Average Marks:",average)
