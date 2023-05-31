import json


#! Cria arquivo que armazena tempo de execução dos scripts
def read(path):
    with open(path, "r") as arquivo:
        return json.load(arquivo)


def create(path, data):
    with open(path, "w") as arquivo:
        json.dump(data, arquivo)

