#!/usr/bin/python3
"""The Log parsing module"""
import sys
import signal


status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

# Variable to store the total file size
total_file_size = 0


def signal_handler(signal, frame):
    """
    To handle the keyboard interaction
    """
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)


def print_stats():
    """
    The function to print the statistics
    """
    print("Total file size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


try:
    line_number = 0
    for line in sys.stdin:
        line_number += 1

        parts = line.split()

        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = parts[-1]

            # Update the status code count and total file size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
                total_file_size += int(file_size)

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()
    sys.exit(0)
