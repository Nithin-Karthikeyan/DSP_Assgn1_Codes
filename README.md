# ED5017: Digital Signal Processing for Engineering Design
## Computational Demonstrations & Numerical Experiments Suite

This repository contains the complete Python implementation suite for the computational experiments of **Assignment 1: Understanding DSP — from Signals to Fourier Transform and DFT**. 

Every experiment follows the scientific hypothesis validation framework[cite: 5]:
**Prediction** $\longrightarrow$ **Simulation** $\longrightarrow$ **Observation** $\longrightarrow$ **Explanation**

---

## Repository Structure

```text
DSP_Assgn1_Codes/
├── images/
│   ├── exp1_signal_operations.png
│   ├── exp2_lti_convolution.png
│   ├── exp3_spectral_leakage.png
│   ├── exp4_frequency_resolution.png
│   └── exp5_phase_scrambling.png
├── src/
│   └── dsp_assgn1_codes/
│       ├── __init__.py
│       ├── exp1_signal_ops.py
│       ├── exp2_lti_convolution.py
│       ├── exp3_spectral_leakage.py
│       ├── exp4_frequency_resolution.py
│       └── exp5_phase_scrambling.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock


## Setup & Environment Installation

We recommend using an isolated virtual environment (`venv`) to run these scripts and manage dependencies like `numpy` and `matplotlib`.

### Option 1: Fast Setup Using `uv` (Recommended)

[`uv`](https://github.com/astral-sh/uv) acts as a fast Python package manager. It will automatically create a `.venv` folder and sync all required dependencies.

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/DSP_Assgn1_Codes.git
cd DSP_Assgn1_Codes
```

2. **Sync dependencies (auto-creates venv):**

```bash
uv sync
```

### Option 2: Setup Using Standard `pip` and `venv`

If you prefer standard Python tools, manually create a virtual environment first.

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/DSP_Assgn1_Codes.git
cd DSP_Assgn1_Codes
```

2. **Create and activate the virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

3. **Install the required scientific packages:**

```bash
pip install numpy scipy matplotlib
```

## Running the Experiments

All scripts are configured to use Matplotlib's headless backend (`matplotlib.use('Agg')`).

They run silently without launching GUI windows and save their outputs directly to the `images/` directory.

To execute all five experiments simultaneously in parallel, run the orchestration script.

### Using `uv`

```bash
uv run python src/dsp_assgn1_codes/__init__.py
```

### Using a Standard Activated `venv`

```bash
python src/dsp_assgn1_codes/__init__.py
```
