# 任意串字符拼接
s = 'qwefcxrlkjjiyytyevbgmnhhkld'
s1 = s.find('f')
s2 = s.find('r')
s3 = s.find('i')
s4 = s.find('e')
s5 = s.find('n')
s6 = s.find('d')

s11 = s[s1]
s22 = s[s2]
s33 = s[s3]
s44 = s[s4]
s55 = s[s5]
s66 = s[s6]


str = ''.join(s11+s22+s33+s44+s55+s66)

print(str)
