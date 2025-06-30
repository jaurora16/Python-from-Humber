# First Name: Jessica
# Last Name: Aurora
import numpy as np
speeds = np.array([29,18.8,21,19.5,13.7,13.5,27.4,17.7,14.3,22.4,23.3,24.1,12.2,29.8,18.8,19.5,16.4,13.9,17.2,23.8,29.9,17.6,12.1,20.1,24.7,17.7,27.4,24.7,22.9,29.8])
def get_mean(speeds):
    return np.mean(speeds)
#prints the mean value of x
print('The mean speeds is:', get_mean(speeds))
speeds2 = np.array([22,22.1,14.6,19.1,12.2,21.3,21.3,20.3,12.4,22.8,12.9,15.7,23,15.5,19.3])
def get_mean(speeds2):
    return np.mean(speeds2)
print('The mean of the data speeds is:', get_mean(speeds2))
