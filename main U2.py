import pygame                                                       # U3 - Estudo de caso (PyGame): importando biblioteca externa de jogos
import sys                                                          # U3 - Biblioteca padrão: importando módulo do sistema

# ########################################################################################################
# UNIDADE I - VARIÁVEIS, TIPOS DE DADOS E EXPRESSÕES
# Conceitos já vistos na U1. Você pode alterar os valores abaixo livremente.
# ########################################################################################################

#--------------------------------------------------------------------
# Configurações de tamanho da janela (Tipos Numéricos: Inteiros)
#------------------------------------------------------------------
LARGURA_JANELA = 500                                                # U1 - Variáveis e atribuições: definindo a largura da tela
ALTURA_JANELA = 600                                                 # U1 - Variáveis e atribuições: definindo a altura da tela


#-----------------------------------------------------------------------------------
# Configurações da grade do tabuleiro (Expressões Aritméticas e Variáveis)
#---------------------------------------------------------------------------------
TAMANHO_GRADE = 4                                                   # U1 - Variáveis e atribuições: quantidade de linhas e colunas
TAMANHO_CELULA = 100                                                # U1 - Variáveis e atribuições: tamanho em pixels de cada quadrado
BORDA_CELULA = 10                                                   # U1 - Variáveis e atribuições: espaçamento entre os quadrados
MARGEM_TOPO = 80                                                    # U1 - Variáveis e atribuições: espaço para o título no topo


#-----------------------------------------------------------------------------------------------------
# Definição de Cores no formato RGB (Modifique os números de 0 a 255)
# OBS: O formato (R, G, B) é uma Tupla (Unidade II), mas tratada aqui como valor de atribuição.
#---------------------------------------------------------------------------------------------------
COR_DE_FUNDO = (187, 173, 160)                                      # U1 - Variáveis e atribuições: cor de fundo do tabuleiro
COR_DO_TEXTO = (119, 110, 101)                                      # U1 - Variáveis e atribuições: cor dos números baixos e título
TEXT0_CLARO = (249, 246, 242)                                       # U1 - Variáveis e atribuições: cor dos números altos


#-----------------------------------------------
# Texto do Título (Tipo de Dado: String)
#---------------------------------------------
NOME_DO_JOGO = "2048 - Edição U2"                                   # U1 - Tipos de dados: strings; U1 - Variáveis e atribuições


#--------------------------------
# O TABULEIRO INICIAL
#------------------------------
TABULEIRO = [                                                       # U1 - Tipos de dados: listas; U1 - Variáveis e atribuições
    [2, 0, 0, 2],                                                   # U1 - Tipos de dados: números
    [4, 0, 0, 4],                                                   # U1 - Tipos de dados: números
    [0, 8, 8, 0],                                                   # U1 - Tipos de dados: números
    [2, 2, 4, 4]                                                    # U1 - Tipos de dados: números
]


# ################################################################################
# BLOCO DE ENTRADA VIA TERMINAL (OPCIONAL E REMOVÍVEL)
# Esta seção é autocontida. Você pode apagar sem afetar o funcionamento do jogo:
# o NOME_DO_JOGO definido acima continuará valendo.
# ##############################################################################

print("==================================================")         # U1 - Entrada e saída: exibindo mensagem de boas-vindas no terminal
print("SISTEMA DE CONFIGURAÇÃO DO 2048 - MODO UNIDADE II")          # U1 - Entrada e saída: exibindo interface textual
print("==================================================")         # U1 - Entrada e saída: exibindo linha divisória

NOME_JOGADOR = input("Digite o nome do jogador: ")                  # U1 - Entrada e saída: recebendo texto do usuário
if len(NOME_JOGADOR) > 21:                                          # U1 - Estruturas de controle: if: limitando o tamanho do nome
    NOME_DO_JOGO = "2048 - Jogador de nome longo"                   # U1 - Variáveis e atribuições
else:                                                               # U1 - Estruturas de controle: else
    NOME_DO_JOGO = "2048 - Jogador: " + NOME_JOGADOR                # U1 - Tipos de dados: strings: concatenação

