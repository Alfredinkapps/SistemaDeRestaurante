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
# O 'with open' é seguro pois fecha o arquivo automaticamente no final.
    # Usamos "w" (write) para que ele reescreva o arquivo do zero a cada atualização.
    # O encoding="utf-8" garante que acentos (como em 'Macarrão') não fiquem bugados.
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"===== PEDIDO DE {cliente.upper()} =====\n")
        
        # Se o cliente ainda não pediu nada
        if not itens_pedidos:
            arquivo.write("Nenhum item adicionado ainda.\n")
        else:
            # Percorre os itens que o cliente pediu
            for cod, qtd in itens_pedidos.items():
                nome, preco = cardapio[cod] # Pega o nome e o preço lá no dicionário global 'cardapio'
                subtotal = qtd * preco      # Calcula o valor dessa linha
                total += subtotal           # Soma ao total geral da conta
                
                # Escreve a linha do produto no .txt
                arquivo.write(f"{qtd}x {nome:<20} R$ {subtotal:.2f}\n")
                
        # Rodapé com o total formatado
        arquivo.write("-" * 32 + "\n")
        arquivo.write(f"TOTAL A PAGAR: R$ {total:.2f}\n")


def gerenciar_itens_cliente(cliente, itens_pedidos):
    """Loop para adicionar produtos ao pedido de um cliente específico."""
    mostrar_cardapio()
    print(f"\nAdicionando itens para: {cliente}")
    print("Digite o código do item (0 para voltar ao menu principal)")
    while True:
        # try/except previne que o programa quebre se o usuário digitar uma letra ao invés de número
        try:
            codigo = int(input("Código: "))
        except ValueError:
            print("Digite um número válido.")
            continue # Volta para o início do loop
        # Condição de saída do loop
        if codigo == 0:
            break
        # Verifica se o código digitado existe no cardápio
        if codigo not in cardapio:
            print("Item não encontrado.")
            continue