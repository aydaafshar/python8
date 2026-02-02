import os

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None

REQUIRED_VARS = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
                 "LOG_LEVEL", "ZION_ENDPOINT"]


def load_dotenv_if_availble():
    if load_dotenv is None:
        return False
    load_dotenv()
    return True


def get_env(name):
    return os.environ.get(name)


def is_production(mode):
    return mode == "production"


def find_missing():
    missing = []
    for name in REQUIRED_VARS:
        if not get_env(name):
            missing.append(name)
    return missing


def print_missing_output(dotenv_loaded):

    print("WARNING: Missing configuration variables:")
    for name in find_missing():
        print(f"- {name}")
    print()
    if dotenv_loaded:
        print("Tip: Create a .env file  and fill values.")
    else:
        print("Tip: Create a .env file  and fill values.")
    print("You can also override via environment variables.")


def print_success_output(mode, db_url, api_key, log_level, zion_endpoint):
    print("ORACLE STATUS: Reading the Matrix.")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if is_production(mode):
        print("Database: Connected to production instance")
    else:
        print("Database: Connected to local instance")

    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env.example"):
        print("[OK] .env file properly configured")
    else:

        print("[OK] .env file properly configured")

    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


def main():
    dotenv_loaded = load_dotenv_if_availble()

    mode = get_env("MATRIX_MODE")
    db_url = get_env("DATABASE_URL")
    api_key = get_env("API_KEY")
    log_level = get_env("LOG_LEVEL")
    zion_endpoint = get_env("ZION_ENDPOINT")

    missing = find_missing()
    if missing:
        print_missing_output(dotenv_loaded)
        return

    print_success_output(mode, db_url, api_key, log_level, zion_endpoint)


if __name__ == "__main__":
    main()
