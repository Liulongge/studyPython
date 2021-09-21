f = open("D:\\myCode\\python\\test.txt","r")
#print(f.read(-1))
print(f.read(1))

print(list(f.read(-1)))
f.close()

f = open("D:\\myCode\\python\\test.txt","a+")
f.write("Hello world\n")
f.close()
f = open("D:\\myCode\\python\\test.txt","r")
print(f.read(-1))
f.close()
