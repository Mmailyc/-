persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, # 
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}
###Comprobar si el diccionario de la persona tiene la clave de habilidades e imprimir la habilidad del medio en la lista de habilidades.
if 'skills' in persona:
    skills = persona['skills']
    if len(skills) > 1:
        middle_skill = skills[len(skills)//2]
        print(middle_skill)
##Comprobar si el diccionario de la persona tiene la clave de habilidades y verificar si la persona tiene la habilidad 'Python', e imprimir el resultado.
if 'skills' in persona:
    skills = persona['skills']
    if 'Python' in skills:
        print('La persona tiene la habilidad de Python')
    else:
        print('La persona no tiene la habilidad de Python')
##Imprimir el título del desarrollador de acuerdo a las habilidades de la persona.
if 'skills' in persona:
    skills = persona['skills']
    if skills == ['JavaScript', 'React']:
        print('Él es un desarrollador frontend')
    elif skills == ['Node', 'Python', 'MongoDB']:
        print('Él es un desarrollador backend')
    elif skills == ['React', 'Node', 'MongoDB']:
        print('Él es un desarrollador fullstack')
    else:
        print('Título desconocido')
