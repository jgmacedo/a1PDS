from src.dependencyCrud.updateCsv import save_dependencies


def add_dependency(dependencies):
    name = input("Name the dependency: ")
    version = input("Version: ")
    dependencies[name] = version
    save_dependencies(dependencies)
    print("Dependency added successfully.")
