import concurrent.futures
from pathlib import Path
import subprocess
import sys


def run_experiment(script_path: Path, project_root: Path):
    """Executes an experiment script with cwd set to the project root

    so relative saves like 'images/expX_*.png' land cleanly in images/.
    """
    print(f"[RUNNING] {script_path.name}...")
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=True,
        )
        return f"[SUCCESS] {script_path.name}\n{result.stdout.strip()}"
    except subprocess.CalledProcessError as e:
        return f"[ERROR] {script_path.name} failed:\n{e.stderr.strip()}"


def main():
    # Location: DSP_Assgn1_Codes/src/dsp_assgn1_codes/__init__.py
    pkg_dir = Path(__file__).resolve().parent

    # Project root: DSP_Assgn1_Codes/ (two directories up from __init__.py)
    project_root = pkg_dir.parents[1]

    # 1. Ensure project_root/images/ exists
    images_dir = project_root / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    print(f"Project root : {project_root}")
    print(f"Images folder: {images_dir}\n")

    # 2. Map of scripts inside src/dsp_assgn1_codes/ to their generated image targets
    experiments = [
        (pkg_dir / "exp1_signal_ops.py", "exp1_signal_operations.png"),
        (pkg_dir / "exp2_lti_convolution.py", "exp2_lti_convolution.png"),
        (pkg_dir / "exp3_spectral_leakage.py", "exp3_spectral_leakage.png"),
        (
            pkg_dir / "exp4_frequency_resolution.py",
            "exp4_frequency_resolution.png",
        ),
        (pkg_dir / "exp5_phase_scrambling.py", "exp5_phase_scrambling.png"),
    ]

    valid_tasks = []
    for script, expected_img in experiments:
        if script.exists():
            valid_tasks.append((script, expected_img))
        else:
            print(f"[MISSING] Could not find {script.name} in {pkg_dir}")

    # 3. Execute all valid scripts in parallel
    print(f"Executing {len(valid_tasks)} scripts in parallel...\n")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(run_experiment, script, project_root)
            for script, _ in valid_tasks
        ]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    # 4. Verify all expected images were written to images/
    print("\n--- Image Verification ---")
    for _, expected_img in valid_tasks:
        target_path = images_dir / expected_img
        status = "FOUND" if target_path.exists() else "NOT FOUND"
        print(f"[{status}] images/{expected_img}")


if __name__ == "__main__":
    main()