'''
Heroes beta-0.1
author
str map  if  while
2018-07-20
'''
import  random

print("|","--"*30,"|")
welcome = "welcome to  KMF !!!"
mapmsg = '#######'
mapins = " ---the KMF is like this---\n %s \n the '*'is you" %(mapmsg,)
map = ['#','#','#','#','#','#','#']
instruction = '''  \ncontrl you :'a'for left ; 'd' for right ; 'q' for quit
 '''
print(welcome)
name = input("请输入用户名:")

growScore = 50
usermsg = {'name':name,'growScore':growScore}

def apple(growScore):
    growScore += 10
    return growScore
def bomb(growScore):
    growScore -= 10
    return growScore

evenlist = [apple,bomb]

# 判断name的值是否为空
if not name :
    print("你的用户名为:KMF_001" ";" "你的成长值为:%d"%usermsg['growScore'])
else:
    print("你的用户名为:%s" %usermsg['name'] , ";" "你的成长值为:%d" %usermsg['growScore'])
# print("你的成长值为:%d" %usermsg[1])
# print("你的成长值为:%d" %growScore)

print(mapins,instruction)

point = 0
while 1:
    map[point] = '*'
    print('you are here',"".join(map))
    userinput = input("请输入操作指令:")
    if userinput == 'd' and point < 6:
        map[point] = '#'
        point += 1
        usermsg['growScore'] = random.choice(evenlist)(usermsg['growScore'])
        print(usermsg['growScore'])
    elif userinput == 'a' and point > 0:
        map[point] = '#'
        point -= 1
        usermsg['growScore'] = random.choice(evenlist)(usermsg['growScore'])
        print(usermsg['growScore'])
    elif  userinput == 'q':
        print("bye!!!")
        break
    else:
        print(instruction)
    # if point == 3:
    #     usermsg['growScore'] = apple(usermsg['growScore'])
    #     print('growScore is: %s' % (usermsg['growScore'],))
    # if point == 4:
    #     usermsg['growScore'] = bomb(usermsg['growScore'])
    #     print('growScore is: %s' % (usermsg['growScore']))