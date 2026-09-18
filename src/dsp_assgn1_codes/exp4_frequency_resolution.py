import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fs = 1000.0  # Sampling rate: 1000 Hz
f1, f2 = 120.0, 124.0  # Component separation = 4 Hz

# Configuration A & B: Short record (T_obs = 0.1 s -> Delta_f = 10 Hz)
N_short = 100
t_short = np.arange(N_short) / fs
x_short = np.cos(2 * np.pi * f1 * t_short) + np.cos(2 * np.pi * f2 * t_short)

# Zero-padded FFT
N_pad = 1024
X_padded = np.abs(np.fft.fft(x_short, n=N_pad))[: N_pad // 2] / (N_short / 2)
f_padded = np.fft.fftfreq(N_pad, d=1 / fs)[: N_pad // 2]

# Configuration C: Extended record (T_obs = 0.5 s -> Delta_f = 2 Hz)
N_long = 500
t_long = np.arange(N_long) / fs
x_long = np.cos(2 * np.pi * f1 * t_long) + np.cos(2 * np.pi * f2 * t_long)
X_long = np.abs(np.fft.fft(x_long, n=N_pad))[: N_pad // 2] / (N_long / 2)

# Plotting
fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=300)

ax.plot(
    f_padded,
    X_padded,
    'r--',
    lw=1.5,
    label='Short Window ($T_{\\mathrm{obs}}=0.1\\,\\mathrm{s}$, Padded to 1024)',
)
ax.plot(
    f_padded,
    X_long,
    'b-',
    lw=1.5,
    label='Long Window ($T_{\\mathrm{obs}}=0.5\\,\\mathrm{s}$, True Resolution)',
)

ax.axvline(120.0, color='gray', linestyle=':', alpha=0.6)
ax.axvline(124.0, color='gray', linestyle=':', alpha=0.6)
ax.set_xlim(100, 145)
ax.set_ylim(0, 2.0)
ax.set_title(
    'Experiment 4: Rayleigh Resolution vs. Zero-Padding Interpolation',
    fontsize=11,
)
ax.set_xlabel('Frequency (Hz)', fontsize=10)
ax.set_ylabel('Normalized Amplitude', fontsize=10)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('images/exp4_frequency_resolution.png', dpi=300)
plt.close()
print('Successfully generated images/exp4_frequency_resolution.png')