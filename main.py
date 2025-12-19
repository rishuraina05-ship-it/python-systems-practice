from log_parser import count_log_levels
from file_cleaner import clean_file

def main():
    print("Running system utilities")
    logs = count_log_levels("sample.log")
    print(logs)

    clean_file("input.txt", "output.txt")


if __name__ == "__main__":
    main()
