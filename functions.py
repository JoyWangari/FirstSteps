
def add(a,b):
    if type(a) and type(b)== int or type(a) and type(b)== float :
        print a + b
    else:
        print 'invalid'

add(2,3)
add(8.8,9.6)
add('car','jane')
add(8,'mike')

def funky(a,b):
	if type(a) and type(b) == dict:
		print "Cant add dictionaries"
	else:
		print a + b
funky(1,1.2)
funky([1,2,3],[2,3,4])
funky("toni",1)
funky("toni","joy")
funky({1:"mangoes", 2:"apples"},{3:"pears",4:"oranges"})