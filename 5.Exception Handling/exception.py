#using else
try:
	a = 'a'
	v = int(a)
except:
	print("error occured")
else:
	print("no error")
#using finally
try:
	n = 20/10
except:
	print("catching division by 0 error")
finally:
	print("in finally block")
#cathcing perticular exceptoins
try:
	a = 'a'
	v = 20/10
	#v = int(a)
except ValueError:
	print("error occured")
else:
	print("no error")
#raising exceptions
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)	