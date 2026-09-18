import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 1. Setup acquisition parameters
fs = 1000.0  # Sampling frequency (Hz)
N = 128  # Record length (Delta_f = 7.8125 Hz)
t = np.arange(N) / fs  # Duration: 0.128 s

# 2. Synthesize test waveforms
# Tone A: Coherent integer bin (125 Hz / 7.8125 Hz = 16 cycles exactly)
x_coherent = np.cos(2 * np.pi * 125.0 * t)
# Tone B: Non-coherent inter-bin tone (132.8 Hz / 7.8125 Hz = 16.998 cycles)
x_leaked = np.cos(2 * np.pi * 132.8 * t)

# 3. Apply tapered Hann window
w_hann = np.hanning(N)
x_hann = x_leaked * w_hann

# 4. Compute single-sided magnitude spectra in dB
freqs = np.fft.fftfreq(N, 1 / fs)[: N // 2]
X_coh = np.abs(np.fft.fft(x_coherent))[: N // 2] / (N / 2)
X_leak = np.abs(np.fft.fft(x_leaked))[: N // 2] / (N / 2)
X_hann_mag = np.abs(np.fft.fft(x_hann))[: N // 2] / (np.sum(w_hann) / 2)

# Convert to dB relative to peak
X_coh_db = 20 * np.log10(np.maximum(X_coh, 1e-5))
X_leak_db = 20 * np.log10(np.maximum(X_leak, 1e-5))
X_hann_db = 20 * np.log10(np.maximum(X_hann_mag, 1e-5))

# Plotting
fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=300)

ax.plot(
    freqs,
    X_coh_db,
    'b-o',
    markersize=4,
    linewidth=1.5,
    label='125.0 Hz (Coherent, Rectangular)',
)
ax.plot(
    freqs,
    X_leak_db,
    'r--x',
    markersize=4,
    linewidth=1.5,
    label='132.8 Hz (Leaked, Rectangular)',
)
ax.plot(
    freqs,
    X_hann_db,
    'g-.s',
    markersize=4,
    linewidth=1.5,
    label='132.8 Hz (Hann Windowed)',
)

ax.set_title(
    'Experiment 3: Spectral Leakage and Sidelobe Suppression', fontsize=11
)
ax.set_xlabel('Frequency (Hz)', fontsize=10)
ax.set_ylabel('Magnitude (dB)', fontsize=10)
ax.set_ylim(-60, 5)
ax.set_xlim(-10, 510)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('images/exp3_spectral_leakage.png', dpi=300)
plt.close()
print('Successfully generated images/exp3_spectral_leakage.png')