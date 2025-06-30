# First Name: Jessica
# Last Name: Aurora
import numpy as np
import math
speeds = np.array([
    17.8, 23.1, 14.4, 15.8, 25.3, 24.7, 22.7, 17.3, 27.4, 16.3,
    20.6, 19.2, 28.2, 17.4, 15.4, 28.0, 21.7, 24.4, 23.4, 15.2,
    18.2, 29.5, 19.8, 17.2, 13.5, 29.7, 25.3, 15.0, 12.4, 23.1
])
def get_var_dev(data):
    """
    Calculates sample variance:
      s² = Σ((xi − x̄)²) / (n − 1)
    """
    n = len(data)
    if n < 2:
        raise ValueError("At least two data points are required")
    mean = np.mean(data)
    sq_devs = [(x - mean) ** 2 for x in data]
    return sum(sq_devs) / (n - 1)
speeds2 = np.array([23,27.9,29.5,22.9,23.4,12.7,23.4,21.5,28.8,23.2,21,12.8,26.6,25.1,13])
# Compute variance and standard deviation
variance = get_var_dev(speeds)
std_speeds = math.sqrt(variance)
print('The variance and standard deviation of the first data set is:', get_var_dev(speeds))
# Compute variance and standard deviation of speeds2
variance = get_var_dev(speeds2)
std_speeds2 = math.sqrt(variance)
print('The variance and standard deviation of the second data set is:', get_var_dev(speeds2))
