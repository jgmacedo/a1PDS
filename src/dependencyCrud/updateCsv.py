# Update the dependencies.csv file with the new dependencies
import csv


def save_dependencies(dependencies):
    with open('data/dependencies.csv', 'w', newline='') as csvfile:
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
