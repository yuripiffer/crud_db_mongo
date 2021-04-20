import re
import cpf_tools



def delete_symbols(text: str):
    text = re.sub('[!?.@# ;$,/-]', '', text)
    return text


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = delete_symbols(cpf)
    if cpf_tools.cpf_str_validation(cpf):
        return cpf
    else:
        return False  # ACHO QUE NÃO PRECISAVA


def valida_idade(idade):
    if not idade.isdigit() or int(idade) > 150:
        return False
    else:
        return int(idade)


def valida_maior_idade(idade):
    if not idade.isdigit() or int(idade) > 150 or int(idade) < 18:
        return False
    else:
        return int(idade)


def valida_altura_metros(altura):
    altura = altura.replace(",", ".")
    if not altura.isdigit() or float(altura) < 0 or float(altura) > 2.5:
        return False
    else:
        return float(altura)


def valida_preco(preco):
    preco = preco.replace(",", ".")
    if not preco.isdigit() or float(preco) < 0:
        return False
    else:
        return float(preco)  # TALVEZ LIMITAR A DUAS CASAS DECIMAIS

def valida_nome(nome):
    if not len(nome) < 2 or len(nome) > 200 or nome.isdigit():
        return False
    else:
        return nome