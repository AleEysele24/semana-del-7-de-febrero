#Diccionarios

#Para Leér Valores
#planet = {
 #"name": "Earth",
#"moons": 1,
#}
#print(planet.get('name'))

#wibble = planet.get('wibble') # Regresa None
#wibble = planet['wibble'] # Arroja un KeyError

#Modificar Valores

 #planet.update({'name': 'Makemake'})

# name ahora es Makemake

#Update una sola llamada a la función
# Usando update

   #planet.update({
  #'name': 'Jupiter',
 # 'moons': 79
#})

# Usando corchetes
#planet['name'] = 'Jupiter'
#planet['moons'] = 79

  #planet['orbital period'] = 4333

#el diccionario planet ahora contiene: {
   ##name: 'jupiter'
   #moons: 79
   #orbital period: 4333
 #}

 #Añadimos los datos
#planet['diameter (km)'] = {
    #'polar': 133709,
    #'equatorial': 142984
#}

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

    #ENCONTRAR UN VALOR EN ESPECIFICO

    if 'december' in rainfall:
    # rainfall [en la posición december] es igual a
    # rainfall [en la posición december] + 1 (2.1+1)

      rainfall['december'] = rainfall['december'] + 1

# Si no:
else:

    # rainfall [en la posición december] es igual a 1
    rainfall['december'] = 1

  #RECUPERAR LOS VALORES DE UN DICCIONARIO
  #Total de precipitaciones 0
total_rainfall = 0

# Para cada valor en los valores de rainfall
for value in rainfall.values():
    
    # El total de las precipitaciones será igual a ese mismo + el valor que se está iterando

    total_rainfall = total_rainfall + value

# Muestra 'Hay un total de precipitaciones (el valor total) en centímetros en el último cuarto (haciendo referencia al cuarto del año)

print(f'There was {total_rainfall}cm in the last quarter')