# First Name: Jessica
# Last Name: Aurora
import numpy as np
from statistics import multimode
clicks = np.array([
        283,130,150,146,134,197,252,204,231,210,262,267,127,184,288,
        159,175,244,129,180,254,283,206,141,269,250,119,283,222,279])
def get_quants(arr: np.ndarray) -> np.ndarray:
    """
    Returns the 25th, 50th, 75th, 95th percentiles and the mode(s).

    Uses numpy.percentile with linear interpolation (default),
    and statistics.multimode for the mode(s).

    Output format: numpy array of size 5:
      [p25, p50, p75, p95, mode]
    If multiple modes, 'mode' is the smallest one returned by multimode().
    """
    # Ensure input is a NumPy array
    a = np.asarray(arr)
    # Calculate percentiles (linear interpolation is the default method)
    p25, p50, p75, p95 = np.percentile(a, [25, 50, 75, 95], method='linear')
    # Get all modal values
    modes = multimode(a.tolist())
    # Choose first mode (or smallest, depending on your preference)
    mode = modes[0] if modes else np.nan
    # Return in the default NumPy format: a 1D numpy.ndarray of floats
    return np.array([p25, p50, p75, p95, mode])
print('The 25th percentile of the click data is: ', get_quants(clicks)[0])
print('The 50th percentile of the click data is: ', get_quants(clicks)[1])
print('The 75th percentile of the click data is: ', get_quants(clicks)[2])
print('The 95th percentile of the click data is: ', get_quants(clicks)[3])
print('The mode of the click data is: ', get_quants(clicks)[4])
#second data set
clicks2 = np.array([132,154,200,115,133,126,149,236,237,275,140,200,192,271,154])
#print statements for second set of data
print('The 25th percentile of the click data is: ', get_quants(clicks2)[0])
print('The 50th percentile of the click data is: ', get_quants(clicks2)[1])
print('The 75th percentile of the click data is: ', get_quants(clicks2)[2])
print('The 95th percentile of the click data is: ', get_quants(clicks2)[3])
print('The mode of the click data is: ', get_quants(clicks2)[4])

