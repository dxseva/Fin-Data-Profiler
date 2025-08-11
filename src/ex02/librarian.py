#!/usr/bin/env python3
import sys
import os
import subprocess
import shutil

# Expected virtual environment path (confirmed by ls -ld)
EXPECTED_VENV = os.path.normpath('VIRTUAL_ENV')


def check_virtual_env():
    """Check if the script is running in the correct virtual environment."""
    current_venv = os.environ.get("VIRTUAL_ENV")
    if not current_venv:
        raise EnvironmentError("No virtual environment is active.")
    current_venv = os.path.normpath(current_venv)
    if current_venv != EXPECTED_VENV:
        raise EnvironmentError(f"Wrong virtual environment. Expected: {EXPECTED_VENV}, Got: {current_venv}")
    return True

def install_libraries():
    """Create requirements.txt and install beautifulsoup4 and pytest."""
    with open("requirements.txt", "w") as file:
        file.write("beautifulsoup4\npytest\n")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error installing libraries: {e.stderr}")
        sys.exit(1)

def list_installed_libraries():
    """List all installed libraries with their versions."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=freeze"],
            check=True,
            capture_output=True,
            text=True
        )
        libraries = result.stdout.strip().split("\n")
        for lib in libraries:
            print(lib)
        return libraries
    except subprocess.CalledProcessError as e:
        print(f"Error listing libraries: {e.stderr}")
        sys.exit(1)

def save_requirements():
    """Save installed libraries to requirements.txt."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            check=True,
            capture_output=True,
            text=True
        )
        with open("requirements.txt", "w") as file:
            file.write(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error saving requirements: {e.stderr}")
        sys.exit(1)
    except OSError as e:
        print(f"Error writing to requirements.txt: {e}")
        sys.exit(1)

def archive_virtual_env():
    """Archive the virtual environment to ex02/lomasdar.tar.gz."""
    venv_name = os.path.basename(EXPECTED_VENV)
    archive_path = os.path.join("archive", f"{venv_name}.tar.gz")
    try:
        os.makedirs("archive", exist_ok=True)
        shutil.make_archive(
            os.path.join("ex02", venv_name),
            "gztar",
            root_dir=os.path.dirname(EXPECTED_VENV),
            base_dir=venv_name
        )
        print(f"Virtual environment archived to {archive_path}")
    except Exception as e:
        print(f"Error archiving virtual environment: {e}")
        sys.exit(1)

def main():
    try:
        check_virtual_env()
        install_libraries()
        print("Installed libraries:")
        list_installed_libraries()
        save_requirements()
        archive_virtual_env()
    except EnvironmentError as e:
        print(f"Environment error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()