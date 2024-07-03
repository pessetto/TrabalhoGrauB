import csv # modulo de manupulação csv 
from datetime import datetime  # classe de manupulação de datas

# função para carregar dados do arquivo CSV
def carregar_dados(filename):
    felinos = []  #  lista vazia para armazenar os dados dos gatos
    try:
        # abre o arquivo CSV para leitura
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # cria um leitor de CSV para ler todas as linhas do arquivo
            for row in reader:
                felinos.append(row)  # adiciona cada linha (felino) à lista de felinos
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")  # caso arquivo não seja encontrado
    return felinos  # retorna lista de gatos

# função para salvar dados do CSV
def salvar_dados(filename, felinos):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = felinos[0].keys()  #  nomes dos campos (chaves do dicionário) do primeiro felino
        writer = csv.DictWriter(file, fieldnames=fieldnames)  # escritor de CSV com os nomes dos campos
        writer.writeheader()  # cabeçalho no arquivo CSV
        writer.writerows(felinos)  # escreve os dados dos felinos no arquivo CSV

# função para gerar um ID automatico a cada gato
def gerar_id(felinos):
    return str(len(felinos) + 1)  # retorna o tamanho da lista de felinos mais 1 como string

# função para cadastrar um novo gato
def cadastrar_felino(felinos):
    felino = {  # dicionário(linha) com os dados do novo gato
        "ID": gerar_id(felinos),  # gera um ID para o novo gato
        "Nome": input("Nome: "),  # solicita o nome do gato
        "Sexo": input("Sexo (M/F): "),  # solicita o sexo do gato
        "Idade": input("Idade: "),  # solicita a idade do gato
        "Raça": input("Raça: "),  # solicita a raça do gato
        "Cor Predominante": input("Cor Predominante: "),  # solicita a cor predominante do gato
        "Castrado": input("Castrado (Sim/Não): "),  # solicita se o gato é castrado
        "FIV+": input("FIV+ (Sim/Não): "),  # solicita se o gato é positivo para FIV
        "FELV+": input("FELV+ (Sim/Não): "),  # solicita se o gato é positivo para FELV
        "Data de Resgate": input("Data de Resgate (dd/mm/yyyy): "),  # solicita a data de resgate do gato
        "Adotado": input("Adotado (Sim/Não): "),  # solicita se o gato foi adotado
        "Lar Temporário": input("Lar Temporário: "),  # solicita o lar temporário do gato
        "Adoção/Hospedagem": input("Adoção/Hospedagem: "),  # solicita a situação de adoção/hospedagem do gato
        "Tutor": input("Tutor: "),  # solicita o tutor do gato
        "Contato": input("Contato: "),  # solicita o contato do tutor
        "Data Última Vacina": input("Data Última Vacina (dd/mm/yyyy): "),  # solicita a data da última vacina
        "Data Última Desvermifugação": input("Data Última Desvermifugação (dd/mm/yyyy): "),  # solicita a data da última desvermifugação
        "Data Último Antipulgas": input("Data Último Antipulgas (dd/mm/yyyy): "),  # solicita a data do último antipulgas
        "Informações Extras": input("Informações Extras: ")  # solicita informações extras sobre o gato
    }
    felinos.append(felino)  # adiciona o novo gato à lista de felinos
    print("Felino cadastrado com sucesso!")  # Informa que o gato foi cadastrado com sucesso

# função para alterar o status de um felino
def alterar_status(felinos):
    listar_felinos(felinos)  # lista os felinos cadastrados
    id_felino = input("Escolha o ID do felino que deseja alterar: ")  # solicita o ID do felino que deseja alterar
    felino = next((f for f in felinos if f["ID"] == id_felino), None)  # encontra o felino com o ID especificado
    if felino:
        print("Informações do felino:")  # exibe as informações do felino
        for i, (key, value) in enumerate(felino.items()):
            print(f"{i+1}. {key}: {value}")
        while True:
            opcao = int(input("Escolha o número da informação que deseja alterar (0 para sair): "))  # solicita o número da informação que deseja alterar
            if opcao == 0:
                break  # sai do loop se o usuário escolher 0
            campo = list(felino.keys())[opcao-1]  # obtém o campo correspondente à opção escolhida
            novo_valor = input(f"Novo valor para {campo}: ")  # solicita o novo valor para o campo
            felino[campo] = novo_valor  # atualiza o campo com o novo valor
        print("Informações alteradas com sucesso!")  # informa que as informações foram alteradas com sucesso
    else:
        print("Felino não encontrado.")  # informa que o felino não foi encontrado

# função para consultar informações sobre um felino
def consultar_felino(felinos):
    listar_felinos(felinos)  # lista os felinos cadastrados
    id_felino = input("Escolha o ID do felino que deseja consultar: ")  # solicita o ID do felino que deseja consultar
    felino = next((f for f in felinos if f["ID"] == id_felino), None)  # encontra o felino com o ID especificado
    if felino:
        print("Informações do felino:")  # exibe as informações do felino
        for key, value in felino.items():
            print(f"{key}: {value}")
    else:
        print("Felino não encontrado.")  # informa que o felino não foi encontrado

# função para listar todos os felinos
def listar_felinos(felinos):
    for felino in felinos:
        print(f"ID: {felino['ID']} - Nome: {felino['Nome']}")  # exibe o ID e o nome de cada felino

