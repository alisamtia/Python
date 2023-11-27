# add and delete data

user_info = {
    'name' : 'Muhammad ali',
    'age' : 12,
    'fav_movies' : 'Avengers',
    'fav_cartoon' : 'Lady Bug',
}

# change data
# user_info['fav_movies'] = 'Zomabies'
# print(user_info)


# Pop Method
# user_info.pop('fav_movies')
# print(user_info)


# popped item method
popped_item = user_info.popitem()
print(popped_item)
