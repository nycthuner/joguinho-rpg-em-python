from random import randint as dano
import time
import os
normal=1
continuar=0
sair=0
while True:
    if continuar == 1 or normal==1:
            ap=dano(7,15)
            ad=dano(5,10)
            aumentarAp=0
            aumentarAd=0
            maisvida=15
            vidamonstro=20
            monstroreset=0
            gamerestart=0
            vidareset=5*gamerestart
            vida=maisvida+vidareset
            normal=0
            continuar=0
            sair=0
            monstros = vidamonstro+monstroreset
            continuarem=0
            gamerestart+=1
            monstroreset+=10
            aumentarAp+=3
            aumentarAd+=3
            while True:
                personagem = input("Escolha um personagem: Mago ou Guerreiro: ")
                if not "Mago" in personagem and not "Guerreiro" in personagem:
                    continue
                break
            if personagem == "Mago":
                ap+=aumentarAp
                while vida > 0 and monstros > 0:
                    time.sleep(1)
                    os.system("clear")
                    acao = input("Escolha uma acao: \n 1-Atacar \n 2-Defender \n 3-curar \n 4-descansar: ")
                    if not "1" in acao or not "2" in acao or not "3" in acao or not "4" in acao:
                        damage = dano(0,8)
                        monstrosdamage= dano(0,10)
                        curar = dano(0,5)
                        defesa = dano(0,7)
                        descanse = dano(0,5)
                        acaomonstro = dano(1,2)
                        if acao == "1":
                            if ap>damage and acaomonstro==1:
                                ap-=2
                                vida-=monstrosdamage
                                monstros-=damage
                                print("Voce esta com" ,ap ,"ap")
                                print("Seu ataque foi: " ,damage)
                                print("O ataque do monstro: " ,monstrosdamage)
                                print("Sua vida esta em: " ,vida)
                                print("A vida do monstro esta em: " ,monstros)
                            elif ap>damage and acaomonstro==2:
                                ap-=2
                                if defesa>damage:
                                    print("Voce esta com" ,ap ,"ap")
                                    print("Seu ataque foi defendido.")
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                                else:
                                    monstros-=damage
                                    monstros+=defesa
                                    print("Voce esta com" ,ap ,"ap")
                                    print("Seu foi ataque meramente defendido")
                                    print("Dano no monstro: " ,damage)
                                    print("A defesa do montro: " ,defesa)
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                            elif damage>ap and acaomonstro==2:
                                    print("Voce nao tem ap suficiente, descanse")
                                    print("Sorte sua o monstro escolheu defender")
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                            else:
                                vida-=monstrosdamage
                                print("Voce nao tem ap suficiente, descanse")
                                print("Sofreu dano do monstro: " ,monstrosdamage)
                                print("Sua vida: " ,vida)
                                print("A vida do monstro: " ,monstros)
                        elif acao =="2":
                            if acaomonstro ==1:
                                if monstrosdamage>defesa:
                                    vida-=monstrosdamage
                                    vida+=defesa
                                    print("Sua defesa nao foi suficiente")
                                    print("Dano do monstro: " ,monstrosdamage)
                                    print("Sua defesa: " ,defesa)
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                                else:
                                    print("Sua defesa fez efeito")
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                            else:
                                print("Ambos defederam")
                                print("Sua vida:" ,vida)
                                print("A vida do monstro: " ,monstros)
                        elif acao =="3":
                            if acaomonstro==1:
                                vida-=monstrosdamage
                                vida+=curar
                                print("O dano do monstro: " ,monstrosdamage)
                                print("Sua vida: " ,vida)
                                print("A vida do montro:" ,monstros)
                            else:
                                vida+=curar
                                print("Nao ocorreu nada")
                                print("Sua vida: " ,vida)
                                print("A vida do montro: " ,monstros)
                        elif acao =="4":
                            if acaomonstro==1:
                                ap+=descanse
                                vida -= monstrosdamage
                                print("Voce recuperou um pouco de ap")
                                print("voce tem " ,ap ,"de ap")
                                print("O dano do montro foi de: " ,monstrosdamage)
                                print("Sua vida: " ,vida)
                                print("A vida do montro: " ,monstros)
                            else:
                                ap+=descanse
                                print("Voce recuperou um pouco de ap")
                                print("Voce tem " ,ap ,"de ap")
                                print("O monstro escolheu se defender")
                                print("Sua vida: " ,vida)
                                print("A vida do monstro:" ,monstros)
                        else:
                            print("Escreva o numero da acao corretamente.")
            elif personagem == "Guerreiro":
                ad+=aumentarAd
                while vida > 0 and monstros > 0:
                    time.sleep(1)
                    os.system("clear")
                    acao = input("Escolha uma acao: \n 1-Atacar \n 2-Defender \n 3-curar \n 4-descansar: ")
                    if not "1" in acao or not "2" in acao or not "3" in acao or not "4" in acao:
                        damage = dano(0,8)
                        monstrosdamage= dano(0,10)
                        curar = dano(0,5)
                        defesa = dano(0,7)
                        descanse = dano(0,5)
                        acaomonstro = dano(1,2)
                        if acao == "1":
                            if ad>damage and acaomonstro==1:
                                ad-=2
                                vida-=monstrosdamage
                                monstros-=damage
                                print("Voce esta com" ,ad ,"ad")
                                print("Seu ataque foi: " ,damage)
                                print("O ataque do monstro: " ,monstrosdamage)
                                print("Sua vida esta em: " ,vida)
                                print("A vida do monstro esta em: " ,monstros)
                            elif ad>damage and acaomonstro==2:
                                ad-=2
                                if defesa>damage:
                                    print("Voce esta com" ,ad ,"ad")
                                    print("Seu ataque foi defendido.")
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                                else:
                                    monstros-=damage
                                    monstros+=defesa
                                    print("Voce esta com" ,ad ,"ad")
                                    print("Seu foi ataque meramente defendido")
                                    print("Dano no monstro: " ,damage)
                                    print("A defesa do montro: " ,defesa)
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                            elif damage>ad and acaomonstro==2:
                                    print("Voce nao tem ad suficiente, descanse")
                                    print("Sorte sua o monstro escolheu defender")
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                            else:
                                vida-=monstrosdamage
                                print("Voce nao tem ad suficiente, descanse")
                                print("Sofreu dano do monstro: " ,monstrosdamage)
                                print("Sua vida: " ,vida)
                                print("A vida do monstro: " ,monstros)
                        elif acao =="2":
                            if acaomonstro ==1:
                                if monstrosdamage>defesa:
                                    vida-=monstrosdamage
                                    vida+=defesa
                                    print("Sua defesa nao foi suficiente")
                                    print("Dano do monstro: " ,monstrosdamage)
                                    print("Sua defesa: " ,defesa)
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                                else:
                                    print("Sua defesa fez efeito")
                                    print("Sua vida: " ,vida)
                                    print("A vida do monstro: " ,monstros)
                            else:
                                print("Ambos defederam")
                                print("Sua vida:" ,vida)
                                print("A vida do monstro: " ,monstros)
                        elif acao =="3":
                            if acaomonstro==1:
                                vida-=monstrosdamage
                                vida+=curar
                                print("O dano do monstro: " ,monstrosdamage)
                                print("Sua vida: " ,vida)
                                print("A vida do montro:" ,monstros)
                            else:
                                vida+=curar
                                print("Nao ocorreu nada")
                                print("Sua vida: " ,vida)
                                print("A vida do montro: " ,monstros)
                        elif acao =="4":
                            if acaomonstro==1:
                                ap+=descanse
                                vida -= monstrosdamage
                                print("Voce recuperou um pouco de ap")
                                print("voce tem " ,ap ,"de ap")
                                print("O dano do montro foi de: " ,monstrosdamage)
                                print("Sua vida: " ,vida)
                                print("A vida do montro: " ,monstros)
                            else:
                                ap+=descanse
                                print("Voce recuperou um pouco de ap")
                                print("Voce tem " ,ap ,"de ap")
                                print("O monstro escolheu se defender")
                                print("Sua vida: " ,vida)
                                print("A vida do monstro:" ,monstros)
                        else:
                            print("Digite o numero da acao corretamente.")
            while True:
                continuarem=input("Deseja \n 1-continuar \n 2-sair:")
                if not continuarem == "1" and not continuarem == "2":
                    continue
                break
            continuar=0
            if continuarem =="2":
                    print("Obrigado por jogar!!")
                    exit()
            else:
                    continuar +=1
                    gamerestart+=1
                    monstroreset+=10
                    aumentarAp+=3
                    aumentarAd+=3
                    continue
