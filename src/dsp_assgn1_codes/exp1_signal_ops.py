import matplotlib
matplotlib.use('Agg')  # Headless backend (no Tcl/Tk needed)
import matplotlib.pyplot as plt
import numpy as np

# Sample index grid
n = np.arange(-5, 16)

# 1. Base rectangular pulse x[n]: active for n in [0, 4]
x = np.where((n >= 0) & (n <= 4), 1.0, 0.0)

# 2. Transformed signal 1: Delay by 3, scale amplitude by 2.0 -> y1[n] = 2 * x[n - 3]
y1 = np.where(((n - 3) >= 0) & ((n - 3) <= 4), 2.0, 0.0)

# 3. Transformed signal 2: Advance by 2, invert & scale by -1.5 -> y2[n] = -1.5 * x[n + 2]
y2 = np.where(((n + 2) >= 0) & ((n + 2) <= 4), -1.5, 0.0)

# Plotting
fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=300)

markerline1, stemlines1, _ = ax.stem(
    n - 0.15,
    x,
    linefmt='b-',
    markerfmt='bo',
    basefmt='k-',
    label='Base Signal $x[n]$',
)
markerline2, stemlines2, _ = ax.stem(
    n,
    y1,
    linefmt='g--',
    markerfmt='gs',
    basefmt='k-',
    label='Delayed & Scaled $y_1[n] = 2x[n-3]$',
)
markerline3, stemlines3, _ = ax.stem(
    n + 0.15,
    y2,
    linefmt='r:',
    markerfmt='r^',
    basefmt='k-',
    label='Advanced & Inverted $y_2[n] = -1.5x[n+2]$',
)

plt.setp(stemlines1, linewidth=1.5)
plt.setp(stemlines2, linewidth=1.5)
plt.setp(stemlines3, linewidth=1.5)

ax.set_title(
    'Experiment 1: Discrete Signal Operations (Shifting and Amplitude Scaling)',
    fontsize=11,
)
ax.set_xlabel('Sample Index $n$', fontsize=10)
ax.set_ylabel('Amplitude', fontsize=10)
ax.set_xticks(np.arange(-5, 16, 2))
ax.set_ylim(-2.2, 2.8)
ax.axhline(0, color='black', linewidth=0.8)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('images/exp1_signal_operations.png', dpi=300)
plt.close()
print('Successfully generated images/exp1_signal_operations.png')