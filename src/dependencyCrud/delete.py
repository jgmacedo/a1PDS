def delete_dependency(dependencies):
    name = input("Enter the name of the dependency to remove: ")
    if name in dependencies:
        del dependencies[name]
    else:
        print("Dependency not found.")


def list_dependencies(dependencies):
    for name, version in dependencies.items():
        print(f"{name}: {version}")
