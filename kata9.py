# Defino mi función
#def rocket_parts():
    #print('payload, propellant, structure')

# Llamo a mi función

     #rocket_parts()
     #'payload, propellant, structure'

#para devolver la cadena en lugar de imprimirla hace que la variable output tenga un valor distinto:

#def rocket_parts():
 #   return 'payload, propellant, structure'
...
#output = rocket_parts()
#output
#'payload, propellant, structure'

#Traceback (most recent call last):
 #        File '<stdin>', line 1, in <module>
  #       TypeError: any() takes exactly one argument (0 given)

#def distance_from_earth(destination):
#    if destination == 'Moon':
 #       return '238,855'
 #   else:
 #       return 'Unable to compute to that destination'
#distance_from_earth()
#distance_from_earth('Saturn')

#def days_to_complete(distance, speed):
#    hours = distance/speed
#    return hours/24
#days_to_complete(238855, 75)

#Combinación de argumentos y argumentos de palabra clave
#from datetime import timedelta, datetime

#def arrival_time(destination, hours=51):
 #   now = datetime.now()
  #  arrival = now + timedelta(hours=hours)
 #   return arrival.strftime(f'{destination} Arrival: %A %H:%M')
 #arrival_time()
#arrival_time('Moon')   
#arrival_time('Orbit', hours=0.13)

#KWARGS
def variable_length(**kwargs):
    print(kwargs)

    variable_length(tanks=1, day='Wednesday', pilots=3)