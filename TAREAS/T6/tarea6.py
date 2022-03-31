dicOUna = {'!': 'not '}
dicOBin = {'|': ' or ','&':' and ','=>':' '}

ops , val = [] , []

def base(data,epa):
    if len(data) !=0:
        inicio(data,epa)
    return val


def inicio(data,epa):
    #Entra mediante un '('
    fin = False
    while(fin == False):
        if len(data)!=0:
            valor = data.pop(0)
            #print(valor)
            if(valor == '('):
                valor = inicio(data,epa)
            else:
                valor = ev(valor,epa,data)
        else: fin = True
            #elif(val == ):
    return valor

def ev(valor, epa,data):
    if valor in dicOUna or valor in dicOBin: 
        ops.append(valor)
        valor = data.pop(0)
        ev(valor, epa, data)
        return
    if valor == '(':
        inicio(data,epa)
        return
    if valor == ')' :
        op,va = ops.pop(), val.pop()
        if op in dicOUna: va = eval(dicOUna[op]+str(va))
        elif op == '=>' : 
            va = eval('not '+str(val.pop())+' or '+str(va))
        else: va =eval(str(va)+dicOBin[op]+str(val.pop()))
        val.append(va)
    else: 
        print(valor)
        val.append(epa[valor])
        if len(data)!=0:
            valor = data.pop(0)
            ev(valor, epa, data)
    return valor

def tdd(f,fp,epa,r): #TEST DRIVEN DEVELOPMENT
    data = fp.split()
    return  f(data,epa) == r

#p='( ( p => q ) => ( ( p | r ) => ( q | r ) ) )'
fp='( ( p | r ) => ( q | r ) )'
#fp='( True => True )'
#fp='( True )'
#fp= '( p & q )'
#fp= '( p | q )'
#fp='( valor => ( ( p | r ) => ( q | r ) ) )'
print(tdd(base,fp,{'p':False,'q':True,'r':True},[True]))
#Caso base, cuando se encuentra un '(' termino, en el ultimo ')', hacer que 
#se registre el numero de simbolos ( de esta manera cuando se encuentren ')'
#el contador de existencia baja. Por otro lado, una vez que encuentra el ( 
#deberia de entrar a la recursividad 