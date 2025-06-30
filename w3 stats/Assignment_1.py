# First Name: Jessica
# Last Name: Aurora
import numpy as np
speeds = np.array([27.4,13.6,29.2,14.4,18.4,20.1,13.3,16.2,12.5,12.5,16.8,25.8,17.8,26.9,22,20.1,14.7,28.3,30,22.2,19.2,21.8,15.9,24.3,22.5,22.9,17.1,28.2,29,25.9])
def get_median(speeds):
    return np.median(speeds)
print('The median of the data speeds is:', get_median(speeds))
speeds2 = np.array([27.8,25.4,29.4,12.1,15.9,23.4,13,27.2,17.3,25.1,21.1,23.9,19.3,21.7,29.1])
def get_median(speeds2):
    return np.median(speeds2)
print('The median of the data speeds is:', get_median(speeds2))
