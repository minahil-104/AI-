#Q:14 Percentage of Correct 
def calculate_percentage(correct, total):
    return (correct / total) * 100

# Taking input from user
total_questions = int(input("Enter total number of questions: "))
correct_answers = int(input("Enter number of correct answers: "))

# Validating input
if 0 <= correct_answers <= total_questions and total_questions > 0:
    percentage = calculate_percentage(correct_answers, total_questions)
    print("Your score is:%", percentage)
else:
    print("Invalid input")
