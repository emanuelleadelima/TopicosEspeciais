#Capítulo 3 - Funções
#3.1 - Chamadas de função

#3.1.1
print(type(42))
print("\n")

#3.1.2
print(int('32'))
print("\n")

#3.1.3
print(int(3.99999))
print("\n")

#3.1.4
print(int(-2.3))
print("\n")

#3.1.5
print(float(32))
print("\n")

#3.1.6
print(float('3.14159'))
print("\n")

#3.1.7
print(str(32))
print("\n")

#3.1.8
print(str(3.14159))
print("\n")

#3.2 - Funções matemáticas

#3.2.1
import math
signal_power = 100
noise_power = 27
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)
print(ratio)
print("\n")
print(decibels)
print("\n")
print(height)
print("\n")

#3.2.2
degrees = 45
radians = degrees / 180.0 * math.pi
print(math.sin(radians))
print("\n")

#3.2.3
print(math.sqrt(2) / 2.0)
print("\n")

#3.3 - Composição

#3.3.1
x = math.sin(degrees / 360.0 * 2 * math.pi)
print(x)
print("\n")
y = math.exp(math.log(x+1))
print(y)
print("\n")

#3.3.2
hours = 72
minutes = hours * 60
print(minutes)
print("\n")

#3.4 - Como acrescentar novas funções

#3.4.1
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
print_lyrics()
print("\n")

#3.4.2
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()
print("\n")

#3.5 - Uso e definições

#3.5.1
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
print("\n")

#3.7 - Parâmetros e argumentos

#3.7.1
def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice("xoxo, gossip girl")
print("\n")

#3.7.2
print_twice("Love you" * 4)
print_twice(math.cos(math.pi))
print("\n")

#3.7.3
michael = "Eric, the half a bee."
print_twice(michael)
print("\n")

#3.8 - As variáveis e os parâmetros são locais

#3.8.1
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
line1 = 'Ó pinheirinho de Natal, '
line2 = 'que lindos são seus ramos!'
cat_twice(line1, line2)
print("\n")

#3.10 - Funções com resultado e funções nulas

#3.10.1
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
print(x)
print("\n")
print(golden)
print("\n")

#3.10.2
print(math.sqrt(5))
print("\n")

#3.10.3
result = print_twice('Bing')
print(result)
print("\n")

#3.10.4
print(type(None))
print("\n")

#3.14 - Exercícios

#3.14.1
def right_justify(s):
	spaces = ""
	newSpaces = (70 - len(s)) * " "
	ideal = newSpaces+s
	print(ideal)
	print(len(ideal))
right_justify("monty")
print("\n")

#3.14.3
def grade():
	print("uma grade 11x11 :) \n")
	i = 0
	while i<11:
		if i == 0 or i == 5 or i==10:
			print("+ - - - - + - - - - +")
			i+=1
		elif (i>0 and i<5) or (i>5 and i<10):
			print("|         |         |")
			i+=1
		else:
			break
grade()
print("\n")

def grade2():
	print("uma grade 4x4 :) \n")
	x = 0
	while x<4:
		if x == 0 or x ==3 :
			print("+ - - +")
			x+=1
		elif x>0 and x<3:
			print("|     |")
			x+=1
		else:
			pass
grade2()
print("\n")
