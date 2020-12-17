import random, time, os

def generate_snow_line(width=70, max_density=5, char="❆"):
   snow_line = []
   snow_flakes = []
   for i in range(0, random.randint(1, max_density)):
      snow_flakes.append(random.randint(0, width))
   for i in range(0, width):
      if i in snow_flakes: 
         snow_line.append(char)
      else:
         snow_line.append(" ")
   return "".join(snow_line)

def generate_snow(lines=15, width=70, max_density=5, delay=0.1, char="❆"):
    snow = []
    while True:
        for i in range(0, lines):
            snow.insert(0, generate_snow_line(width, max_density, char))
            os.system("cls")
            for line in snow:
                print(line)
            time.sleep(delay)
            if len(snow) > lines:
                snow.pop(lines)
            
os.system("cls")
generate_snow(char="💩")