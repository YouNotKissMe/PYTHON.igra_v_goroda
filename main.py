a=input('Введите имена, через пробел: ')
a=set(a.split()) # передаём в функцию
def end(a):
    return len(max((eva(i,a) for i in a),key=len)),max((eva(i,a) for i in a),key=len)
def eva(nachalnoe_slovo,massive):
    nagisa=massive-set([nachalnoe_slovo])
    kaoru=eva02(nachalnoe_slovo,nagisa)
    if kaoru:
        pain=(eva(b,nagisa) for b in nagisa if b[0]==nachalnoe_slovo[-1])#гений мысли ,русской демократии
        max_pain=max(pain,key=len)
    else:
        max_pain=[]
    return [nachalnoe_slovo]+max_pain
def eva02(slovo,massive):
    return set(x for x in massive if x[0]==slovo[-1])
print(end(a))
