import Digimon
import random
import math
import time
import os


def mainMenu(digiovos, qtDigi, carnes):
    print('===========================')
    print('[1] Chocar digiovo (%s)' %digiovos)
    print('[2] Alimentar digimon (%s)' %carnes)
    print('[3] Batalhar')
    print('[4] Visualizar digimons (%s)' %qtDigi)
    print('[5] Sair')
    print()
    print('[0] Recomeçar')
    print('===========================')

    
def chocarOvo(digimons):
    novomon = Digimon.digimon()
    digimons.append(novomon)

    
def alimentarDigi(digimon, Qtd):
    digimon.subirXP(Qtd)
    digimon.hp = digimon.hp + math.ceil(Qtd * ((5 / 100) * digimon.hpMax)) + 5
    if (digimon.hp > digimon.hpMax):
        digimon.hp = digimon.hpMax
        

def batalharDigi(digiAlly, digiEnemy):
    Desevoluir = 0
    XpOriginal = digiAlly.xp
    OrFor = digiAlly.forca
    OrAgi = digiAlly.agilidade
    OrHP = digiAlly.hpMax
    DigivolveuA = False
    print('===========================')
    while ((digiAlly.hp > 0) and (digiEnemy.hp > 0)):
    
        if (digiAlly.agilidade >= digiEnemy.agilidade):
            print('%s lançou um ataque...' %(digiAlly.name))
            time.sleep(1)
            if not (digiEnemy.agilidade + (digiEnemy.agilidade - digiEnemy.forca) >= random.randint(0, 200)):
                print('%s acertou o ataque!' %(digiAlly.name))
                DigivolveuA = digiAlly.subirXP(random.randint(2, 10))
                time.sleep(1)
                digiEnemy.hp = int(digiEnemy.hp) - (int(digiAlly.atk) - int(digiEnemy.forca - digiEnemy.agilidade))
            if (digiEnemy.hp > 0):
                print('%s lançou um ataque...' %(digiEnemy.name))
                time.sleep(1)
                if not (digiAlly.agilidade + (digiAlly.agilidade - digiAlly.forca) >= random.randint(0, 200)):
                    print('%s acertou o ataque!' %(digiEnemy.name))
                    DigivolveuE = digiEnemy.subirXP(random.randint(2, 10))
                    time.sleep(1)
                    digiAlly.hp = digiAlly.hp - (digiEnemy.atk - (digiAlly.forca - digiAlly.agilidade))
        else:
            print('%s lançou um ataque...' %(digiEnemy.name))
            time.sleep(1)
            if not (digiAlly.agilidade + (digiAlly.agilidade - digiAlly.forca) >= random.randint(0, 200)):
                print('%s acertou o ataque!' %(digiEnemy.name))
                DigivolveuE = digiEnemy.subirXP(random.randint(2, 10))
                time.sleep(1)
                digiAlly.hp = int(digiAlly.hp )- (digiEnemy.atk - (digiAlly.forca - digiAlly.agilidade))

            if (digiAlly.hp > 0):
                print('%s lançou um ataque...' %(digiAlly.name))
                time.sleep(1)
                if not (digiEnemy.agilidade + (digiEnemy.agilidade - digiEnemy.forca) >= random.randint(0, 200)):
                    print('%s acertou o ataque!' %(digiAlly.name))
                    DigivolveuA = digiAlly.subirXP(random.randint(2, 10))
                    time.sleep(1)
                    digiEnemy.hp = int(digiEnemy.hp) - (digiAlly.atk - (digiEnemy.forca - digiEnemy.agilidade))        
        if DigivolveuA:
            Desevoluir = Desevoluir + 1
        
    print('===========================')
    for I in range(Desevoluir):
        digiAlly.subirXP(-1, OrFor, OrAgi, OrHP)
    digiAlly.xp = XpOriginal
    del digiEnemy
                

def listarDigi(digimons):
    print()
    print('===========================')
    if (len(digimons) >= 1):
        for I in range(len(digimons)):
            print('[%s] %s' %(I + 1, digimons[I].name))
    else:
        print ('Você ainda não tem nenhum digimon.')
    print('===========================')
    print()
    
    
