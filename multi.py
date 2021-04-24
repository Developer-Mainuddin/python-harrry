##################    Namta er table make kora   ##########################

# for i in range(2,21):
#         with open(f"tables/Multiplication_table_of{i}.txt",'w') as f:
#             for j in range(1,11):
#                 f.write(f"{i}x{j}={i*j}")
#                 if j!=10:
#                     f.write('\n')
       
            


####### nirdisto kono word ka remove kora ########

# words = ['outsourcing','inbox','dollar','freelancing','money','earning']

# with open("sample.txt") as f:
#     content =f.read()

# for word in words:
#     content = content.replace(word,'$%^#@^$%^&')
# with open("sample.txt",'w') as f:
#     f.write(content)

####### log file check kora ########

# with open('log.txt') as f:
#     content=f.read()

# if 'python' in content.lower():
#     print("Yes  python is present")
# else:
#     print("Python is not present here!")



####### Line number log file dia check kora ########

# content=True
# i=1

# with open('log.txt') as log_file:
#     while content:
#         content=log_file.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"python is here at line number {i}")
#         i+=1


####### File copy kora ########

# with open('copykorbo.txt') as f:
#     content=f.read()

# with open('paste.txt','w') as f:
#     f.write(content)


####### File er content ak e hola test kora ########


# with open('copykorbo.txt') as f1:
#     content1=f1.read()

# with open('paste.txt') as f2:
#     content2=f2.read()


# if(content1==content2):
#     print("files are same")
# else:
#     print("Not same")


####### kono file er sob content empty kora ########

# with open('sample.txt','w') as f:
#     f.write('')



#######        File ka rename kora      ########

# import os

# oldname='sample2.txt'
# new_name='renamed.txt'

# with open(oldname) as f:
#     content=f.read()

# with open(new_name,'w') as f:
#     f.write(content)

# os.remove(oldname)
