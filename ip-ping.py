import time
import os
import blessed

term = blessed.Terminal()
underline = term.underline()
bold = term.bold()
reset = term.reset()
done = 'false'

d1 = term.color_rgb(5, 168, 255)
d2 = term.color_rgb(49, 178, 247)
d3 = term.color_rgb(80, 191, 250)
d4 = term.color_rgb(101, 197, 247)
d5 = term.color_rgb(129, 210, 252)
d6 = term.color_rgb(147, 215, 250)

def ipping():
    os.system('cls' if os.name == 'nt' else 'clear')
    count = 1
    hostname = input(f"{d2}Ente{d3}r I{d5}P A{d6}d{d1}dress h{d2}ere: " + reset)
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        response = os.system("ping " + hostname + " >nul")
        if response == 0:
            print(hostname + " Is online!")
        else:
            print(hostname + " Down")
        count +- 1
        time.sleep(.5)

ipping()