#-----------------------------------------------------------------------------------------------------
# Váriável booleana que será utilizada para ditar se o jogo está rodando
# Enquanto estiver True, a janela do jogo permanecerá aberta e o loop principal continuará rodando
#---------------------------------------------------------------------------------------------------
running = True                                                      # U1 - Variáveis e atribuições; U1 - Tipos de dados: booleanos

# ########################################################################################################
# UNIDADE II - ESTRUTURAS DE CONTROLE E ESTRUTURAS DE DADOS
# Esta é a parte central desta unidade. Aqui o tabuleiro deixa de ser estático e passa a se mover.
# Toda a lógica do movimento é construída com 'for', fatiamento de listas e comparação de listas.
#
# OBS: usamos 'def' (criar funções) aqui mas a definição formal de funções (parâmetros,
# retorno, escopo) é o tema da Unidade III.
# ########################################################################################################


#--------------------------------------------------------------------------------------------------------------------------------
# Dicionário que mapeia os valores das peças para suas cores correspondentes, com um valor padrão para peças maiores que 2048
#------------------------------------------------------------------------------------------------------------------------------
CORES_CELULAS = {                                                       # U2 - Estruturas de dados: dicionários: mapeando valores para cores
    0: (205, 192, 180),                                                 # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    2: (238, 228, 218),                                                 # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    4: (237, 224, 200),                                                 # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    8: (242, 177, 121),                                                 # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    16: (245, 149, 99),                                                 # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    32: (246, 124, 95),                                                 # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    64: (246, 94, 59),                                                  # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    128: (237, 207, 114),                                               # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    256: (237, 204, 97),                                                # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    512: (237, 200, 80),                                                # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    1024: (237, 197, 63),                                               # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    2048: (237, 194, 46)                                                # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
}   


#----------------------------------------------------------------------------------------
# COMPRIMIR: empurra os números de uma linha para a esquerda, removendo os zeros do meio
# Exemplo: [2, 0, 0, 2]  ->  [2, 2, 0, 0]
#--------------------------------------------------------------------------------------
def comprimir(linha):                                                   # U3 (apresentado na U2): definição de função
    
    #-----------------------------------------------------------
    # Remove zeros colcando os números no inicio da linha
    #----------------------------------------------------
    nova_linha = [x for x in linha if x != 0]                           # U2 - Estruturas de dados: listas: Compreensão

    #---------------------------------------------------------------------------------
    # Completa o restante da linha com zeros até ela voltar a ter TAMANHO_GRADE itens
    #-------------------------------------------------------------------------------
    while len(nova_linha) < TAMANHO_GRADE:                              # U2 - Estruturas de controle: while: repetindo enquanto faltar espaço
        nova_linha.append(0)                                            # U2 - Estruturas de dados: listas: preenchendo com zero
    return nova_linha                                                   # U3: devolvendo a linha pronta (retorno é detalhado na U3)


#----------------------------------------------------------------------------------------
# MESCLAR: soma pares de números iguais e vizinhos de uma linha (ex: 2 e 2 viram 4)
# Exemplo: [2, 2, 4, 4]  ->  [4, 8, 0, 0]
#--------------------------------------------------------------------------------------
def mesclar(linha):                                                     # U3 (apresentado na U2): definição de função
    nova_linha = comprimir(linha)                                       # U3: chamada de função

    #----------------------------------------------------------------------
    # Percorre a linha comparando cada número com o seu vizinho da direita
    #--------------------------------------------------------------------
    for i in range(TAMANHO_GRADE - 1):                                  # U2 - Estruturas de controle: for: percorrendo posições da linha
        if nova_linha[i] == nova_linha[i + 1] and nova_linha[i] != 0:   # U1 - if com operadores lógicos (and) e relacionais
            nova_linha[i] *= 2                                          # U1 - Expressões aritméticas: dobrando o valor da peça
            nova_linha[i + 1] = 0                                       # U1 - Variáveis e atribuições: zerando a peça que foi absorvida

    nova_linha = comprimir(nova_linha)                                  # U2: comprimindo de novo para empurrar os novos zeros para o fim
    return nova_linha                                                   # U2: devolvendo a linha somada e organizada

