# dictionaries intro
# Q - why we use dictionaries?
# A - Because of limitation of list are enough to represent
# real data.


# Example
user = ['Ali',12,['coco','kimi no na wa'], ['awakning','fairy tale']]
# this list contain user name, age, fav movies, fav tunes
# you can do this but this is not a good way to do this


# Q - what are dictionaries
# A - Unorderd collection of data in key : value pair.


# how to create dictionaries
user={'name' : 'Muhammad ali', 'age' : 12 }
# print(user['name'])
# print(type(user))

# seconf method to create dictionaries
user1 = dict(name='Muhamamd ali', age=12)
# print(user1['age'])

# how to access data form dictionaries 
# Note - There is no indexing becauese of unorderd collection of data
# print(user['name'])
# print(user['age'])

# which type of data a dictionary can store?
# anything
# numbers, strings, list, dictionaries

user_info={
    'name' : 'Muhammad ali',
    'age' : 12,
    'fav_cartoon' : ['miraculous lady bug','how to train your dragon'],
    'fav_tunes' : ['awakening','fail']
}
# print(user_info['fav_cartoon'])


user4 = {
    'hello' : {
    'name' : 'Muhammad ali',
    'age' : 12,
    'fav_cartoon' : ['miraculous lady bug','how to train your dragon'],
    'fav_tunes' : ['awakening','fail']}
}

# how to add data to empty dictionary
user_user={}
user_user['name'] = 'Muhammad ali'
user_user['age'] = 12

print(user_user)