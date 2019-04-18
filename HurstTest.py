import numpy as np
import matplotlib.pyplot as plt
from hurst import compute_Hc, random_walk
import WorkWFiles; import LogMap

# noise parameters
mean = 0; std = 1
num_samples = 1000

# analysed signal ()
series = WorkWFiles.write_to_list('RR.txt')

# Evaluate Hurst equation
H, c, data = compute_Hc(series, kind='price', simplified=True)
print(H, c, data)

# Plot
f, ax = plt.subplots()
ax.plot(data[0], c*data[0]**H, color="deepskyblue")
ax.scatter(data[0], data[1], color="purple")

# plot directives
ax.set_xscale('log'); ax.set_yscale('log')  # scale directives
ax.set_xlabel('Time interval'); ax.set_ylabel('R/S ratio')  # label directives
ax.grid(True); plt.show()

print("H={:.4f}, c={:.4f}".format(H, c))
