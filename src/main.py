from src.dependencyCrud.manipulateDependencies import add_dependency, delete_dependency, list_dependencies, update_dependency
from src.dependencyCrud.updateCsv import load_dependencies, save_dependencies
from src.dependencyCrud.Project import Project
import glob, os


def main():
    projects = []
    project_files = glob.glob('data/*_dependencies.csv')
    for project_file in project_files:
        project_name = os.path.basename(project_file).replace('_dependencies.csv', '')
        project = Project(project_name)
        projects.append(project)
    while True:
        print("\n1. Create Project\n2. Select Project\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter the name of the project: ")
            project = Project(name)
            projects.append(project)
            print("Project created successfully.")
        elif choice == '2':
            for i, project in enumerate(projects, start=1):
                print(f"{i}. {project.name}")
            project_index = int(input("Select a project: ")) - 1
            project = projects[project_index]
            load_dependencies(project)
            while True:
                print("\n1. Add Dependency\n2. Remove Dependency\n3. List Dependencies\n4. Update Dependency\n5. Back "
                      "to Project Selection")
                choice = input("Choose an option: ")
                if choice == '1':
                    add_dependency(project)
                elif choice == '2':
                    delete_dependency(project)
                elif choice == '3':
                    list_dependencies(project)
                elif choice == '4':
                    update_dependency(project)
                elif choice == '5':
                    save_dependencies(project)
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()