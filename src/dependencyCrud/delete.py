from src.dependencyCrud.updateCsv import save_dependencies


def delete_dependency(dependencies):
    name = input("Enter the name of the dependency to remove: ")
    if name in dependencies:
        try:
            del dependencies[name]
        except Exception:
            print("An error occurred while deleting the dependency.")
        save_dependencies(dependencies)
    else:
        print("Dependency not found.")

