def analizar_palabra(n):
    palabrasReservadas =["para", "entonces", "si", "desde", ]
    t_id = '''es_id(n)'''
    t_cte = '''es_cte(n)'''
    t_operador = '''es_operador(n)'''
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

'''def es_id(n):
def es_cte(n):
def es_operador(n):'''

'''inicio programa'''
cadena = ["aux1 = 12 para i desde 9 hasta 19 { mostrar aux1 + i }"]
cadena_tokens =[]
for x in range(len(cadena)):
    lista = cadena[x].split(" ")
    cadena_tokens[x].append("")
    for i in range(len(lista)):
            cadena_tokens[x] = cadena_tokens[x] + analizar_palabra(lista[i])
