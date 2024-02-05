#! /usr/bin/python3
#  banner.py: programa que constrói um banner e
#  o retorna para impressão

LENGTH = 80 # banner length

def createBanner(str):
    '''This function creates a banner'''
    return  '+' + '-'*(LENGTH-2) + '+\n' +\
            '|' + str.center(78) + '|\n' +\
            '+' + '-'*(LENGTH-2) + '+\n'

# test
print(createBanner('This sentence can be until 70 characters'))