#----------------------------------------------------------------------------------------
# MOVER PARA A ESQUERDA: aplica 'mesclar' em cada linha do tabuleiro
#--------------------------------------------------------------------------------------
def mover_esquerda():                                                   # U3 (apresentado na U2): definição de função
    for i in range(TAMANHO_GRADE):                                      # U2 - Estruturas de controle: for: percorrendo cada linha
        TABULEIRO[i] = mesclar(TABULEIRO[i])                            # U2 - Estruturas de dados: listas: substituindo a linha pela versão mesclada

#----------------------------------------------------------------------------------------
# MOVER PARA A DIREITA: inverte a linha, mescla como se fosse à esquerda, e inverte de volta
#--------------------------------------------------------------------------------------
def mover_direita():                                                    # U3 (apresentado na U2): definição de função
    for i in range(TAMANHO_GRADE):                                      # U2 - Estruturas de controle: for: percorrendo cada linha
        linha_invertida = TABULEIRO[i][::-1]                            # U2 - Estruturas de dados: listas: fatiamento (slicing) com passo -1 (inverte)
        linha_invertida = mesclar(linha_invertida)                      # U2: reaproveitando a lógica de mesclar
        TABULEIRO[i] = linha_invertida[::-1]                            # U2 - Estruturas de dados: listas: fatiamento para restaurar a ordem original

#----------------------------------------------------------------------------------------
# MOVER PARA CIMA: trabalha com as COLUNAS. Monta cada coluna como uma lista, mescla, e devolve.
#--------------------------------------------------------------------------------------
def mover_cima():                                                       # U3 (apresentado na U2): definição de função
    for j in range(TAMANHO_GRADE):                                      # U2 - Estruturas de controle: for: percorrendo cada coluna
        coluna = []                                                     # U1 - Tipos de dados: listas: criando lista vazia para a coluna
        for i in range(TAMANHO_GRADE):                                  # U2 - Estruturas de controle: for aninhado: percorrendo as linhas
            coluna.append(TABULEIRO[i][j])                              # U2 - Estruturas de dados: listas: montando a coluna a partir do tabuleiro

        coluna = mesclar(coluna)                                        # U2: tratando a coluna como se fosse uma linha

        for i in range(TAMANHO_GRADE):                                  # U2 - Estruturas de controle: for: devolvendo os valores ao tabuleiro
            TABULEIRO[i][j] = coluna[i]                                 # U2 - Estruturas de dados: listas: escrevendo o valor de volta na matriz

#----------------------------------------------------------------------------------------
# MOVER PARA BAIXO: igual ao "para cima", mas invertendo a coluna antes e depois de mesclar
#--------------------------------------------------------------------------------------
def mover_baixo():                                                      # U3 (apresentado na U2): definição de função
    for j in range(TAMANHO_GRADE):                                      # U2 - Estruturas de controle: for: percorrendo cada coluna
        coluna = []                                                     # U1 - Tipos de dados: listas: criando lista vazia para a coluna
        for i in range(TAMANHO_GRADE):                                  # U2 - Estruturas de controle: for aninhado: percorrendo as linhas
            coluna.append(TABULEIRO[i][j])                              # U2 - Estruturas de dados: listas: montando a coluna

        coluna = coluna[::-1]                                           # U2 - Estruturas de dados: listas: fatiamento com passo -1 (inverte)
        coluna = mesclar(coluna)                                        # U2: mesclando a coluna invertida
        coluna = coluna[::-1]                                           # U2 - Estruturas de dados: listas: fatiamento para restaurar a ordem

        for i in range(TAMANHO_GRADE):                                  # U2 - Estruturas de controle: for: devolvendo os valores ao tabuleiro
            TABULEIRO[i][j] = coluna[i]                                 # U2 - Estruturas de dados: listas: escrevendo o valor de volta na matriz

# ########################################################################################################
# UNIDADE III - PYGAME (CONFIGURAÇÃO E DESENHO)
# ATENÇÃO: Não precisa entender ou modificar esta parte ainda.
# Ela serve apenas para desenhar na tela o TABULEIRO que a Unidade II manipula.
# ########################################################################################################


