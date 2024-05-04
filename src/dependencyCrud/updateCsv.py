# Update the dependencies.csv file with the new dependencies
import csv
import os


def save_dependencies(project):
    file_path = f'data/{project.name}_dependencies.csv'
    print(f"Saving dependencies to {file_path}")  # Debug print
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for name, version in project.dependencies.items():
                writer.writerow([name, version])
        print("Dependencies saved successfully.")  # Debug print
    except Exception as e:
        print(f"An error occurred while saving dependencies: {e}")  # Print the error message


def load_dependencies(project):
    try:
        with open(f'data/{project.name}_dependencies.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                project.dependencies[row[0]] = row[1]
    except FileNotFoundError:
        pass
    return project.dependencies
