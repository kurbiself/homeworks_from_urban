amount_of_homework_done = 12
number_of_hours = 1.5
course_name = 'Python'
time_for_one_homework = number_of_hours / amount_of_homework_done
print('Курс:', course_name + ',', 'всего задач:', str(amount_of_homework_done) + ',',
      'затрачено часов', str(number_of_hours) + ',', 'среднее время выполнения', time_for_one_homework, 'часа')
# другой вариант
print(f'Курс: {course_name}, всего задач: {amount_of_homework_done}, '
      f'затрачено часов {number_of_hours}, среднее время выполнения {time_for_one_homework} часа')
