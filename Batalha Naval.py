from time import sleep
from conteudo import * ####mostrar_regras,ranking_sort, mostrar_ranking

opcao = 0
mostrar_regras ( open ('Regras.txt' , 'r'))
lista = [1,2,3]
boole_1,boole_2 = True, False
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
            lvl,nick = dados (lista)

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
            barco_5 = lvl + 1
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

                        tamanho_barco = adicionar_coordenadas ( barco_2,barco_3,barco_4,barco_5,vezes,tamanho_barco)
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
            desenhar_matriz(matriz,tamanho,score,vida,tiros_total,letra)

            while aux != 0:
                
                
                try:
                    while boole_1:
                        eixo_x = int(input('Escolha um número de 1 à %d que irá representar a linha: '%tamanho))
                        if analisar_coordenadas_do_jogador ( eixo_x, tamanho ):
                            boole_1 = False

                    while boole_2 == False:
                        eixo_y = input('Escolha uma letra de "A" a "%s" que irá representar a coluna: '%letra)
                        eixo_y = dicionario[eixo_y.upper()]
                        if analisar_coordenadas_do_jogador ( eixo_y, tamanho ):
                            boole_2 = True
                except:
                    desenhar_matriz(matriz,tamanho,score,vida,tiros_total,letra)
                    print('\nEntrada inválida. Tente novamente\n')
                    
                if boole_2:
                    
                    eixo_x -=1
                    eixo_y -=1

                    if [eixo_x , eixo_y] in lista_ja_foi:
                        print('\nCoordenada já escolhida. Tente novamente.')
                    else:
                           
                        lista_ja_foi.append([eixo_x, eixo_y])
                                             
                        if [eixo_x , eixo_y] in aux:
                            matriz[eixo_x][eixo_y] = '+'
                            tiros_acertos +=1
                            aux.remove([eixo_x , eixo_y])
                            score += 53.63
                        
                        elif [eixo_x , eixo_y] in bombs[0]:
                            matriz[eixo_x][eixo_y] = '*'
                            vida-=1

                        else:
                             matriz[eixo_x][eixo_y] = '~'

                        tiros_total+=1

                    desenhar_matriz(matriz,tamanho,score,vida,tiros_total,letra)
                
                    if len(aux) == 0:
                        score = score -((tiros_total - tiros_acertos) * 10)
                        print('WINNER!')
                        print('Pontuação final: %d' % score )
                        print('Total de tiros errados: %d\n'% (tiros_total - tiros_acertos))

                        arquivo = open('Ranking.txt','a')
                        arquivo.write('%s - %d\n'%(nick,score))
                        arquivo.close()
                        break

                    elif vida == 0:
                        
                        print('LOSER!')
                        print('Pontuação final: 0\n')
                        break

                    boole_1,boole_2 = True, False



            print('FIM DE JOGO!\n')
            print('Voltando para o menu.\n')




        elif opcao == 2:
            lista = open('Ranking.txt' , 'r')
            l = lista.readlines()
            lista.close()
            arq = open('Ranking.txt' , 'w')
            
            ranking_sort ( l , arq )
            arq.close()
            arquivo = open ('Ranking.txt' , 'r')
            print('Ranking:')
            mostrar_ranking ( arquivo )
            
        elif opcao == 3:
            
            mostrar_regras ( open ('Regras.txt' , 'r'))   

        elif opcao != 4 :
            print('Opção inválida.\n')

print('Obrigado por jogar.')
sleep(5)
