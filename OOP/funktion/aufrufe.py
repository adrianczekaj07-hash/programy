def f(x):

    ''' Hallo!'''

    if hasattr(f, "aufrufe"):
        f.aufrufe += 1
    else:
        f.aufrufe = 1
    return x + 3  

for i in range(13):
    f(i)
    print(f.aufrufe)
    # print(f(i))
print(f.__dict__)      # pokazuje rejestr objektu w postaci dics gdzie wylistowane sa wlasnosci oraz ich wartosc 
print(f.__class__)
print(f.__doc__)       # text dokumentacji funkcji