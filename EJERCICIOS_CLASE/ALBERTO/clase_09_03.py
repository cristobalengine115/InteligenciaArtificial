def ev(fp, epa):
    dicOUna = {'!': 'not '}
    dicOBin = {'|': ' or ','&':' and ','=>':' '}
    ops , val = [] , []
    data = fp.split()
    for i in data:
        if i == '(': pass
        elif i in dicOUna or i in dicOBin: ops.append(i)
        elif i == ')' :
            op,va = ops.pop(), val.pop()
            if op in dicOUna: va = eval(dicOUna[op]+str(va))
            elif op == '=>' : 
                va = eval('not '+str(val.pop())+' or '+str(va))
            else: va =eval(str(va)+dicOBin[op]+str(val.pop()))
            val.append(va)
        else: val.append(epa[i])
    return val

def tdd(f,fp,epa,r): #TEST DRIVEN DEVELOPMENT
   return  f(fp,epa) == r

# print(tdd(ev,'(  ! p  )',{'p': True},[False]))
# print(tdd(ev,'( p | q )',{'p': False,'q': True}, [True]))
# print(tdd(ev,'( p & q )',{'p': False,'q': True}, [False]))
# print(tdd(ev,'( p => q )',{'p': False,'q': True}, [True]))
# print(tdd(ev,'( p => q )',{'p': True,'q': False}, [False]))

fp='( ( p => q ) => ( ( p | r ) => ( q | r ) ) )'
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            print(tdd(ev,fp,{'p':p,'q':q,'r':r},[True]))