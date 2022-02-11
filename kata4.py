#Primer Ejercicio
mars_temperature = 'The highest temperature on Mars is about 30 C'

for item in mars_temperature.split():
   # if item.isnumeric():
        #print(item)
#Segundo Ejercicio
   if "30 C".endswith("C"):
    #print("This temperature is in Celsius")

#Tercer Ejercicio
          'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C')

#Cuarto Ejercicio
text = 'Temperatures on the Moon can vary wildly.'
'temperatures' in text

'temperatures' in text.lower()

'temperatures' in text.lower()
#Quinto Ejercicio

moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']
'\n'.join(moon_facts)

#mass_percentage = '1/6'
#print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)

#print("""Both sides of the %s get the same amount of sunlight,
    #but only one side is seen from %s because
    #the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))

mass_percentage = '1/6'
#print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

#print("""You are lighter on the {0}, because on the {0} 
#... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
#print("""You are lighter on the {moon}, because on the {moon} 
#... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#print(f'On the Moon, you would weigh about {mass_percentage} of your weight on Earth')

round(100/6, 1)

print(f'On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth')

subject = 'interesting facts about the moon'

f'{subject.title()}'