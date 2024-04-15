# Exception handling during file manipulation
f = open('myfile.txt')
try:
	print(f.read())
except:
	print("Something went wrong")
finally:
	f. close()