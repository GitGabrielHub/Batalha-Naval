from time import sleep    ##### Jogo fecha depois de 5 segundos
from conteudo import *    ##### Importar arquivo "conteudo"
opcao = 0
arquivo = open ('Regras.txt' , encoding='utf8')
mostrar_regras (arquivo)
arquivo.close()

dicionario = {'A':1,'B':2,'C':3,'D':4,
              'E':5,'F':6,'G':7,'H':8,
              'I':9,'J':10,'K':11,'L':12,
              'M':13,'N':14,'O':15,'P':16}

while opcao != 4:
    boole = True
    
    try:      
        opcao = int(input('''1 - Para iniciar o jogo.
2 - Mostrar ranking.
3 - Mostrar novamente as regras.
4 - Sair do jogo.

Digite a opção: '''))

        print()

    except:
        boole = False
        print('\nEntrada inválida. Tente novamente.\n')

    if boole:
        if opcao == 1:
            boole_1 = True
            lvl,nick = dados()
            tiros_total = 0
            tiros_acertos = 0
            score = 0
            lista_ja_foi = [] 
            vida = 2 + ( 2 * lvl )
            tamanho = 4 + (4 * lvl)
            quant_barcos = 2 + (4 * lvl)
            barco_2 = lvl + 1
            barco_3 = lvl + 1
            barco_4 = lvl
            barco_5 = lvl 
            bombas = 2 + (4 * lvl)

            while True:

                achou = True
                tamanho_barco = 2
                matriz_barcos = []
                lista_barcos = []
                aux = []
                aux_bombas = []
                bombs = []
                booleana = True
                
                for vezes in range(quant_barcos):  #### Loop para chamar função que criará coordenadas horizontais ou verticais.
                    
                    lista_barcos = []
                    aleatorio = random.choice(['v', 'h'])
                    cord_x , cord_y = coordenada_aleatoria (aleatorio,tamanho,tamanho_barco)

                    try:
                        lista_barcos = gerar_coordenadas_barco(tamanho_barco,[],cord_x, cord_y ,achou,aleatorio,aux,tamanho_barco,tamanho)  #### Lista com coordenadas e posição 
                        
                    except RecursionError:
                        booleana = False

                    except:
                        traceback.print_exc()
                    
                    if booleana:

                        tamanho_barco = adicionar_coordenadas (barco_2,barco_3,barco_4,barco_5,vezes,tamanho_barco)
                        matriz_barcos.append(lista_barcos)

                        aux = []
                            
                        for a in range(len(matriz_barcos)):         #### Loop para criar lista a partir de todas as coordenas horizontais e verticais dos barcos para
                            for i in range(len(matriz_barcos[a])):  #### fazer comparações em algumas funções.
                                aux.append(matriz_barcos[a][i])
                if booleana:
                    break
                        
            matriz = gerar_matriz(tamanho)
            letra = letra_da_matriz(tamanho , dicionario)
            bombs.append(coordenadas_bombas(bombas, [],tamanho,aux,lvl))
            desenhar_matriz(matriz,tamanho,score,vida,tiros_total)
         
            while (len(aux) != 0) and (vida != 0):
                while boole_1 == True:
                    coord_jogador = input('Escolha um número de 1 à %d e uma letra de "A" a "%s" para atirar: '%(tamanho,letra))
                    if analisar_coordenadas_do_jogador ( coord_jogador, tamanho ):
                        if len(coord_jogador) == 2:
                            jogador_x = int(coord_jogador[0])
                            jogador_y = dicionario[coord_jogador[1].upper()]
                        else:
                            jogador_x = int(coord_jogador[0] + coord_jogador[1])
                            jogador_y = dicionario[coord_jogador[2].upper()]
                        boole_1 = False

                    else:
                        desenhar_matriz(matriz,tamanho,score,vida,tiros_total)

                if boole_1 == False:
                    
                    jogador_x -=1
                    jogador_y -=1

                    if [jogador_x , jogador_y] in lista_ja_foi:
                        print('\nCoordenada já escolhida. Tente novamente.')
                    else:                           
                        lista_ja_foi.append([jogador_x, jogador_y])                                           
                        if [jogador_x , jogador_y] in aux:
                            matriz[jogador_x][jogador_y] = '+'
                            tiros_acertos +=1
                            aux.remove([jogador_x , jogador_y])
                            score += 53.63
                        
                        elif [jogador_x , jogador_y] in bombs[0]:
                            matriz[jogador_x][jogador_y] = 'o'
                            vida-=1

                        else:
                             matriz[jogador_x][jogador_y] = '~'

                        tiros_total+=1
                    desenhar_matriz(matriz,tamanho,score,vida,tiros_total)
                    boole_1 = True
                    
            if len(aux) == 0:
                score = score -((tiros_total - tiros_acertos) * (10.65 - lvl))
                print('WINNER!')
                print('Pontuação final: %d' % score )
                print('Total de tiros na água: %d\n'% (tiros_total - tiros_acertos))
                arquivo = open('Ranking.txt','a')
                arquivo.write('%s - %d\n'%(nick,score))
                arquivo.close()                        

            else:
                print('LOSER!')
                print('Pontuação final: 0\n')
                        
            print('FIM DE JOGO!\n')
            print('Voltando para o menu.\n')

        elif opcao == 2:
            try:
                txt = open('Ranking.txt' , 'r')
            except:
                txt = open('Ranking.txt' , 'w+') 
             
            lista = txt.readlines()           
            txt.close()
            arq = open('Ranking.txt' , 'w')
            ranking_sort ( lista , arq )
            arq.close()
            arquivo = open ('Ranking.txt' , 'r')
            print('RANKING!\n')
            print('OS CINCO PRIMEIROS:\n')
            mostrar_ranking ( arquivo )
            arquivo.close()

        elif opcao == 3:
            arquivo = open ('Regras.txt' , encoding='utf8')
            mostrar_regras (arquivo) 
            arquivo.close()
            
        elif opcao != 4 :
            print('Opção inválida.\n')

print('Obrigado por jogar!')
sleep(5)
