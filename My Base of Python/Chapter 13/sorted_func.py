fruits=["Grapes","Banana","Mango","Apple"]
fruits.sort()
# print(fruits)

# We can't Apply it on tuples
fruits1=("Grapes","Banana","Mango","Apple")
# print(sorted(fruits1))

mobiles=[
    {'Model':'Vivo Y21','price':'34000'},
    {'Model':'Oppo A5S','price':'43000'},
    {'Model':'Hawae','price':'22000'},
    {'Model':'IPhone 14','price':'53000'},
]
name=sorted(mobiles, key=lambda item:item['price'],reverse=True) # We can reverse it by writing reverse=True
print(name)