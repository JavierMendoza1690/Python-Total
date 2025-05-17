
def mi_generador():
    x = 1
    yield x

    x+=1
    yield x

    x+=1
    yield x

def main():
    variable_generacion = mi_generador()

    print(next(variable_generacion))    #1
    print(next(variable_generacion))    #2
    print('Impresion intermedia')
    print(next(variable_generacion))  # 3

if __name__ == '__main__':
    main()