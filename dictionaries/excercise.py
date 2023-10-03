
paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'}
}

""" 
Escriba una funcion cuantos_en_comun(a, b),
que indique cuantos paises en comun han visitado
la persona a y la persona b.
>>> cuantos_en_comun('Pepito', 'Jhon')
# 1
"""

def cuantos_en_comun(a, b):
    
    # lista de paises donde se busca a y b
    aList = paises[a]
    bList = paises[b]

    comunes = aList & bList
    print(comunes)
    amount = len(comunes)
    print(amount)
    return amount

cuantos_en_comun('Pepito', 'John')

# 7 min.
# to dos: 
# refine code to make it name-syntax proof
# create an error catch part