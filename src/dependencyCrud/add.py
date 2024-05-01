from src.dependencyCrud.updateCsv import save_dependencies


def add_dependency(dependencies):
    name = input("Nome da Dependência: ")
    version = input("Versão: ")
    dependencies[name] = version
    save_dependencies(dependencies)
    print("Dependência Adicionada com Sucesso")
