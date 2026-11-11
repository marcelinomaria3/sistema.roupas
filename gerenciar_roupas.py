import os
from datetime import datetime

# Configura o caminho automatico para a Pasta 2 (2_dados_txt)
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_DADOS = os.path.join(DIRETORIO_ATUAL, "..", "2_dados_txt")
CAMINHO_ARQUIVO_TXT = os.path.join(PASTA_DADOS, "estoque_roupas.txt")


def garantir_pasta_dados():
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)


def ler_valor_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor >= 0:
                return valor
            print("Erro: O valor nao pode ser negativo.")
        except ValueError:
            print("Erro: Digite um numero valido (ex: 79.90).")


def ler_quantidade(mensagem):
    while True:
        try:
            qtd = int(input(mensagem))
            if qtd >= 0:
                return qtd
            print("Erro: A quantidade nao pode ser negativa.")
        except ValueError:
            print("Erro: Digite um numero inteiro.")


def cadastrar_roupa():
    garantir_pasta_dados()
    print("\n--- NOVO CADASTRO DE ROUPA ---")
    sku = input("Codigo SKU (ex: VES-002): ").strip().upper()
    peca = input("Nome/Descricao da peca: ").strip()
    categoria = input("Categoria (Camiseta, Calca, Vestido, Casaco): ").strip()
    cor = input("Cor: ").strip()
    tamanho = input("Tamanho (PP, P, M, G, GG, Unico): ").strip().upper()
    
    custo = ler_valor_float("Preco de Custo (R$): ")
    venda = ler_valor_float("Preco de Venda (R$): ")
    qtd = ler_quantidade("Quantidade em estoque: ")

    lucro = venda - custo
    status = "ESGOTADO" if qtd == 0 else ("ESTOQUE BAIXO" if qtd <= 3 else "DISPONIVEL")
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    registro = (
        f"--------------------------------------------------------------------\n"
        f"DATA: {data_hora} | SKU: {sku} | STATUS: {status}\n"
        f"PECA: {peca} ({categoria}) | COR: {cor} | TAMANHO: {tamanho}\n"
        f"CUSTO: R$ {custo:.2f} | VENDA: R$ {venda:.2f} | LUCRO: R$ {lucro:.2f}\n"
        f"QUANTIDADE EM ESTOQUE: {qtd} unidades\n"
        f"--------------------------------------------------------------------\n\n"
    )

    with open(CAMINHO_ARQUIVO_TXT, "a", encoding="utf-8") as arquivo:
        arquivo.write(registro)

    print(f"\n[SUCESSO] Peca '{peca}' salva em '2_dados_txt/estoque_roupas.txt'!")


def listar_roupas():
    print("\n--- ESTOQUE ATUAL (2_dados_txt/estoque_roupas.txt) ---")
    if not os.path.exists(CAMINHO_ARQUIVO_TXT):
        print("Nenhum registro encontrado ainda.")
        return

    with open(CAMINHO_ARQUIVO_TXT, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo if conteudo.strip() else "O arquivo esta vazio.")


def menu():
    garantir_pasta_dados()
    while True:
        print("\n=== GERENCIADOR DE LOJA DE ROUPAS ===")
        print("1. Cadastrar nova roupa")
        print("2. Ver estoque salvo no .txt")
        print("3. Sair")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_roupa()
        elif opcao == "2":
            listar_roupas()
        elif opcao == "3":
            print("Sistema encerrado.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu()
