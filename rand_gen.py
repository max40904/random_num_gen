import random
start = int (input("Start?"))
time = int(input ("Time?"))
interval = int(input("Interval?"))
ran_num = int(input("Number of range ?"))
dep_flag = input("Allow deplicate  ?(y/n)")

limit = start+ time * interval -1
list1 = []
new_path = 'interval.txt'
new_interval = open(new_path,'w')

new_path = 'element.txt'
new_element = open(new_path,'w')

new_path = 'operation.txt'
new_operation = open(new_path,'w')
if dep_flag =='y':
    for i in range (time):
        innum =  start + i * interval
        new_interval.write(str (innum)+"\n" )
        rand_ori = []
        for j in range (interval):
            rand_ori.append( int(j)  )  

        for j in range( ran_num-1,-1 , -1 ):
            target = random.randint(0,j)
            
            temp = rand_ori[ target ]
            rand_ori[target] = rand_ori[j] 
            rand_ori[j] = temp
            print(j,target,temp)
            list1.append(innum+temp)
else:    
    for i in range (time):
        innum =  start + i * interval
        new_interval.write(str (innum)+"\n" )
        for j in range( ran_num ):
            list1.append(random.randint(innum, innum + interval ))
            

for i in range (time * ran_num):
    a , b = random.randint(0,time * ran_num -1), random.randint(0,time * ran_num -1)
    list1[a], list1[b] = list1[b] ,list1[a]

print ("------")
for i in list1:
    new_element.write( str (i) +"\n" )




print("Now range is " + str (start) + " to " +str( limit) )
print("Number of element is " + str (time * ran_num) )
del_num = int(input("How many numbers do you want to delete ?"))


del_ele = []
rand_ori = []
for j in range (time * ran_num):
    rand_ori.append( int(j)  )  
for j in range( 1,del_num+1,1 ):
    print(time * ran_num - j)
    num_loc = random.randint(0,time * ran_num - j )
            
    temp = rand_ori[ num_loc ]
    rand_ori[num_loc] = rand_ori[time * ran_num - j] 
    rand_ori[time * ran_num - j] = temp
    del_ele.append(temp)
del_ele.sort()
print(del_ele)
    
use_ele = []
flag = random.randint( 0 ,  interval )
j = 0 
for i in range ( len(list1)) :
    new_operation.write( "insert "+str (list1[i]) +"\n" )
    use_ele.append (list1[i])
    if  j <del_num and i ==  del_ele[j] :
        index = random.randint(0, len(use_ele))
        new_operation.write( "delete "+str (use_ele[index]) +"\n" )
        del use_ele[index]
        j +=1
        
       
    
new_interval.close()
new_element.close()
new_operation.close()