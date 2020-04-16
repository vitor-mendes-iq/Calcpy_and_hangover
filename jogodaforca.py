#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Jogo da Forca

# Bibliotecas

import random 

#bord


#Class Hangman
class Hangman():
    def __init__(self):
        self.quadro = [
'''
*********** Jogo da forca *************

 +---+
 |   |
     |
     |
     |
     |
=========''',
'''
 +---+
 |   |
 o   |
     |
     |
     |
=========''',
'''
 +---+
 |   |
 o   |
 |   |
     |
     |
=========''',
'''
 +---+
 |   |
 o/  |
 |   |
     |
     |
=========''',
'''
 +---+
 |   |
\o/  |
 |   |
     |
     |
=========''',
'''
 +---+
 |   |
\o/  |
 |   |
  \  |
     |
=========''',
'''
 +---+
 |   |
\o/  |
 |   |
/ \  |
     |
========='''   

]
        self.cWords = Hangman.wordSel(self)
        self.unders = Hangman.underCreator(self)
        
    def main(self):
        start = True
        lose = 0
        posicoes = list(enumerate(self.cWords))
       
        
        # O jogo
        while start:
            tamPalavra = len(self.cWords)   
            # parte gráfica
            print(self.quadro[lose])
            print("\n\nA palavra tem %s letras\n\n" %(tamPalavra)) 
            print(self.unders)
            
            Letra = str(input("Escolha uma letra: "))
            
            
            
            # Mudando underline para letra
            if Letra in self.cWords:
                for j,k in posicoes:
                    if k == Letra:
                        self.unders[j] = Letra
            
            else:
                lose += 1
                
            # Lose
            if lose == len(self.quadro):
                start = False
                print(''' 
                         _
                      __| |__
                     |__   __|
                        | |
                        | |
                     =========
                    \nYou Lose!!! \na palavra era %s. \nTente novamente.''' %(self.cWords))
            
            # Win
            if '_' not in self.unders:
                start = False
                print(self.unders)
                print('\n\nAcerto mizeravi!!! É %s mesmo!!!' %(self.cWords.upper()))
                print('\n\nAgora volta trabalhar que a vida não é so jogar')
            
            
            
            
    # Escolhendo a palavra    
    def wordSel(self):
        arquivo = open('/home/cyborg/Documentos/PythonFundamentos-master/Cap05/Lab03/palavras.txt')
        pal = arquivo.readlines()
        palavra = pal
        return random.choice(palavra).strip("\n")
    
    # Criado de underline
    def underCreator(self):
        return ['_' for i in self.cWords]
           

hang = Hangman()
hang.main()
        


# In[ ]:




