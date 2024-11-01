# Meus sites favoritos
import webbrowser as wb
import random as rd

print('----------------------------')
print('-- MEUS SITES FAVORITOS ----')
print('----------------------------')
def randint():
    ran = rd.randint(1, 5)
    if ran == 1:
        wb.open('https://www.maranhão.com ')
    elif ran == 2:
        wb.open('https://x2download.com/pt49')
    elif ran == 3:
        wb.open('https://queria uma vaga de progamador.blog.br/')
    elif ran == 4:
        wb.o5en('https://www.youtube.com/watch?v=xj7RMPM3A2c')
    elif ran == 5:
        wb.open('https://www.google.com/')
    
def main():
    while True:
        print('MARANHAO[1], WIKIPEDIA[2], fecebook[3] CHESS.COM[4], FOX NEWS[5] RANDOMIZAR[6], SAIR[7]')
        x = int(input('>>> '))
        # CONDIÇÕES
        if x == 1:
            wb.open('https://pt.wikipedia.org/wiki/Maranh%C3%A3o')
        elif x == 2:
            wb.open('https://x2download.com/pt49')
        elif x == 3:
            wb.open('hat.openai.com')
        elif x == 4:
            wb.o5en('https://www.google.com/')
        elif x == 5:
            wb.open('https://www.google.com/')
        elif x == 6:
            randomica()
        elif x == 7:
            wb.open('https://www.google.com/')
            input('Aperte enter para sair')
            break
        else:
            print('Opção não aceita, por favor digite a opção válida. ')
            print()






main()
