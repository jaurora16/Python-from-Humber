# First Name: Jessica
# Last Name: Aurora
import numpy as np
#prompt user to enter the course weights as a percentage
print('Enter the course weights as a percentage (without the percent sign) for each category below:')
tests_weight = float(input("Enter the tests category weight: "))
# prompt the user for each category weight and convert to float
labs_weight = float(input("Enter the labs category weight: "))
assignments_weight = float(input("Enter the assignments category weight: "))
final_exam_weight = float(input("Enter the final exam category weight: "))
#step 4
weights = np.array([tests_weight, labs_weight, assignments_weight, final_exam_weight], dtype=float)
#step 5 prompt
print('Enter student grades as a percentage (without the percent sign) for each category below:')
#step 6 and 7
tests = float(input("Enter the tests grade: "))
labs = float(input("Enter the labs grade: "))
assignments = float(input("Enter the assignments grade: "))
final_exam = float (input("Enter the assignments grade: "))
#step 8
grades = np.array([tests, labs, assignments, final_exam], dtype=float)
#step 9
weighted_avg = np.average(grades, weights=weights)
print("The weighted average is:", weighted_avg)