pygame.init()                                                           # U3 - Estudo de caso (PyGame): inicializando todos os módulos do pygame

FONTE_GRANDE = pygame.font.Font(None, 55)                               # U3 - Estudo de caso (PyGame): criando objeto de fonte
FONTE_MEDIA = pygame.font.Font(None, 40)                                # U3 - Estudo de caso (PyGame): criando objeto de fonte
FONTE_PEQUENA = pygame.font.Font(None, 30)                              # U3 - Estudo de caso (PyGame): criando objeto de fonte

janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))       # U3 - Estudo de caso (PyGame): criando janela gráfica
pygame.display.set_caption(NOME_DO_JOGO)                                # U3 - Estudo de caso (PyGame): definindo título da janela
clock = pygame.time.Clock()                                             # U3 - Estudo de caso (PyGame): criando objeto de controle de FPS

#-----------------------------------------------
# Função para desenhar o tabuleiro na tela
#---------------------------------------------
def desenhar_jogo():                                                    # U3 - Funções: definição de função sem parâmetros
    janela.fill((250, 248, 246))                                        # U3 - Estudo de caso (PyGame): preenchendo fundo da janela com cor RGB

    titulo = [
        FONTE_GRANDE.render(NOME_DO_JOGO[0:7], True, COR_DO_TEXTO),     # U3 - Estudo de caso (PyGame): renderizando texto; U1 - Strings
        FONTE_PEQUENA.render(NOME_DO_JOGO[7:], True, COR_DO_TEXTO)      # U3 - Estudo de caso (PyGame): desenhando superfície na janela
        ]  
    janela.blit(titulo[0], (20, 20))
    janela.blit(titulo[1], (140, 30))                                
    
    tabuleiro_top = MARGEM_TOPO                                                                                     # U1 - Variáveis e atribuições
    tabuleiro_left = (LARGURA_JANELA - (TAMANHO_GRADE * TAMANHO_CELULA + (TAMANHO_GRADE - 1) * BORDA_CELULA)) // 2  # U1 - Expressões: calculando margem horizontal

    pygame.draw.rect(
        janela,                                                                                         # U3 - Estudo de caso (PyGame): superfície da janela
        COR_DE_FUNDO,                                                                                   # U3 - Estudo de caso (PyGame): cor do retângulo
        (
            tabuleiro_left - 5,                                                                         # U1 - Expressões: calculando posição x
            tabuleiro_top - 5,                                                                          # U1 - Expressões: calculando posição y
            TAMANHO_GRADE * TAMANHO_CELULA + (TAMANHO_GRADE - 1) * BORDA_CELULA + 10,                   # U1 - Expressões: calculando largura
            TAMANHO_GRADE * TAMANHO_CELULA + (TAMANHO_GRADE - 1) * BORDA_CELULA + 10                    # U1 - Expressões: calculando altura
        )
    )

    #--------------------------------------------------------------------------
    # Desenha cada célula do tabuleiro percorrendo linhas e colunas
    #------------------------------------------------------------------------
    for i in range(TAMANHO_GRADE):                                                                      # U2 - Estruturas de controle: for: iterando sobre linhas
        for j in range(TAMANHO_GRADE):                                                                  # U2 - Estruturas de controle: for aninhado: iterando sobre colunas
            x = tabuleiro_left + j * (TAMANHO_CELULA + BORDA_CELULA)                                    # U1 - Expressões: posição x da célula
            y = tabuleiro_top + i * (TAMANHO_CELULA + BORDA_CELULA)                                     # U1 - Expressões: posição y da célula

            valor = TABULEIRO[i][j]                                                                     # U2 - Estruturas de dados: listas: lendo o valor da célula

            color = CORES_CELULAS.get(valor, CORES_CELULAS[2048])                                       # U2 - Estruturas de dados: dicionários: método .get() com valor padrão
            pygame.draw.rect(janela, color, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))                     # U3 - Estudo de caso (PyGame): desenhando retângulo

            if valor != 0:                                                                              # U1 - Estruturas de controle: if: verificando célula não vazia
                if valor <= 4:                                                                          # U1 - Estruturas de controle: if-elif-else: escolhendo tamanho da fonte
                    texto = FONTE_GRANDE.render(str(valor), True, COR_DO_TEXTO)                         # U3 - Estudo de caso (PyGame): renderizando número
                elif valor < 1024:                                                                      # U1 - Estruturas de controle: elif
                    texto = FONTE_MEDIA.render(str(valor), True, COR_DO_TEXTO)                          # U3 - Estudo de caso (PyGame): renderizando com fonte média
                else:                                                                                   # U1 - Estruturas de controle: else
                    texto = FONTE_PEQUENA.render(str(valor), True, TEXT0_CLARO)                         # U3 - Estudo de caso (PyGame): renderizando com fonte pequena

                texto_rect = texto.get_rect(center=(x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2))  # U3 - Estudo de caso (PyGame): centralizando texto; U1 - Expressões
                janela.blit(texto, texto_rect)                                                          # U3 - Estudo de caso (PyGame): desenhando o número na tela

    #--------------------------------------------------------
    # Exibe instruções na parte inferior da tela
    #------------------------------------------------------
    legenda = [
        FONTE_PEQUENA.render("Use WASD ou as setas para movimentar", True, (150, 150, 150)),            # U3 - Estudo de caso (PyGame): renderizando instrução
        FONTE_PEQUENA.render("Q para sair", True, (150, 150, 150))                                      # U3 - Estudo de caso (PyGame): renderizando instrução
    ]
    janela.blit(legenda[0], (tabuleiro_left, ALTURA_JANELA - 50))                                       # U3 - Estudo de caso (PyGame): desenhando legenda; U2 - Listas: acesso por índice
    janela.blit(legenda[1], (tabuleiro_left, ALTURA_JANELA - 28))                                       # U3 - Estudo de caso (PyGame): desenhando legenda; U2 - Listas: acesso por índice

    pygame.display.flip()                                                                               # U3 - Estudo de caso (PyGame): atualizando a janela (renderizando frame)

