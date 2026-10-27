import os

# Constante com o nome do estabelecimento
NOME = "Restaurante Fredericsen"

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
    Definida antes de ser chamada em 'gerenciar_itens_cliente'.
    """
    nome_arquivo = f"{cliente}.txt"
    total = 0
    # O 'with open' fecha o arquivo automaticamente no final.
    # Usamos "w" (write) para reescrever o arquivo a cada atualização.
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"===== PEDIDO DE {cliente.upper()} =====\n")
        
        # Se o cliente ainda não pediu nada
        if not itens_pedidos:
            arquivo.write("Nenhum item adicionado ainda.\n")
        else:
            # Percorre os itens que o cliente pediu
            for cod, qtd in itens_pedidos.items():
                nome, preco = cardapio[cod]
                subtotal = qtd * preco
                total += subtotal
                arquivo.write(f"{qtd}x {nome:<20} R$ {subtotal:.2f}\n")
                
        arquivo.write("-" * 32 + "\n")
        arquivo.write(f"TOTAL A PAGAR: R$ {total:.2f}\n")


def gerenciar_itens_cliente(cliente, itens_pedidos):
    """Loop para adicionar produtos ao pedido de um cliente específico."""
    mostrar_cardapio()
    print(f"\nAdicionando itens para: {cliente}")
    print("Digite o código do item (0 para voltar ao menu principal)")
    
    while True:
        try:
            codigo = int(input("Código: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        # Condição de saída do loop
        if codigo == 0:
            break

        # Verifica se o código digitado existe no cardápio
        if codigo not in cardapio:
            print("Item não encontrado.")
            continue

        try:
            qtd = int(input("Quantidade: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if qtd <= 0:
            print("Quantidade inválida.")
            continue

        # Se o cliente já pediu esse item antes, somamos a quantidade nova
        if codigo in itens_pedidos:
            itens_pedidos[codigo] += qtd
        else:
            # Primeira vez pedindo o item, cria o registro
            itens_pedidos[codigo] = qtd
                    
        nome = cardapio[codigo][0]
        print(f"{qtd}x {nome} adicionado para {cliente}!")
                
        # Atualiza o arquivo .txt do cliente
        atualizar_arquivo_txt(cliente, itens_pedidos)


def ver_pedido_cliente(cliente):
    """Lê o arquivo .txt salvo no computador e exibe na tela."""
    nome_arquivo = f"{cliente}.txt"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            print("\n" + arquivo.read())
    else:
        print("\nArquivo do cliente não encontrado.")


def exibir_clientes_ativos(pedidos_ativos):
    """Função auxiliar para listar quem está com pedidos em andamento."""
    if not pedidos_ativos:
        print("\nNenhum pedido em andamento no momento.")
        return False    
    print("\n--- CLIENTES COM PEDIDOS ABERTOS ---")
    for cliente in pedidos_ativos.keys():
        print(f"- {cliente}")
    return True


def main():
    """
    Função principal que controla o fluxo do programa.
    """
    pedidos_ativos = {}

    print(f"Bem-vindo ao sistema do {NOME}!")
    
    # Loop infinito do menu principal
    while True:
        print("\n" + "="*35)
        print(f"   PAINEL DE CONTROLE - {NOME}")
        print("="*35)
        print(f"Clientes ativos agora: {len(pedidos_ativos)}")
        print("1 - Abrir novo pedido (Nova Pessoa)")
        print("2 - Adicionar itens a um pedido")
        print("3 - Ver conta de um cliente")
        print("4 - Pagar e finalizar pedido")
        print("5 - Cancelar pedido em aberto")
        print("6 - Ver cardápio")
        print("0 - Sair do Sistema")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cliente = input("\nQual o nome do novo cliente? ").strip()
            if not cliente:
                print("Nome não pode ser vazio.")
            elif cliente in pedidos_ativos:
                print(f"Já existe um pedido aberto para {cliente}.")
            else:
                pedidos_ativos[cliente] = {}
                atualizar_arquivo_txt(cliente, pedidos_ativos[cliente])
                print(f"Conta aberta para {cliente}! Arquivo .txt criado.")
                
        elif opcao == "2":
            if exibir_clientes_ativos(pedidos_ativos):
                cliente = input("\nPara qual cliente deseja adicionar itens? ").strip()
                if cliente in pedidos_ativos:
                    gerenciar_itens_cliente(cliente, pedidos_ativos[cliente])
                else:
                    print("Cliente não encontrado na lista de ativos.")
                    
        elif opcao == "3":
            if exibir_clientes_ativos(pedidos_ativos):
                cliente = input("\nQual cliente deseja visualizar? ").strip()
                if cliente in pedidos_ativos:
                    ver_pedido_cliente(cliente)
                else:
                    print("Cliente não encontrado.")
                    
        elif opcao == "4":
            if exibir_clientes_ativos(pedidos_ativos):
                cliente = input("\nQual cliente vai realizar o pagamento? ").strip()
                if cliente in pedidos_ativos:
                    ver_pedido_cliente(cliente)
                    confirma = input("Confirmar pagamento e encerrar? (s/n): ").strip().lower()
                    if confirma == 's':
                        nome_arquivo = f"{cliente}.txt"
                        if os.path.exists(nome_arquivo):
                            os.remove(nome_arquivo)
                        del pedidos_ativos[cliente] 
                        print(f"Pagamento concluído! O pedido de {cliente} foi finalizado e o arquivo excluído.")
                else:
                    print("Cliente não encontrado.")
                    
        elif opcao == "5":
            if exibir_clientes_ativos(pedidos_ativos):
                cliente = input("\nQual cliente deseja CANCELAR o pedido? ").strip()
                if cliente in pedidos_ativos:
                    confirma = input(f"Tem certeza que deseja cancelar tudo de {cliente}? (s/n): ").strip().lower()
                    if confirma == 's':
                        nome_arquivo = f"{cliente}.txt"
                        if os.path.exists(nome_arquivo):
                            os.remove(nome_arquivo)
                        del pedidos_ativos[cliente]
                        print(f"Pedido de {cliente} cancelado e arquivo excluído com sucesso.")
                else:
                    print("Cliente não encontrado.")

        elif opcao == "6":
            mostrar_cardapio()
            
        elif opcao == "0":
            if pedidos_ativos:
                print("\nATENÇÃO: Ainda existem pedidos abertos!")
                confirma = input("Deseja realmente sair do sistema? (s/n): ").strip().lower()
                if confirma != 's':
                    continue
            print(f"\nSistema encerrado. O {NOME} agradece.")
            break
            
        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()