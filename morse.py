def space ():
    print("\n")

space()
print("Qual você escolhe?\n[ 1 ] Traduzir para a linguagem comum\n[ 2 ] Traduzir para morse")
escolha = (input())
space()

def normalmorse():
    space()
    text = input("Escreva a mensagem em caixa alta e separando cada letra:" + "\n")

    txtcompleto = text.split(" ")

    mensagem = ""

    w = len(txtcompleto)

    for a in range(w):
        if txtcompleto[a] == "A":
            mensagem += ".-"
        elif txtcompleto[a] == "B":
            mensagem += "-..."
        elif txtcompleto[a] == "C":
            mensagem += "-.-."
        elif txtcompleto[a] == "D":
            mensagem += "-.."
        elif txtcompleto[a] == "E":
            mensagem += "."
        elif txtcompleto[a] == "F":
            mensagem += "..-."
        elif txtcompleto[a] == "G":
            mensagem += "--."
        elif txtcompleto[a] == "H":
            mensagem += "...."
        elif txtcompleto[a] == "I":
            mensagem += ".."
        elif txtcompleto[a] == "J":
            mensagem += ".---"
        elif txtcompleto[a] == "K":
            mensagem += "-.-"
        elif txtcompleto[a] == "L":
            mensagem += ".-.."
        elif txtcompleto[a] == "M":
            mensagem += "--"
        elif txtcompleto[a] == "N":
            mensagem += "-."
        elif txtcompleto[a] == "O":
            mensagem += "---"
        elif txtcompleto[a] == "P":
            mensagem += ".--."
        elif txtcompleto[a] == "Q":
            mensagem += "--.-"
        elif txtcompleto[a] == "R":
            mensagem += "-.-"
        elif txtcompleto[a] == "S":
            mensagem += "..."
        elif txtcompleto[a] == "T":
            mensagem += "-"
        elif txtcompleto[a] == "U":
            mensagem += "..-"
        elif txtcompleto[a] == "V":
            mensagem += "...-"
        elif txtcompleto[a] == "W":
            mensagem += ".--"
        elif txtcompleto[a] == "X":
            mensagem += "-..-"
        elif txtcompleto[a] == "Y":
            mensagem += "-.--"
        elif txtcompleto[a] == "Z":
            mensagem += "--.."

    space()
    print(mensagem)
    space()

def morsenormal():
    space()
    text = input("Escreva a mensagem morse separando por espaços:" + "\n")

    txtcompleto = text.split(" ")

    mensagem = ""

    w = len(txtcompleto)

    for a in range(w):
        if txtcompleto[a] == ".-":
            mensagem += "a"
        elif txtcompleto[a] == "-...":
            mensagem += "b"
        elif txtcompleto[a] == "-.-.":
            mensagem += "c"
        elif txtcompleto[a] == "-..":
            mensagem += "d"
        elif txtcompleto[a] == ".":
            mensagem += "e"
        elif txtcompleto[a] == "..-.":
            mensagem += "f"
        elif txtcompleto[a] == "--.":
            mensagem += "g"
        elif txtcompleto[a] == "....":
            mensagem += "h"
        elif txtcompleto[a] == "..":
            mensagem += "i"
        elif txtcompleto[a] == ".---":
            mensagem += "j"
        elif txtcompleto[a] == "-.-":
            mensagem += "k"
        elif txtcompleto[a] == ".-..":
            mensagem += "l"
        elif txtcompleto[a] == "--":
            mensagem += "m"
        elif txtcompleto[a] == "-.":
            mensagem += "n"
        elif txtcompleto[a] == "---":
            mensagem += "o"
        elif txtcompleto[a] == ".--.":
            mensagem += "p"
        elif txtcompleto[a] == "--.-":
            mensagem += "q"
        elif txtcompleto[a] == "-.-":
            mensagem += "r"
        elif txtcompleto[a] == "...":
            mensagem += "s"
        elif txtcompleto[a] == "-":
            mensagem += "t"
        elif txtcompleto[a] == "..-":
            mensagem += "u"
        elif txtcompleto[a] == "...-":
            mensagem += "v"
        elif txtcompleto[a] == ".--":
            mensagem += "w"
        elif txtcompleto[a] == "-..-":
            mensagem += "x"
        elif txtcompleto[a] == "-.--":
            mensagem += "y"
        elif txtcompleto[a] == "--..":
            mensagem += "z"

    space()
    print(mensagem.upper())
    space()

if escolha == "1":
    morsenormal()
elif escolha == "2":
    normalmorse()