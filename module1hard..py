grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
for i in range(len(grades)):
    GPA = round(sum(grades[i])/len(grades[i]),1)
    grades[i] = GPA
grade_book = dict(zip(students, grades))
print(grade_book)