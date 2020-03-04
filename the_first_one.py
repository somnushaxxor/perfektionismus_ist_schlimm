try:
	def decorator(fun):
		def wrapper(arg1,arg2,arg3):
			print(fun(arg1,arg2,arg3))
			print(v0*t + (fun(arg1,arg2,arg3)*t**2)/2)
		return wrapper

	v0 = int(input())
	v1 = int(input())
	t = int(input())

	def acceleration(v0,v1,t):
		return((v1-v0)/t)
			
	acceleration = decorator(acceleration)
	acceleration(v0,v1,t)
except ValueError:
	print('Нельзя вводить строки')
except ZeroDivisionError:
	print('t не может быть равно 0')