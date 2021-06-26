def analizar_palabra(n):
    print(n)
    palabrasReservadas =["para", "entonces", "si", "desde", "hasta","sino","mostrar","aceptar"]
    t_id = es_id(n)
    t_cte = es_cte(n)
    t_operador = es_operador(n)
    t_parenizq = n=="("
    t_parender = n==")"
    t_corizq = n =="{"
    t_corder = n== "}"
    if t_id:
        if n in palabrasReservadas:
            return "<"+n+">"
        else:
            return "<id>"
    if t_cte:
        return"<cte>"
    if t_operador:
        return"<operador>"
    if t_parenizq:
        return"<parenizq>"
    if t_parender:
        return"<parender>"
    if t_corizq:
        return "<corizq>"
    if t_corder:
        return "<corder>"

def es_id(n):
    cuerpo_alfanumerico = True
    primeraEsLetra =n[0].isalpha()
    for w in range(1,len(n)):
        if not n[w].isalnum():
            cuerpo_alfanumerico = False
    return (cuerpo_alfanumerico and primeraEsLetra)
def es_cte(n):
    contador_puntos = 0
    todos_numericos = True
    '''valores negativos'''
    if n[0] =="-":
        if n[1].isnumeric():
            for w in range(2,len(n)):
                if not n[w].isnumeric():
                    if n[w] == ".":
                        contador_puntos +=1
                    else:
                        todos_numericos =False
    else:
        '''valores positivos'''
        if n[0].isnumeric():
            for w in range(1,len(n)):
                if not n[w].isnumeric():
                    if n[w] ==".":
                        contador_puntos +=1
                    else:
                        todos_numericos = False
        else:
            return False
    return todos_numericos and contador_puntos <= 1
def es_operador(n):
    return (n=="=" or n=="+" or n=="*")

'''inicio programa'''
cadena = ["aux1 = 12 para i desde 9 hasta 19 { mostrar aux1 + i }"]
cadena_tokens =[]
for x in range(len(cadena)):
    lista = cadena[x].split(" ")
    cadena_tokens.append("")
    for i in range(len(lista)):
            cadena_tokens[x] = cadena_tokens[x] + analizar_palabra(lista[i])
print(cadena_tokens[0])