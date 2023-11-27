# fromkeys
# d={'name' : 'unknown', 'age' : 'Unknown', 'Height' : 'Unknown'}

d=dict.fromkeys(['name', 'age', 'Height'], 'Unknown')
# d=dict.fromkeys(('name', 'age', 'Height'), 'Unknown')
# d=dict.fromkeys('abc', 'Unknown')
# d=dict.fromkeys(range(1,11), 'Unknown')
# d=dict.fromkeys(['name', 'age', 'Height'], ['Unknown','Unknown'])
# print(d)

# Get Method
s={'name' : 'ali', 'age' : 12, 'Height' : '30'}
# print(s['name'])

# print(s.get('names')) # Better

# if 'name' in s:
#     print('Present')
# else:
#     print('Not Present')

# if s.get('names'):
#     print('Present')
# else:
#     print('Not Present')

# if None ------> Else False -----> True

# s.clear()
# print(s)


# copy
s1 = s.copy
s1=s # 1 Dictoniary

# print(s1 is s)