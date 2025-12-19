def count_log_levels(file_path):
    levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(file_path, "r") as file:
            for line in file:
                for level in levels:
                    if level in line:
                        levels[level] += 1
    except FileNotFoundError:
        print("Log file not found.")

    return levels


if __name__ == "__main__":
    result = count_log_levels("sample.log")
    print(result)
