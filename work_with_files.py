f = open("1.txt", "w")
f.write("Привет, мир")
f.close()

k = open("1.txt", "r")
print(k.read())
k.close()
