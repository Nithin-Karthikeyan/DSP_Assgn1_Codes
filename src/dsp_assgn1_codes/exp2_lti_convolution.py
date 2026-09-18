import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 1. Define Input x[n]: length Lx = 10
Lx = 10
x = np.ones(Lx)

# 2. Define Impulse Response h[n]: length Lh = 15
Lh = 15
n_h = np.arange(Lh)
h = (0.8) ** n_h

# 3. Discrete Linear Convolution
y = np.convolve(x, h)
n_y = np.arange(len(y))

# Plotting
fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=300)

markerline, stemlines, baseline = ax.stem(
    n_y,
    y,
    linefmt='b-',
    markerfmt='bo',
    basefmt='k-',
    label='Output $y[n] = x[n] * h[n]$',
)
plt.setp(stemlines, linewidth=1.5)
plt.setp(markerline, markersize=5)

# Highlight transient rise vs decaying tail
ax.axvline(
    9.5,
    color='red',
    linestyle='--',
    alpha=0.7,
    label='Input Shuts Off ($n=10$)',
)
ax.text(
    4.5,
    2.5,
    'Transient Rise\n(0 <= n <= 9)',
    color='blue',
    ha='center',
    fontsize=9,
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
)
ax.text(
    16.5,
    2.0,
    'Discharge Tail\n(10 <= n <= 23)',
    color='darkgreen',
    ha='center',
    fontsize=9,
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
)

ax.set_title(
    'Experiment 2: LTI System Response via Discrete Linear Convolution',
    fontsize=11,
)
ax.set_xlabel('Sample Index $n$', fontsize=10)
ax.set_ylabel('Amplitude', fontsize=10)
ax.set_xticks(np.arange(0, 25, 2))
ax.set_ylim(0, 5.2)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('images/exp2_lti_convolution.png', dpi=300)
plt.close()
print('Successfully generated images/exp2_lti_convolution.png')