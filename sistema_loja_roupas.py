import os
from datetime import datetime

ARQUIVO_ESTOQUE = "registro_estoque_roupas.txt"


def ler_valor_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor >= 0:
                return valor
            print("Erro: O valor nao pode ser negativo.")
        except ValueError:
            print("Erro: Digite um valor numerico valido (ex: 59.90).")


def ler_quantidade(mensagem):
    while True:
        try:
            qtd = int(input(mensagem))
            if qtd >= 0:
                return qtd
            print("Erro: A quantidade nao pode ser negativa.")
        except ValueError:
            print("Erro: Digite um numero inteiro.")


def definir_status_estoque(quantidade):
    if quantidade == 0:
        return "ESGOTADO"
    elif quantidade <= 3:
        return "ESTOQUE BAIXO (Repor)"
    return "DISPONIVEL"


def cadastrar_roupa():
    print("\n--- CADASTRO DE PECA DE ROUPA ---")
    sku = input("Codigo SKU (ex: CAM-010): ").strip().upper()
    descricao = input("Descricao da peca (ex: Camiseta Basica Algodao): ").strip()
    categoria = input("Categoria (Camiseta, Calca, Vestido, Casaco, etc.): ").strip()
    cor = input("Cor: ").strip()
    tamanho = input("Tamanho (PP, P, M, G, GG, Unico): ").strip().upper()
    tecido = input("Tecido/Material principal: ").strip()
    
    custo = ler_valor_float("Preco de Custo (R$): ")
    venda = ler_valor_float("Preco de Venda (R$): ")
    quantidade = ler_quantidade("Quantidade em estoque: ")

    lucro_unitario = venda - custo
    status = definir_status_estoque(quantidade)
    data_registro = datetime.now().strftime("%d/%m/%Y %H:%M")

    ficha = (
        f"====================================================================\n"
        f"DATA DE REGISTRO: {data_registro}\n"
        f"SKU: {sku} | CATEGORIA: {categoria}\n"
        f"PECA: {descricao} ({tecido})\n"
        f"COR: {cor} | TAMANHO: {tamanho}\n"
        f"PRECO CUSTO: R$ {custo:.2f} | PRECO VENDA: R$ {venda:.2f} | LUCRO/UNID: R$ {lucro_unitario:.2f}\n"
        f"QUANTIDADE: {quantidade} un. | STATUS: {status}\n"
        f"====================================================================\n\n"
    )

    with open(ARQUIVO_ESTOQUE, "a", encoding="utf-8") as arquivo:
        arquivo.write(ficha)

    print(f"\n[OK] Peca '{descricao}' ({sku}) salva com sucesso em '{ARQUIVO_ESTOQUE}'!")


def listar_estoque():
    print("\n--- CATALOGO E ESTOQUE SALVO ---")
    if not os.path.exists(ARQUIVO_ESTOQUE):
        print("Nenhuma peca cadastrada ainda.")
        return

    with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        if conteudo.strip():
            print(conteudo)
        else:
            print("O arquivo de estoque esta vazio.")


def menu():
    while True:
        print("\n=== SISTEMA DE LOJA DE ROUPAS (.TXT) ===")
        print("1. Cadastrar nova peca de roupa")
        print("2. Visualizar pecas cadastradas")
        print("3. Sair")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_roupa()
        elif opcao == "2":
            listar_estoque()
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu()
