import os
import sys

def read_files_in_directory():
    if len(sys.argv) != 3:
        print("Wrong number of arguments")
    else:
        directory = sys.argv[1]
        extension = sys.argv[2]

    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        files = [file for file in os.listdir(directory) if file.endswith(extension)]

        for file in files:
            file_path = os.path.join(directory, file)
            try:
                with open(file_path, 'r') as f:
                    contents = f.read()
                    print(f"Contents of {file}:")
                    print(contents)
                    print()
            except IOError:
                print(f"Error accessing file: {file_path}")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#read_files_in_directory()

def rename_files_with_prefix():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
    else:
        directory= sys.argv[1]
    try:
        # Verifica daca folderul exista
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")


        files = os.listdir(directory)


        for i, file in enumerate(files):
            file_path = os.path.join(directory, file)
            new_file_name = f"file{i+1}{file}"
            new_file_path = os.path.join(directory, new_file_name)
            try:
                os.rename(file_path, new_file_path)
                print(f"Renamed {file} to {new_file_name}")
            except Exception as e:
                print(f"Error renaming file: {file_path} - {str(e)}")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#rename_files_with_prefix()
def calculate_total_size():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
    else:
        directory_path = sys.argv[1]
    try:
        # Verifica daca folderul exista
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        total_size = 0


        for foldername, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)

                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except Exception as e:
                    print(f"Error getting size for {filename}: {e}")

        print(f"Total size of all files: {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")
def count_files_by_extension():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
    else:
        directory_path = sys.argv[1]
    try:
        # Verifica daca folderul exista
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        if not os.listdir(directory_path):
            raise ValueError(f"Directory is empty: {directory_path}")


        extension_counts = {}

        for filename in os.listdir(directory_path):
            _, file_extension = os.path.splitext(filename)

            extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1


        print("File counts by extension:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except Exception as e:
        print(f"Error: {e}")
#count_files_by_extension()