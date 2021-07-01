password = "arroz"
array_de_tracos = []
string_array = ''
tentativas = 6
letras_digitadas = []

palavra_iteirada = ''

encerrou = False
vencedor = False

print("#################################")
print("######### JOGO DA FORCA #########")
print("################################\n")


print("Adivinhe a palavra abaixo: \n")

for x in password:
    array_de_tracos.append(" __ ")

print(string_array.join(array_de_tracos), '\n')

while not encerrou and not vencedor:
    print("Tentativas Restantes", tentativas)
    print("Palpites Errados: ", letras_digitadas, "\n")
    letter = input('Digite uma letra: ')

    normalize_letter = letter.lower().strip()





    if password.find(normalize_letter) < 0:
        tentativas = tentativas - 1
        letras_digitadas.append(normalize_letter.upper())
       # print('Não achou')
    else:
        i = 0
       # print('Achou')
        for x in password:

            if x == normalize_letter:
                array_de_tracos[i] = " " + letter.upper() + " "
            i += 1

    print("")
    print(string_array.join(array_de_tracos), '\n')

    try:
        array_de_tracos.index(' __ ')
    except ValueError:
        vencedor = True

    if(tentativas == 0):
      encerrou = True
      print('#######################')
      print('##### GAMER OVER ######')
      print('#######################')

    if (vencedor == True):
        encerrou = True
        print('#######################')
        print('##### VOCÊ VENCEU #####')
        print('#######################')