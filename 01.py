# Harry python

# from playsound import playsound
# playsound('G:\\Python with harry\\096-al-alaq.mp3')

# import os
# print(os.listdir())

# b='Mainuddin'
# #-9,-8,-7,-6,-5,-4,-3,-2,-1  (-index)       
# print(b[-4:-1])

#practise 3

# # string skipping
# x = '''forhadisGood'''
# print(x[0::3])# aikan e index 0 thaka last porjonto selected kora hoyasa and third argument hisba koto ta er nic porjonto skipp kora hoba tar argument pass kora hoiyasa



# story = 'forhad is an web application developer ma'
# String functins
# print(len(story))
# print(story.endswith('an'))
# print(story.count('ma'))
# print(story.capitalize())
# print(story.find('web'))
# print(story.replace('forhad','mr forhad'))

# x = "harry is good \nhe\tis very g\\ood"
# print(x)

# name = input('Enter your name\n')
# print('Good night,'+ name)

# letter='''Dear <|Name|>,
# You are selected!
# Grettings from abm coding house.I am happy to tell  you about your selection
# You are selected
# Thanks and regards 
# Bill
# Date: <|Date|>
# '''
# name=input("Enter your Name\n")
# date=input("Enter Date\n")
# letter = letter.replace('<|Name|>',name)
# letter = letter.replace('<|Date|>',date)
# print(letter)

# st="this is a double    space"
# # doublespace = st.find('  ')
# # print(doublespace)
# st = st.replace('  ',' ')
# print(st)
# formattedLetter = 'dear mainuddin\n\tthis is nice training!\nThanks!'
# print(formattedLetter)

# l=[0,10,20,50]
# print(l[0:4])
# print(l[-4:])
# l.sort()
# l.reverse()
# l.append(100000)  # add in the end this element
# l.append(200000)
# l.insert(3,22) # 22 ka add kora hoisa 3 number index e
# l.pop(1) # remove elements at index 1
# l.remove(50) #50 ka remove kora hoisa list thaka
# print(list)

# t = (1,2,3,4,5,6,1,5,5)
# t[0]=34 #throw an errro
# print(t)
# t1= (1,)
# print(t1)
# print(t.count(5))
# print(t.index(2)) #2 asa index 1 e

# f1 = input('Enter fruit number 1\n')
# f2 = input('Enter fruit number 2\n')
# f3 = input('Enter fruit number 3\n')
# f4 = input('Enter fruit number 4\n')
# f5 = input('Enter fruit number 5\n')
# f6 = input('Enter fruit number 6\n')
# f7 = input('Enter fruit number 7\n')
# myFruitsList=[f1,f2,f3,f4,f5,f6,f7]
# print(myFruitsList)
# m1 = float(input('Enter Marks for all Student number 1\n'))
# m2 = float(input('Enter Marks for all Student number 2\n'))
# m3 = float(input('Enter Marks for all Student number 3\n'))
# m4 = float(input('Enter Marks for all Student number 4\n'))
# m5 = float(input('Enter Marks for all Student number 5\n'))
# m6 = float(input('Enter Marks for all Student number 6\n'))
# m7 = float(input('Enter Marks for all Student number 7\n'))

# marksList =[m1,m2,m3,m4,m5,m6,m7]
# marksList.sort()
# print(marksList)

# a=[10,50,30,10]
# # print(a[0]+a[1]+a[2]+a[3])
# # print(sum(a))
# print(a.count(10))
# print(a.index(50))


# Chapter: 5 Dictinary

# myDict = {
#     "Fast":'a quick manner',
#     "mainuddin":"A Programmer",
#     "Marks":[1,2,3,5],
#     "anotherDict0":{"harry":"player","forhad":"gamer"}
# }
# # print(myDict['mainuddin'])
# myDict["Marks"]=[100,500,700,200]
# print(myDict['Marks'])
# # print(myDict['anotherDict0']["forhad"])

# Methods of dictionary

# myDict = {
#     "Fast":'a quick manner',
#     "mainuddin":"A Programmer",
#     "Marks":[1,2,3,5],
#     "anotherDict0":{"harry":"player","forhad":"gamer"},
#     1:2
# }
# print(myDict.keys())
# print(type(myDict.keys()))
# print(list(myDict.keys()))
# print(type(list(myDict.keys())))

# print(myDict.values())
# print(type(myDict['anotherDict0']))
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items()) #print the value and keys for all contents of a dictionary

# myDict = {
#     "Fast":'a quick manner',
#     "mainuddin":"A Programmer",
#     "Marks":[1,2,3,5],
#     "anotherDict0":{"harry":"player","forhad":"gamer"},
#     1:2
# }

# print(myDict.get('mainuddin2'))#through none for get method
# print(myDict['mainuddin2'])

# # updateDict = {
# #     'developer':"Md Mainuddin",
# #      'freelance':"Mainuddin",
# #     "mainuddin":"A Dancer",

# # }
# # myDict.update(updateDict)
# # print(myDict)

# tel={'jack': 4098, 'sape': 4139, 'guido': 4127}
# del tel['sape']
# tel['onwner'] = 'Developer Mainuddin'
# print(tel)

# SETS IN PYTHON

# seet ={ 1,2,3,4,1,2}
# print(seet)

#its make a empty dictionary not empty set
# a={}
# print(type(a))

# create empty set by this syntex
emptyset=set()
# print(type(emptyset))
#set er item change kora jai na &&& duplicate oo kora jai na
emptyset.add(4)
emptyset.add(1)
emptyset.add(3)
emptyset.add(3)
emptyset.add(3)
emptyset.add(0)
# emptyset.add([10,20])
#ai khan e set er vitora list rakah jai na jahatu aita changeable
# emptyset.add({'name':'mdmainuddin',4:'fourth Class'}) #aikhan e set er vitora dictionary raka jai na jahatur aita changeable

emptyset.add((10,20,30)) #aikhan e set er vitora tuple rakha jai

#set er value repeate kora jai na
print(emptyset) #aikhan e .add() method use korai sorted akara sajano asa
# b = {0,50,20,10,80,5,55}
# print(b)
# print(type(b)
# print(len(emptyset))
# emptyset.remove(1)
# print(emptyset)
# print(emptyset.pop())
# print(emptyset)

# emptyset.clear() #pura set ka clear kora day
# print(emptyset)

# print(emptyset.union({8,10}))
# print(emptyset.intersection({88,110}))

