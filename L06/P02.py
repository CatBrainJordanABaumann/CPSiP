grades = [95, 88, 85, 75]
letter_grades = ['A', 'B+', 'B', 'C']
print('The original list ', letter_grades)
print('The zipped tuples ', list(zip(letter_grades, grades)))
print('Next is a map-lambda version')
print(list(map(lambda *a: a, letter_grades, grades)))