def main():
    Digiovo = 1
    Carnes = 0
    Digimons = []
    Controle = True
    while Controle:
        mainMenu(Digiovo, len(Digimons), Carnes)
        try:
            Ctrl = int(input())
        except:
            print('!!!!!!Atenção!!!!!!')
            print('Caractere inválido!')
            print('Tente novamente')
            Ctrl = 100
        
        if (Ctrl == 5):
            Controle = False
        elif (Ctrl == 1):
            if (Digiovo > 0):
                chocarOvo(Digimons)
                Digiovo = Digiovo - 1
        elif (Ctrl == 2):
            listarDigi(Digimons)
            D = int(input('Escolha um digimon... '))
            print('Quantos pedaços de carne deseja dar? ')
            C = int(input())
            if (C <= Carnes):
                alimentarDigi(Digimons[D - 1], C)
                Carnes = Carnes - C
            else:
                print('Você não tem essa quantia de comida...')
                print()
        elif (Ctrl == 3):
            print('Escolha um digimon para batalhar')
            listarDigi(Digimons)
            print ('[0] Voltar')
            print('===========================')
            D = int(input())
            if (D != 0):
                Inimigo = Digimon.digimon()
                Inimigo.subirXP(random.randint(0, 30))
                if Digimons[D - 1].forma >= 10:
                    Inimigo.subirXP(100)
                if Digimons[D - 1].forma >= 100:
                    Inimigo.subirXP(100)
                if Digimons[D - 1].forma >= 1000:
                    Inimigo.subirXP(500)
                if Digimons[D - 1].forma >= 10000:
                    Inimigo.subirXP(500)
                
                print('===========================')
                print('%s irá batalhar contra %s' %(Digimons[D - 1].name, Inimigo.name))
                print('Que comece a batalha!')
                print('===========================')
                
                batalharDigi(Digimons[D - 1], Inimigo)
                
                if (Inimigo.hp <= 0):
                    print('%s foi o vencedor!' %(Digimons[D - 1].name))
                    IR = random.randint (1, 5)
                    for I in range(IR):
                        if random.randint (1, 100) <= 40:
                            Carnes = Carnes + random.randint(1, 3) 
                        elif random.randint(0, 10) == 2:
                            Digiovo = Digiovo + random.randint(0, 1)
                        elif random.randint(0, 1) == 1:
                            Digimons[D - 1].subirXP(random.randint(10, 25))
                elif (Digimons[D - 1].hp <= 0):
                    print('Seu digimon foi derrotado em combate e se transformou em um digiovo...')
                    if (random.randint(1, 10) < 2):
                        Digiovo = Digiovo + 1
                        print('E você recuperou esse ovo!')
                    else:
                        print('Mas esse digiovo foi embora!')
                    Digimons.pop(D - 1)
        elif (Ctrl == 4):
            listarDigi(Digimons)
            print('[0] Voltar')
            print('===========================')
            print()
            Desc = int(input())
            if not Desc == (0):
                print('[%s] %s' %(Desc, Digimons[Desc - 1].name))
                if ((Digimons[Desc - 1].hp / Digimons[Desc - 1].hpMax) >= 0.7): 
                    print('%s parece saudavel.' %(Digimons[Desc - 1].name))
                elif (((Digimons[Desc - 1].hp / Digimons[Desc - 1].hpMax) < 0.7) and ((Digimons[Desc - 1].hp / Digimons[Desc - 1].hpMax) >= 0.4)):
                    print('%s parece estar um pouco machucado.' %(Digimons[Desc - 1].name))
                elif ((Digimons[Desc - 1].hp / Digimons[Desc - 1].hpMax) < 0.4):
                    print('%s parece estar mal.' %(Digimons[Desc - 1].name))
                print('Força:     ', Digimons[Desc - 1].forca)
                print('Agilidade: ', Digimons[Desc - 1].agilidade)
                print('===========================')
                print() 
        elif (Ctrl == 0):
            Digiovo = 1
            Carnes = 0
            Digimons = []
            for I in range (50):
                print('###########################')
                print('===========================')
 
if __name__ == '__main__':
    main()