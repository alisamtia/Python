number=[1,2,3,4,5,6,7]
# print(max(number))

# def func(item):
#     return len(item)

names=["Ali","Alian","Zaroon","Ibrahim"]
# print(max(names,key=lambda item:len(item)))
# print(max(names,key=func))

student=[
    {'name':'Muhammmad Ali','age':12,'Score':70},
    {'name':'Muhammmad Alian','age':11,'Score':97},
    {'name':'Muhammmad Zaroon','age':7,'Score':75},
    {'name':'Ibrahim','age':3,'Score':20},
]

student2={
    'Muhammmad Ali':{'age':12,'Score':70},
    'Muhammmad Alian':{'age':11,'Score':97},
    'Muhammmad Zaroon':{'age':7,'Score':75},
    'Ibrahim':{'age':3,'Score':20},
}

# print(min(student, key=lambda item:item.get('Score'))['name'])
# print(max(student2,key=lambda item:student2[item]['age']))