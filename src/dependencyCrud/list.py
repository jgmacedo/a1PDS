def list_dependencies(dependencies):
    for name, version in dependencies.items():
        print(f"\ndependency : {name} \nversion: {version}\n")
    print("Listed all dependencies.")