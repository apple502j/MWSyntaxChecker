"""Run as __main__."""
from MWSyntaxChecker import check_all

print('Enter lines of wikitext below. End with a line containing !!!END!!!')
text = ''
lastinp = None
while lastinp != '!!!END!!!':
    lastinp = input()
    text += lastinp + '\n'
check_all(text)
