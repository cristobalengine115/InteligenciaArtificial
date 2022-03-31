""" Definición de operaciones """
dicOUna = {'!': 'not '}
dicOBin = {'|': ' or ','&':' and ','=>':' '}

""" Pilas de operadores y valores """
ops , val = [] , []

def base(data,epa):
    '''Detecta si la longitud de data esta vacia para volver a inicio'''
    if len(data) !=0:
        inicio(data,epa)
    return val


def inicio(data,epa):
    '''Detecta un parentesis de inicio para una nueva operación'''
    #Entra mediante un '('
    fin = False
    while(fin == False):
        if len(data)!=0:
            valor = data.pop(0)
            if(valor == '('):
                valor = inicio(data,epa)
            else:
                valor = ev(valor,epa,data)
        else: fin = True
    return valor

def ev(valor, epa,data):
    '''Evalua la operación a realizar o indica si se abre o cierra una nueva operación'''
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
        #print(valor)
        val.append(epa[valor])
        if len(data)!=0:
            valor = data.pop(0)
            ev(valor, epa, data)
    return valor


def tdd(f,fp,epa,r): #TEST DRIVEN DEVELOPMENT
    '''TEST DRIVEN DEVELOPMENT, Nos permite evaluar una función, con los parametros solicitados y la respuesta esperada'''
    data = fp.split()
    return  f(data,epa) == r


##PRUEBAS UNITARIAS USANDO TEST DRIVEN DEVELOPMENT
#T1
fp='( ( p | r ) => ( q | r ) )'
print(tdd(base,fp,{'p':False,'q':True,'r':True},[True]))
val=[]
#T2
fp='( ( p => q ) => ( ( p | r ) => ( q | r ) ) )'
print(tdd(base,fp,{'p':False,'q':True,'r':True},[True]))
val=[]
#T3
fp= '( p & q )'
print(tdd(base,fp,{'p':False,'q':True},[False]))
val=[]
#T4
fp= '( p | q )'
print(tdd(base,fp,{'p':False,'q':True},[True]))
val=[]
