import random
import math
from enum import Enum

class EDigimons(Enum):
    Botamon = 1
    Nyokimon = 2
    Punimon = 3
    Pichimon = 4
    Poyomon = 5
    Yuramon = 6
    YukimiBotamon = 7
    
    Koromon = 10
    Yokomon = 20
    Tsunomon = 30
    Bukamon = 40
    Tokomon = 50
    Tanemon = 60
    Nyaromon = 70
    
    Agumon = 101
    AgumonX = 102
    Piyomon = 200
    Gabumon = 301
    Bearmon = 302
    Gomamon = 400
    Patamon = 500
    Palmon = 601
    Floramon = 602
    Salamon = 700
    
    Greymon = 1011
    Meramon = 1012
    Centaurmon = 1013 #Não evolui
    GreymonX = 1021
    GeoGreymon = 1022
    Birdramon = 2001
    Aquilamon = 2002
    Garurumon = 3010
    Gryzmon = 3021
    LoaderLiomon = 3022
    Ikkakumon = 4001
    Gaogamon = 4002
    Angemon = 5000
    Togemon = 6011
    Woodmon = 6012
    Vegiemon = 6020 #Não evolui
    Gatomon = 7001
    BlackGatomon = 7002
    
    MetalGreymon = 10111
    SkullGreymon = 10112
    BlueMeraMon = 10120
    MetalGreymonX = 10210
    RiseGreymon = 10220
    Garudamon = 20010, 20020
    WereGarurumon = 30101
    ShadowWereGarurumon = 30102
    Monzeamon = 30211
    Pandamon = 30212
    Baihumon = 30220
    Zudomon = 40010
    MachGaogamon = 40020
    HolyAngemon = 50000
    Lillymon = 60110
    Cherrymon = 60120
    Angewomon = 70010
    LadyDevimon = 70020
    

class digimon(object):
    __slots__ = ['__name', '__HP', '__for', '__agi', '__fel', '__XP', '__formaAtual', '__HPMax']
    
    def __getAtk(self):
        if (random.randint(0, 100) <= self.agilidade):
            dano = math.floor(((self.forca + self.agilidade) / 1.5) * (1 + (self.agilidade / 10)))
        else:
            dano = math.floor(((self.forca + self.agilidade) / 1.5) * (1 + self.agilidade / 100))
        
        return dano
    
    @property
    def hp(self):
        return self.__HP
    
    @property
    def hpMax(self):
        return self.__HPMax
        
    @property
    def name(self):
        return self.__name
    
    @property
    def forca(self):
        return self.__for
    
    @property
    def agilidade(self):
        return self.__agi
    
    @property
    def felicidade(self):
        return self.__fel
        
    @property
    def xp(self):
        return self.__XP
    
    @property
    def atk(self):
        return self.__getAtk()
    
    @property
    def forma(self):
        return self.__formaAtual
    
    @hp.setter
    def hp(self, hp):
        self.__HP = hp
        
    @name.setter
    def name(self, name):
        self.__name = name
        
    @felicidade.setter
    def felicidade(self, fel):
        self.__fel = fel
        
    @xp.setter
    def xp(self, xp):
        self.__XP = xp
        
    def __init__(self):
        self.__formaAtual = random.randint(1, 7)
        self.__for = random.randint(4, 7)
        self.__agi = random.randint(4, 7)
        self.__HPMax = random.randint(15, 25)
        if self.__for + self.__agi < 10:
            self.__HPMax = self.__HPMax + 7 - math.floor((self.__agi + self.__for) / 2)
        self.name = EDigimons(self.__formaAtual).name
        self.hp = self.__HPMax
        self.felicidade = 10
        self.xp = 0
        
    def subirXP(self, ganhoXP, OrFor = 0, OrAgi = 0, OrHP = 0):
        if (ganhoXP < 0):
            self.__voltaForma(OrFor, OrAgi, OrHP)
            Digivolveu = True
            print(self.name, ' voltou a sua forma normal...')
        else:
            self.xp = self.xp + ganhoXP
            Digivolveu = False
            if self.forma < 10:
                while (self.xp >= 50):
                    print('%s digivolve para...' %(self.name))
                    self.xp = self.xp - 50
                    Digivolveu = self.__digivolve()
                    print(self.name, '!')
            elif (self.forma >=10 and self.forma < 100):
                while (self.xp >= 100):
                    print('%s digivolve para...' %(self.name))
                    self.xp = self.xp - 100
                    Digivolveu = self.__digivolve()
                    print(self.name, '!')
            if (self.forma >= 100):
                while (self.xp >= 500):
                    if not ((self.forma == 1013) or (self.forma == 6020)):
                        print('%s digivolve para...' %(self.name))
                    self.xp = self.xp - 500
                    Digivolveu = self.__digivolve()
                    if not ((self.forma == 1013) or (self.forma == 6020)):
                        print(self.name, '!')
                    else:
                        print(self.name, ' não é mais capaz de evoluir, mas ficou mais forte!')

                        
        
        return Digivolveu
        
    def __voltaForma(self, OrFor, OrAgi, OrHP):
        self.__formaAtual = math.floor(self.__formaAtual / 10)
        self.name = EDigimons(self.__formaAtual).name
        self.__for = OrFor
        self.__agi = OrAgi
        self.__HPMax = OrHP
        
    def __digivolve(self):
        if (self.__formaAtual == 10) or (self.__formaAtual == 30) or (self.__formaAtual == 60): #duas possibilidades
            self.__formaAtual = self.__formaAtual * 10 + random.randint(1,2)
        elif (self.__formaAtual == 200) or (self.__formaAtual == 301) or (self.__formaAtual == 302):
            self.__formaAtual = self.__formaAtual * 10 + random.randint(1,2)
        elif (self.__formaAtual == 400) or (self.__formaAtual == 601) or (self.__formaAtual == 102):
            self.__formaAtual = self.__formaAtual * 10 + random.randint(1,2)
        elif (self.__formaAtual == 700) or (self.__formaAtual == 1011) or (self.__formaAtual == 3010):
            self.__formaAtual = self.__formaAtual * 10 + random.randint(1,2)
        elif (self.__formaAtual == 3021):
            self.__formaAtual = self.__formaAtual * 10 + random.randint(1,2)

        elif (self.__formaAtual == 101): #tres possibilidades
            self.__formaAtual = self.__formaAtual * 10 + random.randint(1,3)
        
        elif ((self.forma == 1013) or (self.forma == 6020)): #Não digivolve
            self.__formaAtual = self.__formaAtual
        
        else:
            self.__formaAtual = self.__formaAtual * 10
            
        
        self.name = EDigimons(self.__formaAtual).name
        
        self.__agi = self.__agi + random.randint (3, 7)
        self.__for = self.__for + random.randint (3, 7)
        self.__HPMax = self.__HPMax + random.randint(20, 30)
        self.felicidade = self.felicidade + 5
        return True
    