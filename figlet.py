import sys 
from random import choice
from pyfiglet import Figlet
if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid using")
figlet = Figlet()
f = figlet.getFonts()
if len(sys.argv) == 1:
    rf = choice(f)
    figlet.setFont(f=rf)
elif len(sys.argv) == 3 :
    if sys.argv[1] != "-f" or sys.argv[2] not in f:
        sys.exit("Invalid using")
    figlet.setFont(f = sys.argv[2])
t = input("Please Enter text: ").strip()
print(figlet.renderText(t))

 