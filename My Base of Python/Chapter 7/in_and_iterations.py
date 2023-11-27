# in keyword and iteration in dectionary

user_info = {
    'name' : 'Harshit',
    'age' : 24,
    'fav_movie' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale']
}

# check if key exist in dictionary
if 'name' in user_info:
    print('present')
else:
    print('Not Present')

# Check if value in dictionary
if 24 in user_info.values():
    print('present')
else:
    print('Not Present')

# Looping in DIctionary
# for i in user_info.values():
#     print(i)

# for i in user_info:
#     print(user_info[i])

# Values Method
# print(user_info.values())
# print(type(user_info.values()))

# keys method
# print(user_info.keys())
# print(type(user_info.keys()))

for key, value in user_info.items():
    print(f"Key is {key} and Value is {value}")