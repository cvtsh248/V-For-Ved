import random
class interaction:
    def __init__(self):
        self.inter = {'antonio':['भगवान', 'Brugh!', 'Fun!', 'Having fun?', 'Oui', 'Madam'],
                      'bob':['EHEHEHEHEHHEHHEHEHEH', 'VAAAAAAAARRRRRUUUUUUUUUNNNNEEEEEEHHHH', 'SAMABAR'],
                      'avi':['*Oink Oink*', 'Vhat!'], 
                      'shourjo':['Ummm...', 'Vedanth what is wrong with you!?', 'All because of the modern music', 'God damn modern music i swear', 'Sounds better than most modern music these days', 'These modern degenerates', 'Degenerate music', 'Hare Krishna!', 'Jesus!', 'Allah!'],
                      'krishna':['You know how gay Bob is?'],
                      'ong':['Eh- guys ah', 'Any of you know where to get some nice puri?']}


    def say(self, name): 
        dialogueL = self.inter[name]
        dialogue = dialogueL[random.randint(0, len(dialogueL)-1)]
        return dialogue
    

