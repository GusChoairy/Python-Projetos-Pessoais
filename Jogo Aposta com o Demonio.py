import random, time
#LORE
print('O VILAREJO DE GOA ESTÁ EM CHAMAS, VOCÊ DEVE APOSTAR SUA ALMA CONTRA O DEMONIO MALTAEL PARA CONSEGUIR SALVAR SEUS AMIGOS E FAMÍLIA!!')
print('Tire um resultado no dado que seja maior que o do Demônio para não perder sua alma e salvar seu vilarejo!')
print('Você e o malicioso Demônio lançam seus dados ao fatídico destino! ')
dadoD = int(random.randint(1,6))
dadoD2= int(random.randint(1,6))
dadoH = int(random.randint(1,6))

print('O dado do Demonio: ',(dadoD))
print('O seu dado:', (dadoH))

#Se os dados do Humano for menor que o do Demonio:

if dadoH < dadoD:
    print('"Nínguem nunca lhe ensinou a não apostar contra um Demônio!?RMRMRMRMhahaha..."')

#se os dados do Humano for igual ao do Demonio:

elif dadoD == dadoH:
    print('=== EMPATE ===\nAgora terá que advinhar o número que cairá no dado do Demõnio. Você realmente esperava que fosse ser assim tão simples ganhar do próprio MALTAEL!?')
    advinhação = int(input('Agora Diga! Que numeros cairão nos dados? '))
    resposta = str(input('Tem CERTEZA da sua resposta? ')).strip()

#se a resposta for SIM:

    if resposta.lower() == 'sim' or resposta.lower() == 's':
        print('"Pois bem! rmrmrmm..."')
        time.sleep(2)
        print('O Demônio lança seus dados e o resultado é surpreendente!')
        print(dadoD, 'e', dadoD2)
        print('O ardiloso Demônio possuia mais de um dado.')

#se ganhar com resposta SIM:

        if dadoD == advinhação and dadoD2 == advinhação:
           print('MAS COMO PODE UM VERME COMO VOCÊ GANHAR NUMA APOSTA CONTRA O DEMÔNIO!')

#se perder com resposta SIM:
        else:
            print('O RESULTADO NÃO PODERIA SER OUTRO! SOMENTE UM ANIMAL PARA SER TÃO IGNORANTE A PONTO DE ACHAR QUE PODERIA GANHAR NUM JOGO DE AZAR CONTRA O SENHOR DAS MARUAGEM!')

#se a resposta for NÃO:
    else:
        print('"QUE SEJA {} ENTÃO!"'.format(advinhação))
        print('O Demonio lança seus dados e o resultado foi surpreendente!')
        print(dadoD,'e', dadoD2)
        print('O ardiloso Demônio possuia mais um dado.')

#se ganhar com resposta NÃO:
        if dadoD == advinhação and dadoD2 == advinhação:
#RESPOSTA PRA AMIGOS:
            print('"MAS COMO PODE UM VERME COMO VOCÊ GANHAR NUMA APOSTA CONTRA O DEMÔNIO!"')

#se perder com resposta NÃO:
        else:
            print('"O RESULTADO NÃO PODERIA SER OUTRO! SOMENTE UM ANIMAL PARA SER TÃO IGNORANTE A PONTO DE ACHAR QUE PODERIA GANHAR NUM JOGO DE AZAR CONTRA O SENHOR DAS MARUAGEM!"\n"AGORA TODOS QUE CONHECE QUEIMARÃO E SUA ALMA ME SERVIRÁ PARA SEMPRE!"')


else:
    print('O DEMONIO FICOU REVOLTADO COM O RESULTADO E VOCÊ MORREU!')