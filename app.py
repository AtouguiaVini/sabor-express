import os

restaurantes = [{'nome':'Praça', 'categoria':'Petiscaria','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Italiana','ativo':True},
                {'nome':'SushiBar','categoria':'Japonesa','ativo':False}]

# Cadastro de restaurantes com menu
def exibir_nome_do_programa():
    '''exibe o nome estilizado do app'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def exibir_opcoes():
    '''Exibe menu de seleções'''
    print('1. Cadastro de Restaurante')
    print('2. Lista de Restaurantes')
    print('3. Alterar status de Restaurantes')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    '''Exibe de subtítulos conforme opção selecionada do menu'''
    os.system('cls')
    linha = '*' * (len(texto) +1)
    print(linha)
    print(f'{texto}')
    print(linha)
    print('')

def voltar_menu_principal():
    '''retorna ao menu de seleções'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def finalizar_app():
    '''Finaliza o app'''
    os.system('cls')
    print('Finalizando o app\n')

def opcao_invalida():
    '''Esta função acusa seleção de opção inválida e retorna ao menu principal'''
    exibir_subtitulo('Opção Inválida!')

    voltar_menu_principal()


def cadastrar_novo_restaurante():
    '''Esta função é responsável por cadastrar novos restaurantes
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novo restaurante')

    nome_do_restaurante = input('Digite o nome do Restaurante: ')
    categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar_menu_principal()

# print(f'Você escolheu a opção {opcao_escolhida}')
# print(type(opcao_escolhida))

def listar_restaurantes():
    '''Exibe lista de restaurantes conforme incluido na string restaurantes'''

    exibir_subtitulo('Lista de restaurantes')

    print(f'{'Nome do restaurante'.ljust(28)} | {'Categoria'.ljust(31)} | Status')
    print('')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- Nome: {nome_restaurante.ljust(20)} | Categoria: {categoria_restaurante.ljust(20)} | Situação: {ativo_restaurante}')
    voltar_menu_principal()

def alternar_estado_restaurante():
    '''Esta função altera o estado do restaurante entre ativo e não ativo
    
    Inputs:
    - nome do restaurante

    Outputs
    - caso identifique, realiza a ativação | caso não identifique, retorna aviso que não foi encontrado
        
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu_principal()

def escolher_opcao():
    '''Esta função solicita uma opção para o usuário
    
    input:
    - Escolher opção

    output:
    - direciona para a opção escolhida

    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    '''Função principal de carregamento do app - chama as demais funções principais'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ =='__main__':
    main() 