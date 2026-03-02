import os
import time


def main():
    duration = 120  # seconds
    interval = 10
    elapsed = 0
    test_env_var = os.environ.get("TEST_ENV_VAR", "")

    print(f"Job started. Running for {duration // 60} minutes... [{test_env_var}]")

    while elapsed < duration:
        time.sleep(interval)
        elapsed += interval
        print(f"Progress: {elapsed}/{duration}s ({int(elapsed / duration * 100)}%) [{test_env_var}]")

    print(f"Job completed successfully. [{test_env_var}]")


if __name__ == "__main__":
    main()
