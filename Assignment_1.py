# First Name: Jessica
# Last Name: Aurora
def get_array_sums(arr1, arr2):
    #Returns the element-wise sum of two arrays.
    return [x + y for x, y in zip(arr1, arr2)]
# Define the arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
# Calculate the element-wise sums
result = get_array_sums(arr1, arr2)
# Print the result
print(f"The sum of the arrays is: {sum(result)}")
#check50 mycode-cloud/predictive/main/1_python_basics/Assignment_1.py
#submit50 mycode-cloud/predictive/main/1_python_basics/Assignment_1.py
