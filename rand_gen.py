import random
start = int (input("Start?"))
time = int(input ("Time?"))
interval = int(input("Interval?"))
ran_num = int(input("Number of range ?"))


limit = start+ time * interval -1
list1 = []
new_path = 'interval.txt'
new_interval = open(new_path,'w')

new_path = 'element.txt'
new_element = open(new_path,'w')

new_path = 'operation.txt'
new_operation = open(new_path,'w')

for i in range (time):
    innum =  start + i * interval
    new_interval.write(str (innum)+"\n" )
    for j in range( ran_num ):
        list1.append(random.randint(innum, innum + interval ))
        
        #print (list1[-1])

for i in range (time * ran_num):
    a , b = random.randint(0,time * interval -1),random.randint(0,  time * interval -1)
    #print(a,b);
    list1[a], list1[b] = list1[b] ,list1[a]

print ("------")
for i in list1:
    new_element.write( str (i) +"\n" )




print("Now range is " + str (start) + " to " +str( limit) )
print("Number of element is " + str (time * ran_num) )
del_num = int(input("How many numbers do you want to delete ?"))
del_ele = []
flag =  int (random.randint( 0 ,  interval ))
 
for i in range(del_num):
    del_ele.append (list1[flag] )
    print(int (limit/del_num))
    flag += int (limit/del_num)
    

flag = random.randint( 0 ,  interval )
j = 0 
for i in range ( len(list1)) :
    if  i == flag:
        new_operation.write( "delete "+str (del_ele[j]) +"\n" )
        j +=1
        flag +=  int (limit/del_num)
    new_operation.write( "insert "+str (list1[i]) +"\n" )
new_interval.close()
new_element.close()
new_operation.close()