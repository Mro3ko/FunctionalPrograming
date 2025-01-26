grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]

valid_grades = list(filter(lambda grade: grade != 2.0, grades))
mean = sum(valid_grades) / len(valid_grades)
print(f"Arithmetic mean for grades <> 2.0 is {round(mean,2)}")