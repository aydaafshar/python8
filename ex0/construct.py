import os
import site
import sys


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def print_site_packages() -> None:
    print("Package installation path:")
    try:
        paths = site.getsitepackages()
        for p in paths:
            print(p)
    except Exception:
        major = sys.version_info.major
        minor = sys.version_info.minor
        path = os.path.join(
            sys.prefix, "lib", f"python{major}.{minor}", "site-packages"
        )
        print(path)


def main() -> None:
    inside = is_in_venv()
    python_path = sys.executable

    if not inside:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print("Current Python: " + python_path)
        print()
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print_site_packages()

        print()

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print()
        print("Then run this program again.")
        return

    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    venv_name = os.path.basename(venv_path.rstrip(os.sep))

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print("Current Python: " + python_path)
    print("Virtual Environment: " + venv_name)
    print("Environment Path: " + venv_path)
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print_site_packages()


if __name__ == "__main__":
    main()
