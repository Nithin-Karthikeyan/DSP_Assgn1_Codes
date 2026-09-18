import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

N = 128
# 1. Temporally localized rectangular boxcar pulse
x = np.zeros(N)
x[48:80] = 1.0

# 2. Forward FFT
X = np.fft.fft(x)
mag = np.abs(X)
phase = np.angle(X)

# Condition A: Zero-phase spectrum
X_zero_phase = mag * np.exp(1j * 0.0)

# Condition B: Randomized phase spectrum (preserving Hermitian conjugate symmetry)
np.random.seed(42)
rand_phase = np.random.uniform(-np.pi, np.pi, N // 2 - 1)
scrambled_phase = np.zeros(N)
scrambled_phase[1 : N // 2] = rand_phase
scrambled_phase[N // 2 + 1 :] = -rand_phase[::-1]
X_scrambled = mag * np.exp(1j * scrambled_phase)

# 3. Waveform reconstruction via IDFT
x_true = np.real(np.fft.ifft(X))
x_zero = np.real(np.fft.ifft(X_zero_phase))
x_rand = np.real(np.fft.ifft(X_scrambled))

# Plotting
fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=300)

ax.plot(
    x_true,
    'b-',
    lw=1.8,
    label='Original Isolated Pulse (Active 48 <= n < 80)',
)
ax.plot(
    x_zero,
    'r--',
    lw=1.3,
    label='Zero-Phase Reconstruction (Symmetric at $n=0$)',
)
ax.plot(
    x_rand,
    'g:',
    lw=1.3,
    label='Random-Phase Reconstruction (Coherence Destroyed)',
)

ax.set_title(
    'Experiment 5: The Critical Role of Phase in Waveform Synthesis',
    fontsize=11,
)
ax.set_xlabel('Sample Index $n$', fontsize=10)
ax.set_ylabel('Amplitude', fontsize=10)
ax.set_xlim(0, 130)
ax.set_ylim(-0.4, 2.5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('images/exp5_phase_scrambling.png', dpi=300)
plt.close()
print('Successfully generated images/exp5_phase_scrambling.png')