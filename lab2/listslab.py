
#def listsfun():
	#list1=[5, 10, 15, 20, 25]
	#list2=[list1[0]] + [list1[-1]]
	#print(list2) 
#listsfun()
#a=[1,1,2,3,5,8,13,21,34,55,89]	
#for i in range(len(a)):
    #if a[i]<5:
       #print(a[i])       

def listsfun1():
   a=[1,1,2,3,5,8,13,21,34,55,89]
   b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
   for i in a:
	   for j in b:
		   if i==j:
		     print i
listsfun1()			
