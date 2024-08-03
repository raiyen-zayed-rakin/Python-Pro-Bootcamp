
student_height = input("Input a list of student heights ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(f"The inputted list: {student_height}, Length: {len(student_height)}")

total_height = 0
for height in student_height:
    total_height += student_height[height-1]

average = round(total_height/len(student_height))
print(f"Average height: {average}")