def clean_file(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if line.strip():
                    outfile.write(line)
    except FileNotFoundError:
        print("Input file not found.")


if __name__ == "__main__":
    clean_file("input.txt", "output.txt")
