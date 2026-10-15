students = {}

while True:
    student_id = input("학번 입력: ")
    if student_id == "0" or student_id.lower() == "quit":
        break

    name = input("이름 입력: ")
    if name.lower() == "none" or name.lower() == "quit":
        break

    students[student_id] = name

print("학생 명단:", students)

while True:
    search_id = input("조회할 학번 입력 (종료는 quit): ")
    if search_id.lower() == "quit":
        break

    if search_id in students:
        print(students[search_id])
    else:
        print("not found!")