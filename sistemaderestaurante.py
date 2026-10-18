# Importamos a biblioteca 'os' (Operating System) para conseguirmos interagir 
# com o sistema operacional, o que nos permite apagar os arquivos .txt depois.
import os
# Constante com o nome do estabelecimento
NOME = "BAITOLA"
# O cardápio é um dicionário onde a CHAVE é o código do produto 
# e o VALOR é uma tupla contendo ("Nome do Produto", Preço).
cardapio = {
    1: ("Feijoada", 42.00),
    2: ("Picanha na chapa", 68.50),
    3: ("Frango grelhado", 35.00),
    4: ("Macarrão ao molho", 29.90),
    5: ("Refrigerante", 7.00),
    6: ("Suco natural", 9.50),
    7: ("Pudim", 12.00),
}

def mostrar_cardapio():
    """Função simples que percorre o dicionário do cardápio e imprime na tela."""
    print(f"\n===== CARDÁPIO {NOME} =====")
    # .items() pega tanto o código (chave) quanto os dados do produto (valor)
    for codigo, (nome, preco) in cardapio.items():
        # :<20 formata o nome para ocupar 20 espaços, alinhando os preços à direita
        print(f"{codigo} - {nome:<20} R$ {preco:.2f}")

def atualizar_arquivo_txt(cliente, itens_pedidos):
    """
    Função responsável por criar ou atualizar o arquivo .txt do cliente.
    Ela é chamada toda vez que um novo item é adicionado ao pedido.
    """
    # Define o nome do arquivo usando o nome do cliente. Ex: "Alfredo.txt"
    nome_arquivo = f"{cliente}.txt"
    total = 0
    