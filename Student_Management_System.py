students = []
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. View students")
    print("3. Calculate average score")
    print("4. Exit")

    choice = input("Choose an option: ")
    print("You chose:", choice)

    if choice == "1":
        # Add a student
        name = input("Enter student's name:")
        score = float(input("Enter student's score:"))
    
        student = {"name": name,"score": score}
        students.append(student)
        
        print('Student added successfully!')
    
    elif choice == '2':
        # View students
        print("\n===== STUDENTS =====")
        if len(students) == 0:
            print("No students have been added yet.")
        else:
            print(students)
            
    elif choice == "3":
        # Calculate average score
        if len(students) == 0:
            print("No students have been added yet.")
        else:
            total_score = 0

            for student in students:
                total_score = total_score + student["score"]

            number_of_students = len(students)
            average = total_score / number_of_students

            print("Average score:", average)

    
    elif choice == '4':
        #Exit
        print('Goodbye')
        break
    
    else:
        print('Invalid input. Please choose 1,2,3, or 4.')
    