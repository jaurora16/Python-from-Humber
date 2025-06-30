# First Name: Jessica
# Last Name: Aurora
import numpy as np
def add_arrays():
    # Initialize arrays
    a = np.array([1, 2, 3, 4])
    b = np.array([[4, 3], [2, 1]])
    # Print the shape and dtype of 'a'
    print(f"The shape of 'a' is {a.shape}")
    print(f"The dtype of 'a' is {a.dtype}")
    # Print the shape and dtype of 'b'
    print(f"The shape of 'b' is {b.shape}")
    print(f"The dtype of 'b' is {b.dtype}")
    # Reshape 'a' to (2, 2)
    c = a.reshape(2, 2)
    print("\nReshaped 'a' is:")
    print(c)
    # Add 'b' and 'c' if shapes are compatible
    if b.shape == c.shape:
        result = b + c
        print("\nReshaped 'a' added to 'b' is:")
        print(result)
    else:
        print("\nShapes of 'b' and reshaped 'a' are not compatible for addition.")
# Execute the function
add_arrays()
