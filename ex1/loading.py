import importlib

REQUIRED = ["pandas", "requests", "matplotlib"]


def version_of(name_of_package):
    try:
        pkg = importlib.import_module(name_of_package)
        ver = getattr(pkg, "__version__", "unknown")
        return str(ver)
    except Exception:
        return "missing"


def missing_packages():
    missing = []
    for name in REQUIRED:
        try:
            importlib.import_module(name)
        except Exception:
            missing.append(name)
    return missing


def print_missing(missing):
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    for name in missing:
        print(f"[MISSING] {name}")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("Install with Poetry:")
    print("poetry install")
    print("poetry run python3 loading.py")


def run_analysis():

    import pandas as pd
    import requests
    import matplotlib.pyplot as plt

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    print(f"[OK] pandas ({version_of('pandas')}) - Data manipulation ready")
    print(f"[OK] requests ({version_of('requests')}) - Network access ready")
    print(f"[OK] matplotlib ({version_of('matplotlib')}) - Visualiation ready")

    fetched_size = 0
    try:
        r = requests.get("https://example.com/", timeout=5)
        fetched_size = len(r.text)
    except Exception:
        fetched_size = 0

    print("Analyzing Matrix data...")

    n = 1000
    index_list = []
    value_list = []

    base = fetched_size % 50

    i = 0
    while i < n:
        index_list.append(i)
        value_list.append((i % 100) + base)
        i += 1

    df = pd.DataFrame({"index": index_list, "value": value_list})

    print(f"Processing {n} data points...")
    print("Generating visualization...")

    plt.figure()
    plt.plot(df["index"], df["value"])
    plt.title("Matrix data (simulated)")
    plt.xlabel("index")
    plt.ylabel("value")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    missing = missing_packages()
    if missing:
        print_missing(missing)
        return
    run_analysis()


if __name__ == "__main__":
    main()
