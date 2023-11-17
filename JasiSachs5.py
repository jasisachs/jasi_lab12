import os
import csv

def create_output_file(output_file_name):
    with open(f'files/{output_file_name}', 'w', newline='') as csvfile:
        fieldnames = ['Email', 'Time', 'Confidence']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        print("Data stored!")

def main():
    while True:
        input_file_name = input("Input file name: ").strip()

        try:
            with open(f'files/{input_file_name}', 'r') as file:
                while True:
                    output_file_name = input("Output file name: ").strip()
                    if not output_file_name:
                        print("Please enter a valid output file name.")
                    elif os.path.exists(f'files/{output_file_name}'):
                        choice = input("Overwrite existing file (y/n): ").strip().lower()
                        if choice == 'y':
                            create_output_file(output_file_name)
                            break
                        elif choice == 'n':
                            continue
                        else:
                            print("Invalid choice.")
                    else:
                        create_output_file(output_file_name)
                        break
                break
        except FileNotFoundError:
            print("File does not exist!")

if __name__ == "__main__":
    main()