# ########################################################################################################
# UNIDADE II - GAME LOOP (O CORAÇÃO DESTA UNIDADE)
# O 'while' mantém o jogo rodando. A cada volta, lemos os eventos do teclado e, dependendo
# da tecla pressionada, chamamos uma das funções de movimento que escrevemos acima.
# ########################################################################################################

while running:                                                      # U2 - Estruturas de controle: while: loop principal do jogo
    for event in pygame.event.get():                                # U2 - Estruturas de controle: for: percorrendo a lista de eventos
        if event.type == pygame.QUIT:                               # U1 - Estruturas de controle: if: evento de fechar a janela
            running = False                                         # U1 - Variáveis e atribuições: encerrando o loop

        if event.type == pygame.KEYDOWN:                            # U1 - Estruturas de controle: if: alguma tecla foi pressionada
            if event.key in [pygame.K_LEFT, pygame.K_a]:            # U2 - Estruturas de dados: listas: operador 'in' testando pertencimento
                mover_esquerda()                                    # U2: chamando a função de movimento para a esquerda
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:         # U1 - Estruturas de controle: elif; U2 - Listas: operador 'in'
                mover_direita()                                     # U2: chamando a função de movimento para a direita
            elif event.key in [pygame.K_UP, pygame.K_w]:            # U1 - Estruturas de controle: elif; U2 - Listas: operador 'in'
                mover_cima()                                        # U2: chamando a função de movimento para cima
            elif event.key in [pygame.K_DOWN, pygame.K_s]:          # U1 - Estruturas de controle: elif; U2 - Listas: operador 'in'
                mover_baixo()                                       # U2: chamando a função de movimento para baixo
            elif event.key == pygame.K_q:                           # U1 - Estruturas de controle: elif: verificando a tecla 'Q'
                running = False                                     # U1 - Variáveis e atribuições: encerrando o loop

    desenhar_jogo()                                                 # U3 - Funções: chamada de função (desenha o estado atual)
    clock.tick(10)                                                  # U3 - Estudo de caso (PyGame): limitando os FPS

pygame.quit()                                                       # U3 - Estudo de caso (PyGame): encerrando todos os módulos do pygame
sys.exit()                                                          # U3 - Biblioteca padrão: encerrando o processo Python
