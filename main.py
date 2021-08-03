def automata_id(n):
    estado_actual = 0
    estados_finales =[1]
    for i in n:
        if estado_actual == 0 and i.isalpha():
            estado_actual= 1
        elif estado_actual == 1 and i.isalnum():
            estado_actual = 1
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return "Cadena aceptada"
    elif estado_actual == -1:
        return
    else:
        return "cadena no aceptada"

def automata_cte(n):
    estado_actual = 0
    estados_finales =[1,2,4]
    for i in n:
        if estado_actual == 0 and i == "0":
            estado_actual = 2
        elif estado_actual == 0 and i in ["1","2","3","4","5","6","7","8","9"]:
            estado_actual = 1
        elif estado_actual == 1 and i in ["0","1","2","3","4","5","6","7","8","9"]:
            estado_actual = 1
        elif estado_actual == 1 and i ==".":
            estado_actual = 3
        elif estado_actual == 2 and i == ".":
            estado_actual = 3
        elif estado_actual == 3 and i in ["0","1","2","3","4","5","6","7","8","9"]:
            estado_actual = 4
        elif estado_actual == 4 and i in ["0","1","2","3","4","5","6","7","8","9"]:
            estado_actual = 4
        else:
            estado_actual = -1
            break
    print(estado_actual)
    if estado_actual in estados_finales:
        return "cadena aceptada"
    else:
        return"cadena no aceptada"

def automata_op(n):
    return (n=="=" or n=="+" or n=="*")

def automata_parender(n):
def automata_parenizq(n):
def automata_corder(n):
def automata_corizq(n):

def lexer(cadena):
    tokens = []
    posicion = 0
    while posicion <len(cadena):
        while cadena[posicion].isspace():
            posicion+=1
        comienzo_lexema = posicion
        posibles_tokens = []
        posibles_tokens_con_uno_mas = []
        lexema = ""
        todos_trampa = False
        while not todos_trampa:
            todos_trampa = True
            lexema = cadena[comienzo_lexema:posicion+1]
            posibles_tokens = posibles_tokens_con_uno_mas
            posibles_tokens_con_uno_mas = []

            for


'''inicio programa'''
cadena = ["aux1 = 12 para i desde 9 hasta 19 { mostrar aux1 + i }", "si ( x = 3 ) entonces { mostrar hola }", "si ( x = 3 ) entonces { mostrar hola } sino { mostrar python }", "num = 32", "mostrar ( 4 + 2 )", "para i desde 10 hasta 20 { mostrar ( i * 2 ) }"]
cadena_tokens =[]
for x in range(len(cadena)):
    lista = cadena[x].split(" ")
    cadena_tokens.append("")
    for i in range(len(lista)):
            cadena_tokens[x] = cadena_tokens[x] + analizar_palabra(lista[i])
for z in range(len(cadena_tokens)):
    print(cadena[z], cadena_tokens[z])
