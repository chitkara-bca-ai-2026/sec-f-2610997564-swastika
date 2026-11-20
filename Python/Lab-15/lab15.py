# Lab 15 - Student Information Management System

students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },

    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },

    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

while True:
    print("========================================")
    print("  STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("========================================")

    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("--- Enrolled Student Records ---")

        for roll, student in students.items():
            print("Roll No:", roll,
                  "| Name:", student["Name"],
                  "| Branch:", student["Branch"],
                  "| Semester:", student["Semester"],
                  "| Marks:", student["Marks"])

        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")

        student = students.get(roll)

        if student is not None:
            print("\n[FOUND] Student Record")
            print("Name:", student["Name"])
            print("Branch:", student["Branch"])
            print("Semester:", student["Semester"])
            print("Marks:", student["Marks"])
        else:
            print("[ERROR] Student record not found.")

    elif choice == "3":
        print("--- Register New Student ---")

        roll = input("Enter Roll Number: ")

        if roll in students:
            print("[ERROR] Roll Number already exists.")

        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            semester = input("Enter Semester: ")

            marks = []

            for i in range(3):
                mark = int(input("Enter marks for Subject " + str(i + 1) + ": "))
                marks.append(mark)

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }

            print("[SUCCESS] Student registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            print("1. Update Branch")
            print("2. Update Semester")

            update_choice = input("Choose field to update (1 or 2): ")

            if update_choice == "1":
                branch = input("Enter new branch: ")
                students[roll]["Branch"] = branch

                print("[SUCCESS] Branch updated.")

            elif update_choice == "2":
                semester = input("Enter new semester: ")
                students[roll]["Semester"] = semester

                print("[SUCCESS] Semester updated.")

            else:
                print("Invalid update choice.")

        else:
            print("[ERROR] Student record not found.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")

        if roll in students:
            student = students[roll]
            marks = student["Marks"]

            total = sum(marks)
            average = total / len(marks)

            print("========== ACADEMIC REPORT ==========")
            print("Student Name:", student["Name"])
            print("Roll Number:", roll)
            print("Subject Marks:", marks)
            print("Total Marks:", total, "/", len(marks) * 100)
            print("Average Percentage:", round(average, 2), "%")

            if average >= 40:
                print("Final Result: PASS")
            else:
                print("Final Result: FAIL")

            print("=====================================")

        else:
            print("[ERROR] Student record not found.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")

        student = students.pop(roll, None)

        if student is not None:
            print("[SUCCESS] Record for", student["Name"], "deleted successfully.")
        else:
            print("[ERROR] Student record not found.")

    elif choice == "7":
        print("Thank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 7.")