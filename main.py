import json
import os
import time


def main():
    duration = 120  # seconds
    interval = 10
    elapsed = 0
    test_env_var = os.environ.get("TEST_ENV_VAR", "{}")
    print(f"Raw TEST_ENV_VAR: {test_env_var!r}")
    try:
        config = json.loads(test_env_var)
    except json.JSONDecodeError as e:
        print(f"Failed to parse TEST_ENV_VAR as JSON: {e}")
        config = {}
    start_date = config.get("startDate", "N/A")

    print(f"Job started. Running for {duration // 60} minutes... [startDate={start_date}]")

    while elapsed < duration:
        time.sleep(interval)
        elapsed += interval
        print(f"Progress: {elapsed}/{duration}s ({int(elapsed / duration * 100)}%) [startDate={start_date}]")

    print(f"Job completed successfully. [startDate={start_date}]")


if __name__ == "__main__":
    main()
