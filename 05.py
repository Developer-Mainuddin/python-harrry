# #practise of 05 section
# my_dict = {
#     'tupi':'cap',
#     'boi':'book',
#     'bastu':'item'
# }
# print(my_dict['boi'])
# print('options are: \n',my_dict.keys())
# a=input("Please Enter the Bangla Word:\n")
# # print('The mening of your word is: ',my_dict[a])

# #Blew line will not through an error if the key is not preset in the dictionary
# print('The meaning of the word is ',my_dict.get(a))

# num1 = int(input("Enter number 1\n"))
# num2 = int(input("Enter number 2\n"))
# num3 = int(input("Enter number 3\n"))
# num4 = int(input("Enter number 4\n"))
# num5 = int(input("Enter number 5\n"))
# num6 = int(input("Enter number 6\n"))
# num7 = int(input("Enter number 7\n"))
# num8 = int(input("Enter number 8\n"))

# seet = {num1,num2,num3,num4,num5,num6,num7,num8}
# #set er vitora kono value repeate kora jai na

# print(seet)

# s= {18,18.0,'18'}
# print(s)
# print(len(s)) #aikhan e value 2 asar karon holo 18 and 18.0 ake e soman valu jodi oo data type alada

# s={}
# print(type(s)) #this is a dictionary
# s=set()
# print(type(s)) #this is set



# favLang = {}
# a = input('Enter your favaourite lnaguage MD:\n')
# b = input('Enter your favaourite lnaguage Mainuddin:\n')
# c = input('Enter your favaourite lnaguage Developer:\n')
# d = input('Enter your favaourite lnaguage Forhad:\n')
# favLang['MD'] =  a
# favLang['Mainuddin'] =  b
# favLang['MD'] =  c
# favLang['Forhad'] =  d
# print(favLang)


# s={1,2,3,[1,2,4,5]}
s={1,2,4,[10,20]}
s={1,2,4,(10,20)}

print(s)