students = {}

while True:
   print("\n1 - Add student")
   print("2 - Add grade")
   print("3 - Show average")
   print("4 - Show all students")
   print("5 - Exit")
   try:
    choice = input("Please choice a number: ")
   except:
      print("Please enter a number!")
      continue

   if choice == "1":
      name_of_student = input("student name: ")
      if name_of_student in students:
         print("Student already exists!")
      else:
          students[name_of_student] = []
          print("Student added.")

   elif choice == "2":
      name_of_student = input("student name: ")
      if name_of_student not in students:
         print("Student not found!")
      else:
         try:
          grade = float(input("Grade: "))
          students[name_of_student].append(grade)
         except:
            print("Please enter a number!")

   elif choice == "3":
      name_of_student = input("student name: ")
      if name_of_student not in students or len(students[name_of_student]) == 0:
         print("No grades found!")
      else:
         avg = sum(students[name_of_student]) / len(students[name_of_student])
         print("Average:", avg)

   elif choice == "4":
      for name, grade in students.items():
         print(name, ":", ", ".join(map(str, grade)))

   elif choice == "5":
      print("Have a good time🧡")
      break
   else:
      print("Invalid choice!")