import pickle
dic = {'name': 'rxz','age': 29,'sex':'gils'}
print(type(dic))#<class ‘dict’>
j=pickle.dumps(dic)
print(type(j))#<class ‘bytes’>f=open(‘序列化对象_pickle’,‘wb’)#注意是w是写入str,wb是写入bytes,j是’bytes’
f.write(j) #-------------------等价于pickle.dump(dic,f)f.close()
 #-------------------------反序列化
import pickle
f=open('序列化对象_pickle','rb')
data=pickle.loads(f.read())
print(data['age'])
