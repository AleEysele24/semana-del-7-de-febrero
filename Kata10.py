#def main():
#   open("/path/to/mars.jpg")

#def main():
#    try:
 #       configuration = open('config.txt')
 #   except FileNotFoundError:
 #       print("Couldn't find the config.txt file!")


#if __name__ == '__main__':
#    main()

#python config.py

#      File "/tmp/config.py", line 9, in <module>
#     main()
#    File "/tmp/config.py", line 3, in main

#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#   except IsADirectoryError:
 #       print("Found config.txt but it is a directory, couldn't read it")

##agrupar las excepciones como una usando paréntesis en la línea except
#def main():
#    try:
#        configuration = open('config.txt')
 #   except FileNotFoundError:
  #      print("Couldn't find the config.txt file!")
  #  except IsADirectoryError:
 #       print("Found config.txt but it is a directory, couldn't read it")
 #   except (BlockingIOError, TimeoutError):
 #       print("Filesystem under heavy load, can't complete reading configuration file")
    
#open("config.txt")
#     except OSError as err:
#      if err.errno == 2:
#  print("Couldn't find the config.txt file!")
#elif err.errno == 13:
#    print("Found config.txt but couldn't read it")

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"