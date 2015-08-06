'''
Created on Aug 6, 2015

@author: S Vin
'''

class Var(object):
    '''
    variable class containing an ID and a value
    '''

    number = 0
    def __init__(self, name, value):
        self.name = name
        self.id = Var.number
        Var.number += 1
        