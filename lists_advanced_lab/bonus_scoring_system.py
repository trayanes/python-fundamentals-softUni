from math import ceil
students_number = int(input())
lectures_number = int(input())
additional_bonus = int(input())

max_bonus = 0
max_bonus_student_att = 0
for student in range(1, students_number+1):
    attendance = int(input())
    total_bonus = attendance / lectures_number * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_bonus_student_att = attendance
max_bonus = ceil(max_bonus)
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_bonus_student_att} lectures.")
