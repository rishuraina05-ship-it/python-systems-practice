def count_log_levels(file_path):
    """
    Reads a log file and counts occurrences of common log levels.
    """
    levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(file_path, "r") as file:
            for line in file:
                # Check each log level in the current line
                for level in levels:
                    if level in line:
                        levels[level] += 1
    except FileNotFoundError:
        print("Log file not found.")

    return levels


if __name__ == "__main__":
    # Example usage
    result = count_log_levels("sample.log")
    print(result)
