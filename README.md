Sistema de Gerenciamento de Pedidos e Comandas (CLI)
Um sistema em linha de comando (CLI) desenvolvido em Python para gerenciamento de mesas, comandas e pedidos de estabelecimentos alimentícios. O software permite abrir contas para múltiplos clientes de forma simultânea, registrar consumo com atualização em tempo real e gerar espelhos de conta em arquivos .txt.

🚀 Funcionalidades
Gestão Multi-Cliente: Abertura e acompanhamento de múltiplos pedidos ativos em memória simultaneamente.

Persistência Dinâmica (.txt): Criação e atualização automática de um arquivo de texto individual para cada cliente a cada item adicionado.

Cardápio Estruturado: Exibição clara de produtos, códigos e preços formatados.

Controle de Quantidade e Subtotais: Cálculo automático de subtotais por item e valor total acumulado da conta.

Validação de Entradas: Tratamento de erros de digitação (valores inválidos, códigos inexistentes ou quantidades nulas/negativas).

Fechamento e Cancelamento de Comandas: Exclusão automática do arquivo .txt ao finalizar o pagamento ou ao cancelar a conta.

Confirmação de Segurança: Alerta ao tentar encerrar o sistema mantendo clientes com pedidos em aberto.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Módulos Nativos: os (para manipulação e exclusão de arquivos no sistema operacional).

📋 Estrutura do Código
Plaintext
.
├── main.py              # Código-fonte principal da aplicação
└── [cliente].txt        # Arquivos temporários gerados automaticamente para cada comanda
Principais Funções
mostrar_cardapio(): Exibe a lista de produtos disponíveis com preços formatados em R$.

atualizar_arquivo_txt(cliente, itens_pedidos): Grava ou atualiza no disco o extrato detalhado da conta do cliente.

gerenciar_itens_cliente(cliente, itens_pedidos): Loop interativo para inclusão de itens e quantidades no pedido do cliente.

ver_pedido_cliente(cliente): Lê e exibe o conteúdo do arquivo .txt da comanda selecionada.

exibir_clientes_ativos(pedidos_ativos): Lista os clientes com contas abertas no momento.

main(): Gerencia o fluxo de navegação e o menu principal da aplicação.

💻 Como Executar
Pré-requisitos
Python 3.7 ou superior instalado na máquina.

Passo a Passo
Clone o repositório ou baixe o arquivo .py:

Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
Acesse a pasta do projeto no terminal:

Bash
cd seu-repositorio
Execute o aplicativo:

Bash
python main.py
📖 Opções do Painel de Controle
Abrir novo pedido (Nova Pessoa): Registra um novo cliente e cria seu arquivo de comanda inicial.

Adicionar itens a um pedido: Seleciona um cliente ativo e abre o menu para inserção de itens do cardápio.

Ver conta de um cliente: Exibe o extrato formatado com os itens consumidos e o total a pagar.

Pagar e finalizar pedido: Exibe a conta, solicita confirmação de pagamento e remove o cliente e o arquivo .txt do sistema.

Cancelar pedido em aberto: Cancela a conta, descartando o arquivo associado sem efetuar cobrança.

Ver cardápio: Exibe a tabela de itens e preços.

Sair do Sistema: Encerra a aplicação (exige confirmação se houver contas abertas).

🔮 Possíveis Melhorias Futuras
[ ] Integração com banco de dados (SQLite ou PostgreSQL) para histórico de vendas.

[ ] Exportação de relatórios diários de faturamento.

[ ] Interface gráfica (GUI) usando customtkinter ou versão Web com Flask/FastAPI.

[ ] Sistema de cadastro dinâmico de novos itens no cardápio.
