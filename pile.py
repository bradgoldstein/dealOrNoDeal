'''
Created on Aug 6, 2015

@author: S Vin
'''

from random import randint


class Pile(object):
    '''
    pile: list of cards
    '''

    def __init__(self, id, cards):
        # self.name = name
        self.id = id
        self.cards = cards

    def pileTransfer(self, toPile, fromMethod, toMethod, numberCards, fromList, toList):
        if fromMethod == 0:
            fromMethod = "stack"
        elif fromMethod == 1: #TODO not implemented
            fromMethod = "stack"
        elif fromMethod == 2:
            fromMethod = "random"
        elif fromMethod == 3:
            fromMethod = "user"

        if toMethod == 0:
            toMethod = "stack"
        elif toMethod == 1: #TODO not implemented
            toMethod = "stack"
        elif toMethod == 2:
            toMethod = "random"



        if fromMethod == "stack":
            if toMethod == "stack":      #Places the top stack of numberCards from self onto the top of toPile: [1 2 3 4 5].pileTransfer([a b c d e], "stack", "stack", 3, None, None) results in [4 5], [1 2 3 a b c d e] respectively
                self.pileTransfer_helper(toPile, numberCards)
            elif toMethod == "multiple": #Assumes numberCards == len(toList) whose highest value <= len(toPile): places stack of numberCards from self into toPile according to values listed in toList.
                temp = toList            #Example: [1 2 3 4 5 6].pileTransfer([a b c d e f], "stack", "multiple", 3, None, [0 5 2]) --> [4 5 6] and [1 a b 3 c d e 2 f] respectively
                for i in range(len(toList)):
                    toPile.insert(max(temp), self.pop(temp.index(max(temp))))
                    temp.remove(temp.index(max(temp)))
            elif toMethod == "random":   #Places the top stack of numberCards randomly into toList
                for i in range(numberCards):
                    toPile.insert(randint(0, len(toPile)), self.popleft())
            pass
        elif fromMethod == "multiple":   #Assumes numberCards == len(fromList)
            if toMethod == "stack":      #Places given cards from self at the top of toPile
                self.pileTransfer_helper2(toPile, fromList) #[1 2 3 4 5 6].pileTransfer([a b c d e f], "multiple", "stack", 3, [0 4 2], None) results in [2 4 6] [1 5 3 a b c d e f]
            elif toMethod == "multiple": #Assumes numberCards == len(fromList) == len(toList), places each card in its appropriate position
                for i in range(len(toList)): #Example [1 2 3 4 5 6].pileTransfer([a b c d e f], "multiple", "multiple", 3, [4 1 5], [0 5 2]) --> [1 3 4], [5 a b 6 c d e 2 f]
                    temp = toList.index(max(toList))
                    for i in range(len(fromList)):
                        if fromList[i] > max(toList): fromList[i] -= 1
                    toPile.insert(temp, self.pop(temp))
            elif toMethod == "random":   #Randomply places the given cards from self into toPile
                temp = fromList.sort()
                for i in range(len(fromList)): toPile.insert(randint(0, len(toPile)), self.pop(temp.pop()))
            else:
                pass
        elif fromMethod == "random":
            if toMethod == "stack":      #Places numberCards random draws from self and puts them atop toPile
                for _ in range(numberCards): toPile.cards.insert(0, self.cards.pop(randint(0, len(self.cards)-1)))
            elif toMethod == "multiple": #Places numberCards random draws into selected positions in toPile
                temp = toList.sort()
                for _ in range(len(toList)): toPile.insert(temp.pop(), self.pop(randint(0, len(self))))
            elif toMethod == "random":   #randomly transfers numberCards from self to toPile
                for _ in range(len(toList)): toPile.insert(randint(0, len(toPile)), self.pop(randint(0, len(self))))
        elif fromMethod == "user":
            for i in range(numberCards):
                var = int(raw_input("Please select the number card: "))
                self.pileTransfer_helper2(toPile, [var])

    # def pileTransfer(self, toPile): #A Pile refers to cards from 'top' to 'bottom'
    #     toPile.insert(0, self.popleft())
    #
    def pileTransfer_helper(self, toPile, numberCards):
        for i in range(numberCards): toPile.cards.insert(i, self.cards.pop(0)) #Takes the number of cards 'as is' ie the first three elemtns transfered from 1 2 3 4 5 6 to a b c d e f results in 1 2 3 a b c d e f

    def pileTransfer_helper2(self, toPile, fromList):
        # temp = fromList
        # for i in range len(fromList): toPile.insert(i, self.pop((max(temp)))); temp.remove(temp.index(max(temp)))
        fromList.sort()
        temp = fromList
        for i in range(len(fromList)):
            toPile.cards.insert(i, self.cards.pop(temp.pop())) #Orders the temp list and moves the elements in reverse order (largest to smallest) to prevent indexing errors

#    def transfer_stack(self, pile):                                         #transfer 1: moves first item of self to the top of pile
#        pile.append(self.pop([-1]))
#    def transfer_stack_multiple(self, pile, num):                           #transfer multiple items from the top of a pile to the top of another pile?
#        for _ in range(num): self.transfer_stack(pile)
#    def transfer_stack_spec(self, pile, pos):
#        pile.insert(self.pop[-1], pos)
#    def transfer_stack_multiple_spec(self, pile, range, pos):
