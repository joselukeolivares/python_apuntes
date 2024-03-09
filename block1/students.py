names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Introduces assginaments separated by commas").split(',')
grades =  input("Introduces grades  by commas").split(',')

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name,assignament,grade in zip(names,assignments,grades):
    print(message.format(name,assignament,grade,int(grade)+int(assignament)*2))