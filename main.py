import time


def main():
    duration = 120  # seconds
    interval = 10
    elapsed = 0

    print(f"Job started. Running for {duration // 60} minutes...")

    while elapsed < duration:
        time.sleep(interval)
        elapsed += interval
        print(f"Progress: {elapsed}/{duration}s ({int(elapsed / duration * 100)}%)")

    print("Job completed successfully.")


if __name__ == "__main__":
    main()
