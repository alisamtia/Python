user_data={}

name=input("Enter Your Name: ")
user_data['Name']=name

age=input("Enter Your Age: ")
user_data['Age']=int(age)

Movies=input("Enter Your Fav_Movies Coma Seprated: ").split(',')
user_data['Fav_Movies']=Movies

Songs=input("Enter Your Fav_Songs Coma Seprated: ").split(',')
user_data['Fav_Songs']=Songs

for i in user_data:
    print(f"{i} : {user_data[i]}")