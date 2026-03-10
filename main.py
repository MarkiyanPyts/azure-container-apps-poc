import json
import os
import time


def main():
    duration = 120  # seconds
    interval = 10
    elapsed = 0
    storage_config_file_path = os.environ.get("STORAGE_CONFIG_FILE_PATH", "{}")
    print(f"Raw STORAGE_CONFIG_FILE_PATH: {storage_config_file_path}")
    try:
        config = json.loads(storage_config_file_path)
    except json.JSONDecodeError as e:
        print(f"Failed to parse STORAGE_CONFIG_FILE_PATH as JSON: {e}")
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
