import subprocess
import sys
from pathlib import Path

src_dir = (Path(__file__).parent.parent.parent / "src").resolve()

py_files = [
    src_dir / "settings.py",
    # add relevent pyfiles in order
]


def main():
    for py_file in py_files:
        result = subprocess.run([sys.executable, str(py_file)], capture_output=True)
        if result.returncode != 0:
            print(f"Error in {py_file}:\n{result.stderr.decode()}")
            sys.exit(1)
        else:
            print(f"{py_file} ran successfully.")


if __name__ == "__main__":
    main()
