from pathlib import Path

def file_search(input_path):
    file_path = Path(input_path)

    if not file_path.exists() or not file_path.is_dir():
        print("Invalid directory. Please try again.")
        return

    c_files = [f for f in file_path.rglob('*') if f.suffix.lower() == '.c']
    java_files = [f for f in file_path.rglob('*') if f.suffix.lower() == '.java']
    python_files = [f for f in file_path.rglob('*') if f.suffix.lower() == '.py']
    matlab_files = [f for f in file_path.rglob('*') if f.suffix.lower() == '.m']

    print("C Files:\n")
    for file in c_files:
        print(file)

    print("\nJava Files:\n")
    for file in java_files:
        print(file)

    print("\nPython Files:\n")
    for file in python_files:
        print(file)

    print("\nMatlab Files:\n")
    for file in matlab_files:
        print(file)

user_path_input = input("Input the directory to search: ").strip().strip('"')
file_search(user_path_input)
