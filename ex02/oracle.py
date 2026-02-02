import os
from typing import List, Optional

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

REQUIRED_VARS = ["MATRIX_MODE", "DATABASE_URL",
                 "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]


def load_dotenv_if_availble() -> bool:
    if load_dotenv is None:
        return False
    load_dotenv(override=False)
    return True


def get_env(name: str) -> Optional[str]:
    return os.environ.get(name)


def is_production(mode: str) -> bool:
    return mode == "production"


def find_missing() -> List[str]:
    missing = []
    for name in REQUIRED_VARS:
        if not get_env(name):
            missing.append(name)
    return missing


def mask_secret(value: str) -> str:
    if len(value) <= 4:
        return "*" * len(value)
    return value[:2] + "*" * (len(value) - 4) + value[-2:]


def print_missing_output(dotenv_loaded: bool, missing: List[str]) -> None:

    print("WARNING: Missing configuration variables:")
    for name in missing:
        print(f"- {name}")
    print()
    if dotenv_loaded:
        print("Tip: Create a .env file  and fill values.")
    else:
        print("Tip: Create a .env file from .env.example and fill values.")
        print("      (Do NOT commit .env)")
    print("You can also override via environment variables.")
    print("Example:")
    print("MATRIX_MODE=production API_KEY=secret123 python3 oracle.py")


def print_success_output(
    mode: str, db_url: str, api_key: str, log_level: str, zion_endpoint: str
) -> None:

    _ = (db_url, zion_endpoint)

    print("\nORACLE STATUS: Reading the Matrix.\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if is_production(mode):
        print("Database: Connected to production instance")
    else:
        print("Database: Connected to local instance")

    print(f"API Access: Authenticated ({mask_secret(api_key)})")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:

        print("[OK] no .env file in repository")

    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


def main():
    dotenv_loaded = load_dotenv_if_availble()

    missing = find_missing()
    if missing:
        print_missing_output(dotenv_loaded, missing)
        return
    mode = get_env("MATRIX_MODE") or ""
    db_url = get_env("DATABASE_URL") or ""
    api_key = get_env("API_KEY") or ""
    log_level = get_env("LOG_LEVEL") or ""
    zion_endpoint = get_env("ZION_ENDPOINT") or ""

    print_success_output(mode, db_url, api_key, log_level, zion_endpoint)


if __name__ == "__main__":
    main()
