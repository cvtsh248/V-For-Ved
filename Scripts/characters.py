import random

#Every important character will have its own class for logic stuff
class vee():
    def __init__(self):
        self.health = 100
        self.random_phrases = ['Inilaute Amma', 'By meaning?'] #Random mutterings
        self.phrases_spoken = ['Sexy ass, <name> ah','Shut up', 'Shut the fuck up, <name>', 'EEEH', 
                                'ITS YOUR FAULT!', 'EEEEH', 'Eh, you ah!', 'YOU FUCKING DID IT!', 'Do you want to be belted, <name>?'] #directed at people
    def interact(self, name):
        phrase = self.phrases_spoken[random.randint(0,len(self.phrases_spoken)-1)]
        try:
            phrase.replace('<name>', name)
        except:
            pass
        return phrase
    def mutter(self):
        phrase = self.random_phrases[random.randint(0,len(self.random_phrases)-1)]
        return phrase
    #Unfinished
    
