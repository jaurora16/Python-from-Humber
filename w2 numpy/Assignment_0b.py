import numpy as np
def add_arrays(a, b):
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
# Define new arrays
a2 = np.array([9, 8, 7, 6])
b2 = np.array([[6, 7], [8, 9]])
# Execute the function with new arrays
add_arrays(a2, b2)
