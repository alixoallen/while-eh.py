a=int(input('digite um valor : [999]para parar : '))
c=999
soma=0

while a!=c :
    b=(int(input('digite um valor : [999]para parar : '))) 
    soma+=a 
    if a==999 or b==999:
        print('o loop acabou...')
        print('a soma foi de {}'.format(soma))
        break

