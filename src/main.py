from src.dependencyCrud.add import add_dependency
from src.dependencyCrud.delete import delete_dependency
from src.dependencyCrud.updateCsv import save_dependencies, load_dependencies
from src.dependencyCrud.list import list_dependencies
from src.dependencyCrud.update_dependency import update_dependency


def show_menu():
    print("Sistema de Gestão de Dependências")
    print("1. Adicionar Dependência")
    print("2. Remover Dependência")
    print("3. Listar Dependências")
    print("4. Atualizar Dependência")
    print("5. Sair")
    choice = input("Escolha uma opção: ")
    return choice

# não existe switch case em python então usamos if elif else


def main():
    dependencies = load_dependencies({})
    while True:
        print("\n1. Add Dependency\n2. Remove Dependency\n3. List Dependencies\n4. Update Dependency\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_dependency(dependencies)
        elif choice == '2':
            delete_dependency(dependencies)
        elif choice == '3':
            list_dependencies(dependencies)
        elif choice == '4':
            update_dependency(dependencies)
        elif choice == '5':
            save_dependencies(dependencies)
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()