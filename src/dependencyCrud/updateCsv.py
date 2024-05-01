# Update the dependencies.csv file with the new dependencies
import csv
import os


def save_dependencies(dependencies):
    file_path = 'data/dependencies.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for name, version in dependencies.items():
            writer.writerow([name, version])


def load_dependencies(dependencies):
    try:
        with open('data/dependencies.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                dependencies[row[0]] = row[1]
    except FileNotFoundError:
        pass
    return dependencies