# função para apresentar estatísticas gerais dos felinos
def apresentar_estatisticas(felinos):
    total = len(felinos)  # calcula o total de felinos
    machos = sum(1 for f in felinos if f["Sexo"] == "M")  # calcula o total de machos
    femeas = sum(1 for f in felinos if f["Sexo"] == "F")  # calcula o total de fêmeas
    adotados = sum(1 for f in felinos if f["Adotado"] == "Sim")  # calcula o total de adotados
    nao_adotados = total - adotados  # calcula o total de não adotados
    fiv_negativos = sum(1 for f in felinos if f["FIV+"] == "Não" and f["FELV+"] == "Não")  # calcula o total de FIV- e FELV-
    fiv_positivos = sum(1 for f in felinos if f["FIV+"] == "Sim" and f["FELV+"] == "Não")  # calcula o total de apenas FIV+
    felv_positivos = sum(1 for f in felinos if f["FIV+"] == "Não" and f["FELV+"] == "Sim")  # calcula o total de apenas FELV+
    fiv_felv_positivos = sum(1 for f in felinos if f["FIV+"] == "Sim" and f["FELV+"] == "Sim")  # calcula o total de FIV+ e FELV+

    print("Estatísticas Gerais:")  # exibe as estatísticas gerais
    print(f"Total de felinos: {total}")
    print(f"Porcentagem de machos: {machos / total * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {femeas / total * 100:.2f}%")
    print(f"Porcentagem de adotados: {adotados / total * 100:.2f}%")
    print(f"Porcentagem de não adotados: {nao_adotados / total * 100:.2f}%")
    print(f"Porcentagem de FIV- e FELV-: {fiv_negativos / total * 100:.2f}%")
    print(f"Porcentagem de apenas FIV+: {fiv_positivos / total * 100:.2f}%")
    print(f"Porcentagem de apenas FELV+: {felv_positivos / total * 100:.2f}%")
    print(f"Porcentagem de FIV+ e FELV+: {fiv_felv_positivos / total * 100:.2f}%")

# função para filtrar dados dos felinos
def filtrar_dados(felinos):
    print("1) Consultar gatos resgatados por período")  # exibe a opção 1
    print("2) Consultar gatos adotados por período")  # exibe a opção 2
    opcao = int(input("Escolha uma opção: "))  # solicita a escolha da opção
    ano_inicio = int(input("Ano de início: "))  # solicita o ano de início do período
    ano_fim = int(input("Ano de fim: "))  # solicita o ano de fim do período
    
    if opcao == 1:
        resgatados = [f for f in felinos if ano_inicio <= datetime.strptime(f["Data de Resgate"], "%d/%m/%Y").year <= ano_fim]  # filtra os felinos resgatados no período
        print(f"Gatos resgatados entre {ano_inicio} e {ano_fim}:")  # exibe os felinos resgatados no período
        for felino in resgatados:
            print(f"ID: {felino['ID']} - Nome: {felino['Nome']} - Data de Resgate: {felino['Data de Resgate']}")
    elif opcao == 2:
        adotados = [f for f in felinos if f["Adotado"] == "Sim" and ano_inicio <= datetime.strptime(f["Data de Resgate"], "%d/%m/%Y").year <= ano_fim]  # filtra os felinos adotados no período
        print(f"Gatos adotados entre {ano_inicio} e {ano_fim}:")  # exibe os felinos adotados no período
        for felino in adotados:
            print(f"ID: {felino['ID']} - Nome: {felino['Nome']} - Data de Resgate: {felino['Data de Resgate']}")
    else:
        print("Opção inválida.")  # informa que a opção escolhida é inválida

# função principal que coordena o programa!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def main():
    filename = "felinos.csv"  # nome do arquivo CSV
    felinos = carregar_dados(filename)  # carrega os dados dos felinos do arquivo CSV
    
    while True:
        print("\nMenu Principal:")  # exibe o menu principal
        print("1) Cadastrar felino")
        print("2) Alterar status de felino")
        print("3) Consultar informações sobre felino")
        print("4) Apresentar estatísticas gerais")
        print("5) Filtragem de dados")
        print("6) Salvar")
        print("7) Sair do programa")
        opcao = int(input("Escolha uma opção: "))  # solicita a escolha da opção
        
        if opcao == 1:
            cadastrar_felino(felinos)  # chama a função para cadastrar um felino
        elif opcao == 2:
            alterar_status(felinos)  # chama a função para alterar o status de um felino
        elif opcao == 3:
            consultar_felino(felinos)  # chama a função para consultar informações sobre um felino
        elif opcao == 4:
            apresentar_estatisticas(felinos)  # chama a função para apresentar estatísticas gerais
        elif opcao == 5:
            filtrar_dados(felinos)  # chama a função para filtrar dados dos felinos
        elif opcao == 6:
            salvar_dados(filename, felinos)  # chama a função para salvar os dados no arquivo CSV
            print("Dados salvos com sucesso!")
        elif opcao == 7:
            salvar_dados(filename, felinos)  # chama a função para salvar os dados antes de sair
            print("Saindo do programa... Dados salvos com sucesso!")
            break  # sai do loop e encerra o programa
        else:
            print("Opção inválida.")  # informa que a opção escolhida é inválida

if __name__ == "__main__":
    main()  # chama a função principal para executar o programa
