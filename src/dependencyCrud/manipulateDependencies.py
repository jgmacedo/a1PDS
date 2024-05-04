import csv
import os


def add_dependency(project):
    name = input("Name the dependency: ")
    version = input("Version: ")
    project.dependencies[name] = version
    save_dependencies(project)
    print("Dependency added successfully.")


def delete_dependency(project):
    name = input("Enter the name of the dependency to delete: ")
    if name in project.dependencies:
        del project.dependencies[name]
        save_dependencies(project)
        print("Dependency deleted successfully.")
    else:
        print("Dependency not found.")


def update_dependency(project):
    name = input("Enter the name of the dependency to update: ")
    if name in project.dependencies:
        version = input("Enter the new version: ")
        project.dependencies[name] = version
        save_dependencies(project)
        print("Dependency updated successfully.")
    else:
        print("Dependency not found.")


def list_dependencies(project):
    if project.dependencies:
        for name, version in project.dependencies.items():
            print(f"{name}: {version}")
    else:
        print("No dependencies found.")
