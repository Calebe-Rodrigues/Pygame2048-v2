import pygame                                                       # U3 - Estudo de caso (PyGame): importando biblioteca externa de jogos
import sys                                                          # U3 - Biblioteca padrão: importando módulo do sistema

# ########################################################################################################
# UNIDADE I - VARIÁVEIS, TIPOS DE DADOS E EXPRESSÕES
# Altere os valores abaixo livremente para ver o impacto visual no jogo
# ########################################################################################################

#------------------------------------------------------------------
# Configurações de tamanho da janela (Tipos Numéricos: Inteiros)
#------------------------------------------------------------------
LARGURA_JANELA = 500                                                # U1 - Variáveis e atribuições: definindo a largura da tela
ALTURA_JANELA = 600                                                 # U1 - Variáveis e atribuições: definindo a altura da tela


#---------------------------------------------------------------------------------
# Configurações da grade do tabuleiro (Expressões Aritméticas e Variáveis)
#---------------------------------------------------------------------------------
TAMANHO_GRADE = 4                                                   # U1 - Variáveis e atribuições: quantidade de linhas e colunas
TAMANHO_CELULA = 100                                                # U1 - Variáveis e atribuições: tamanho em pixels de cada quadrado
BORDA_CELULA = 10                                                   # U1 - Variáveis e atribuições: espaçamento entre os quadrados
MARGEM_TOPO = 100                                                   # U1 - Variáveis e atribuições: espaço para o título no topo


#---------------------------------------------------------------------------------------------------
# Definição de Cores no formato RGB (Modifique os números de 0 a 255)
# OBS: O formato (R, G, B) é uma Tupla (Unidade II), mas tratada aqui como valor de atribuição.
#---------------------------------------------------------------------------------------------------
COR_DE_FUNDO = (187, 173, 160)                                      # U1 - Variáveis e atribuições: cor de fundo do tabuleiro
COR_DO_TEXTO = (119, 110, 101)                                      # U1 - Variáveis e atribuições: cor dos números baixos e título
TEXT0_CLARO = (249, 246, 242)                                       # U1 - Variáveis e atribuições: cor dos números altos


#---------------------------------------------
# Texto do Título (Tipo de Dado: String)
#---------------------------------------------
NOME_DO_JOGO = "2048 - Edição U1"                                   # U1 - Tipos de dados: strings; U1 - Variáveis e atribuições


#------------------------------------------------------------------
# O TABULEIRO INICIAL ESTÁTICO
#------------------------------------------------------------------
TABULEIRO_TESTE = [                                                 # U1 - Tipos de dados: listas; U1 - Variáveis e atribuições
    [2, 4, 0, 0],                                                   # U1 - Tipos de dados: números
    [0, 8, 16, 0],                                                  # U1 - Tipos de dados: números
    [0, 0, 32, 64],                                                 # U1 - Tipos de dados: números
    [0, 0, 0, 128]                                                  # U1 - Tipos de dados: números
]


##############################################################################################
# UNIDADES II E III (ESTRUTURAS DE CONTROLE, FUNÇÕES E PYGAME)
# ATENÇÃO: Não precisa entender ou modificar esta parte ainda
# Ela serve apenas para processar e desenhar as variáveis que foram definidas acima.
##############################################################################################

#------------------------------------------------------------------------------------------------------------------------------
# Dicionário que mapeia os valores das peças para suas cores correspondentes, com um valor padrão para peças maiores que 2048 
#------------------------------------------------------------------------------------------------------------------------------
CORES_CELULAS = {                                                   # U2 - Estruturas de dados: dicionários: mapeando valores para cores
    0: (205, 192, 180),                                             # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    2: (238, 228, 218),                                             # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    4: (237, 224, 200),                                             # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    8: (242, 177, 121),                                             # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    16: (245, 149, 99),                                             # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    32: (246, 124, 95),                                             # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    64: (246, 94, 59),                                              # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    128: (237, 207, 114),                                           # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    256: (237, 204, 97),                                            # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    512: (237, 200, 80),                                            # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    1024: (237, 197, 63),                                           # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
    2048: (237, 194, 46)                                            # U2 - Dicionários: par chave(int)-valor(tupla); U2 - Tuplas
}

pygame.init()                                                       # U3 - Estudo de caso (PyGame): inicializando todos os módulos do pygame


