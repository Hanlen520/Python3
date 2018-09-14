# 已知10以内 3,5的倍数和为23,实现100以内 3，5倍数的和

# 方法一:
sum= 0
for i in range(1,100):
    if i%3 == 0   or  i%5 == 0 :
        sum += (i);
print (sum)


# 方法二:
nums = []
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0 :
        nums.append(i)
# print (nums)
print (sum (nums))

# 方法三:列表表达式
print (sum( [i for i in range(1,10) if i%3 ==0 or i%5 ==0 ]))