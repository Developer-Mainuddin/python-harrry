######### use open function or defination to read or wirte the content of a function or def  #########

# file=open('sample.txt','r')
# file=open('sample.txt') #by default the mode is r
# # data=file.read()
# data=file.read(5) # read(value) for read how many char you wanna to read from that file 
# print(data)
# file.close()
 


##########      radline method       ###########

# file=open('sample.txt')
# #read first line
# data=file.readline()
# print(data)

# #read second line
# data=file.readline()
# print(data)

# #read third line
# data=file.readline()
# print(data)

# #read fourth line and so on..........
# data=file.readline()
# print(data)
# file.close()


#########    file write kora       ###########

# file=open('sample.txt','w')
# file.write('I am writing\n')
# file.write('I am writing Second time\n')
# file.write('I am writing Third time\n')
# file.close()


######  file hisaba with open korbo ---open er alternative way--- ############
###### The best way to open and close the file automatically  #######
# with open('sample.txt','r') as file:
#     a=file.read()
# with open('sample.txt','w') as file:
#     a=file.write('Developer mainuddin')
# print(a)



######   ?????????? PRACTISE SET ????????? ##########

#||| PROBLEM 1 ||||||

# f=open('sample.txt')
# t=f.read()
# if 'TWINKLE' in t:
#     print("The poem is here!")
# else:
#     print("Missing the poem")
# f.close()


# ||||| PROBLE TWO |||||||