#---------------------------------------------------------------------------------------------------------------------
# Tamanhos das fontes dos números. Números maiores precisam ter uma fonte menor para caberem dentro da célula
#---------------------------------------------------------------------------------------------------------------------
FONTE_GRANDE = pygame.font.Font(None, 55)                           # U3 - Estudo de caso (PyGame): criando objeto de fonte
FONTE_MEDIA = pygame.font.Font(None, 40)                            # U3 - Estudo de caso (PyGame): criando objeto de fonte
FONTE_PEQUENA = pygame.font.Font(None, 30)                          # U3 - Estudo de caso (PyGame): criando objeto de fonte

#---------------------------------------------------------------------------------
# Criando a janela do jogo e o relógio para controlar a taxa de atualização
#---------------------------------------------------------------------------------
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))   # U3 - Estudo de caso (PyGame): criando janela gráfica
pygame.display.set_caption(NOME_DO_JOGO)                            # U3 - Estudo de caso (PyGame): definindo título da janela
clock = pygame.time.Clock()                                         # U3 - Estudo de caso (PyGame): criando objeto de controle de FPS


#---------------------------------------------
# Função para desenhar o tabuleiro estático
# utilizando as variáveis definidas acima
#---------------------------------------------
def desenhar_jogo():                                                # U3 - Funções: definição de função sem parâmetros
    janela.fill((250, 248, 246))                                    # U3 - Estudo de caso (PyGame): preenchendo fundo da janela com cor RGB
    
    #------------------
    # Título do jogo
    #------------------
    titulo = FONTE_GRANDE.render(NOME_DO_JOGO, True, COR_DO_TEXTO)  # U3 - Estudo de caso (PyGame): renderizando texto; U1 - Strings
    janela.blit(titulo, (20, 20))                                   # U3 - Estudo de caso (PyGame): desenhando superfície na janela
    
    #---------------------------------------------------------------
    # Calcula a posição do tabuleiro para centralizá-lo na tela
    #---------------------------------------------------------------
    tabuleiro_top = MARGEM_TOPO                                                                                       # U1 - Variáveis e atribuições
    tabuleiro_left = (LARGURA_JANELA - (TAMANHO_GRADE * TAMANHO_CELULA + (TAMANHO_GRADE - 1) * BORDA_CELULA)) // 2    # U1 - Expressões: calculando margem horizontal 
    
    #------------------------------------------------------------------------------------------
    # Desenha o fundo do tabuleiro, criando um retângulo maior para dar um efeito de borda
    #------------------------------------------------------------------------------------------
    pygame.draw.rect(
        janela,                                                                                                 # U3 - Estudo de caso (PyGame): referência à superfície da janela
        COR_DE_FUNDO,                                                                                           # U3 - Estudo de caso (PyGame): cor do retângulo; U1 - Variáveis
        (
            tabuleiro_left - 5,                                                                                 # U1 - Expressões: calculando posição x
            tabuleiro_top - 5,                                                                                  # U1 - Expressões: calculando posição y                                             
            TAMANHO_GRADE * TAMANHO_CELULA + (TAMANHO_GRADE - 1) * BORDA_CELULA + 10,                           # U1 - Expressões: calculando largura           
            TAMANHO_GRADE * TAMANHO_CELULA + (TAMANHO_GRADE - 1) * BORDA_CELULA + 10                            # U1 - Expressões: calculando altura
         )
    )
    
    #------------------------------------------------------------------------
    # Desenha as peças do tabuleiro, iterando sobre cada célula
    # desenhando um retângulo com a cor correspondente ao valor da peça,
    # e desenhando o número da peça centralizado dentro do retângulo
    #------------------------------------------------------------------------
    for i in range(TAMANHO_GRADE):                                                                              # U2 - Estruturas de controle: for: iterando sobre linhas
        for j in range(TAMANHO_GRADE):                                                                          # U2 - Estruturas de controle: for aninhado: iterando sobre colunas
            x = tabuleiro_left + j * (TAMANHO_CELULA + BORDA_CELULA)                                            # U1 - Variáveis e atribuições / Expressões: posição x da célula
            y = tabuleiro_top + i * (TAMANHO_CELULA + BORDA_CELULA)                                             # U1 - Variáveis e atribuições / Expressões: posição y da célula
            

            #---------------------------------------------------------------------------------
            # Condicionais para segurança caso o usuário coloque um valor fora da matriz
            #---------------------------------------------------------------------------------
            if i < len(TABULEIRO_TESTE) and j < len(TABULEIRO_TESTE[i]):                                        # U1 - Estruturas de controle: if com operadores lógicos e relacionais
                valor = TABULEIRO_TESTE[i][j]                                                                   # U1 - Variáveis e atribuições
            else:                                                                                               # U1 - Estruturas de controle: else
                valor = 0                                                                                       # U1 - Variáveis e atribuições
            
            
            #------------------------------------------------------
            # Obtém a cor correspondente ao valor da peça,
            # usando o dicionário CORES_CELULAS 
            # (com um valor padrão para peças maiores que 2048)
            #------------------------------------------------------
            color = CORES_CELULAS.get(valor, CORES_CELULAS[2048])                                               # U2 - Estruturas de dados: dicionários: método .get()
            
            #------------------------------------------------------
            # Desenha o retângulo da peça com a cor correspondente
            #------------------------------------------------------
            pygame.draw.rect(janela, color, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))                             # U3 - Estudo de caso (PyGame): desenhando retângulo

            
            #---------------------------------------------------------------
            # Se a peça não for vazia (valor diferente de 0), 
            # desenha o número da peça centralizado dentro do retângulo
            #---------------------------------------------------------------
            if valor != 0:                                                                                      # U1 - Estruturas de controle: if: verificando célula não vazia
                if valor <= 4:                                                                                  # U1 - Estruturas de controle: if-elif-else: escolhendo tamanho da fonte
                    texto = FONTE_GRANDE.render(str(valor), True, COR_DO_TEXTO)                                 # U3 - Estudo de caso (PyGame): renderizando número como texto
                elif valor < 1024:                                                                              # U1 - Estruturas de controle: elif
                    texto = FONTE_MEDIA.render(str(valor), True, COR_DO_TEXTO)                                  # U3 - Estudo de caso (PyGame): renderizando com fonte média
                else:                                                                                           # U1 - Estruturas de controle: else
                    texto = FONTE_PEQUENA.render(str(valor), True, TEXT0_CLARO)                                 # U3 - Estudo de caso (PyGame): renderizando com fonte pequena
                
                texto_rect = texto.get_rect(center=(x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2))          # U3 - Estudo de caso (PyGame): centralizando texto na célula; U1 - Expressões
                janela.blit(texto, texto_rect)                                                                  # U3 - Estudo de caso (PyGame): desenhando texto na tela

    
    #------------------------------------------------------
    # Exibe instruções na parte inferior da tela
    #------------------------------------------------------
    legenda = FONTE_PEQUENA.render("Modo U1 - Altere as variáveis no código", True, (150, 150, 150))            # U3 - Estudo de caso (PyGame): renderizando instrução; U1 - Strings
    
    
    #---------------------------------------------
    # Função que escreve as intruções na tela
    #---------------------------------------------
    janela.blit(legenda, (tabuleiro_left, ALTURA_JANELA - 40))                                                  # U3 - Estudo de caso (PyGame): desenhando legenda
    
    #------------------------------------------------------
    # Atualiza a tela para mostrar as mudanças feitas
    #------------------------------------------------------
    pygame.display.flip()                                                                                       # U3 - Estudo de caso (PyGame): atualizando a janela (renderizando frame)

#---------------------------------------------------------------------------------
# Loop Principal Simplificado (Apenas mantém a janela aberta e atualiza o visual)
#---------------------------------------------------------------------------------
running = True                                                                                                  # U1 - Variáveis e atribuições; U1 - Tipos de dados: booleanos
while running:                                                                                                  # U2 - Estruturas de controle: while: loop principal do jogo
    for event in pygame.event.get():                                                                            # U2 - Estruturas de controle: for: percorrendo eventos do pygame; U3 - Estudo de caso (PyGame)
        if event.type == pygame.QUIT:                                                                           # U1 - Estruturas de controle: if: verificando evento de fechar janela
            running = False                                                                                     # U1 - Variáveis e atribuições; U1 - Tipos de dados: booleanos
            
    desenhar_jogo()                                                                                             # U3 - Funções: chamada de função
    clock.tick(10)                                                                                              # U3 - Estudo de caso (PyGame): limitando FPS; U1 - Tipos de dados: números

pygame.quit()                                                                                                   # U3 - Estudo de caso (PyGame): encerrando todos os módulos do pygame
sys.exit()                                                                                                      # U3 - Biblioteca padrão: encerrando o processo Python