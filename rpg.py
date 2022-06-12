from random import randint as dano
monstros = 20
while True:
    personagem = input("Escolha um personagem: Mago ou Guerreiro: ")
    if not "Mago" in personagem and not "Guerreiro" in personagem:
        continue
    break

mago = int(dano(7,15))
guerreiro = int(dano(5,10))
if personagem == "Mago":
    personagem = mago
    while personagem > 0 and monstros > 0:
        acao = input("Escolha sua acao: \n Atacar \n Defender \n Curar \n Descansar: ")
        if not "Atacar" in acao or not "Defender" in acao or not "Curar" in acao or not "Descansar" in acao:
            atacarmago = dano(0,8)
            descansar = dano(1,5)
            if acao == "Atacar":
                personagem -= 2
                monstros -= atacarmago
                print("Sua vida: " ,personagem)
                print("Dano do ataque" ,atacarmago)
                print("A vida do monstro: " ,monstros)
            elif acao == "Defender":
                personagem -= 1
                print("Sua vida: " ,personagem)
                print("A vida do monstro: " ,monstros)
            elif acao == "Curar":
                personagem +=1
                print("Sua vida: " ,personagem)
                print("A vida do monstro: " ,monstros)
            elif acao == "Descansar":
                personagem +=descansar
                print("A sua vida: " ,personagem)
                print("A vida do monstro: " ,monstros)
            else:
                print("Por favor digitar certo")
else:
    personagem = guerreiro
    while personagem > 0 and monstros > 0:
        acao = input("Escolha sua acao: \n Atacar \n Defender \n Curar \n Descansar: ")
        if not "Atacar" in acao or not "Defender" in acao or not "Curar" in acao or not "Descansar" in acao:
            atacarwarrior = dano(0,8)
            descansar = dano(1,5)
            if acao == "Atacar":
                personagem -= 2
                monstros -= atacarwarrior
                print("Sua vida: " ,personagem)
                print("Dano do ataque" ,atacarwarrior)
                print("A vida do monstro: " ,monstros)
            elif acao == "Defender":
                personagem -= 1
                print("Sua vida: " ,personagem)
                print("A vida do monstro: " ,monstros)
            elif acao == "Curar":
                personagem +=1
                print("Sua vida: " ,personagem)
                print("A vida do monstro: " ,monstros)
            elif acao == "Descansar":
                personagem +=descansar
                print("A sua vida: " ,personagem)
                print("A vida do monstro: " ,monstros)
            else:
                print("Por favor digitar certo")
while True:
    continuar=input("Deseja continuar ou sair:")
    if not "continuar" in  continuar and not "sair" in continuar:
        continue
    break

if "continuar" in continuar:
    print("va fazer outra coisa pls")
else:
    print("obg por jogar volte sempre")
