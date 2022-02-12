#Hacer una secuencia de Valores
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#0,1,2..... n

#print('The first planet is', planets[0])
#print('The second planet is', planets[1])
#print('The third planet is', planets[2])

#Cambiar un caracter

#planets[3] = 'Red Planet'
#print('Mars is also known as', planets[3])

#Para obtener la longitud de una lista

#number_of_planets = len(planets)
#print('There are', number_of_planets, 'planets in the solar system.')

#Asi se agrega un cadena 

#planets.append('Pluto')
#number_of_planets = len(planets)
#print('There are actually', number_of_planets, 'planets in the solar system.')

#POP para eliminar un valor
#planets.pop()  # Goodbye, Pluto
#number_of_planets = len(planets)
#print('No, there are definitely', number_of_planets, 'planets in the solar system.')

#Indices negativos
#print('The last planet is', planets[-1])
#print('The penultimate planet is', planets[-2])

#Buscar un valor en una Lista
#jupiter_index = planets.index('Jupiter')
#print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

#Asignar Floats a una variable
#gravity_on_earth = 1.0
#gravity_on_the_moon = 0.166

#Lista de fuerzas gravitacionales
#gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

#Calcular el peso de un bus en diferentes planetas
#bus_weight = 12650 # in kilograms, on Earth

#print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
#print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')

#pesos Min y Max en el Sistema Solar
#bus_weight = 12650 # in kilograms, on Earth

#print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
#print('The lightest a bus would be in the solar system is', bus_weight * min(gravity_on_planets), 'kg')
#print('The heaviest a bus would be in the solar system is', bus_weight * max(gravity_on_planets), 'kg')

#SLICE- crea una lista nueva no modifica a la actual
#planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#planets_before_earth = planets[0:2]
#print(planets_before_earth)

#planets_after_earth = planets[3:8]
#print(planets_after_earth) 

##
#planets_after_earth = planets[3:]
#print(planets_after_earth)

##Unir lista y crear una nueva
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)


#Ordenar alfabeticamente
#regular_satellite_moons.sort()
#print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#Ordenar de forma inversa
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)



