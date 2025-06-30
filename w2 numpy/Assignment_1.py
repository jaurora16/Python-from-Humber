# First Name: Jessica
# Last Name: Aurora
import numpy as np
def subarray_ops(a, b):
    """
    Perform various operations on subarrays of two 3x4 numpy arrays.
    Parameters:
    a (numpy.ndarray): First 3x4 array.
    b (numpy.ndarray): Second 3x4 array.
    """
 # Step 5: Print the subarray of 'a' with shape (2, 2) from the first 2 rows and columns
    print("Upper left subarray of first array is:")
    print(a[:2, :2])
    print()
# Step 6: Print the subarray of 'b' with shape (2, 2) from the last 2 rows and columns
    print("Lower right subarray of second array is:")
    print(b[1:, 2:])
    print()
 # Step 7: Subtract the subarray of 'b' from the subarray of 'a' and print the result
    print("The result of subtracting second subarray from first subarray is:")
    print(a[:2, :2] - b[1:, 2:])
    print()
# Step 8: Perform elementwise multiplication of the subarrays and print the result
    print("The result of elementwise multiplication of subarrays is:")
    print(a[:2, :2] * b[1:, 2:])
    print()
# Step 9: Perform elementwise division of the subarrays and print the result
    print("The result of elementwise division of subarrays is:")
    print(a[:2, :2] / b[1:, 2:])
    print()
# Step 10: Add all elements of the subarrays together and print the scalar result
    print("The result of adding all elements from subarrays is:")
    print(np.sum(a[:2, :2]) + np.sum(b[1:, 2:]))
    print()
# Example usage:
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
b = np.array([[21, 22, 23, 24],
              [25, 26, 27, 28],
              [29, 30, 31, 32]])
c = np.array([[11,21,31,41],
              [51,61,71,81],
              [91,101,111,121]])
d = np.array([[221,222,223,224],
              [225,226,227,228],
              [229,230,231,232]])
subarray_ops(a, b)
