# update dependency from dependencies array
from src.dependencyCrud.updateCsv import save_dependencies


def update_dependency(dependencies):
    name = input("Enter the name of the dependency to update: ")
    if name in dependencies:
        version = input("Enter the new version: ")
        dependencies[name] = version
    else:
        print("Dependency not found.")
    save_dependencies(dependencies)
