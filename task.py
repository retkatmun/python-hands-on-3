'''
meals = ["Gwote", "Masa", "Tuwon Acha", "Fura da Nono", "Kunu", "Miyan Kuka"]

meals.insert(4,"Miyan Taushe")
print(meals)

meals.remove(meals[1])
print(meals)

meals.remove(meals[3])
meals.append("Fura Da NOno")
print(meals)


meals = sorted(meals)
print(meals)

meals =len(meals)//2
print(meals)
'''

'''
#Question2 
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

genres.append("Drama")
print(genres)

genres.remove([3])
print(genres)

print(genres)

print(f" {genres[1]} {genres[-2]}")
'''

'''
#Question3

money = [1000,1200,800,110]

money.remove([2])
print(money)


money.insert(2,1000)
print(money)

money = money[::-1]
print(money)

print
'''

#Question4
courses = ["MTH 101", "PHY 101", "CHM 101", "CSC 101", "GST 101"]

courses.insert(0,"ENG")
print(courses)

#courses.remove([1-])
#print(courses)

courses.insert(2,"BIO 101")
print(courses)

courses = len(courses)
print(courses)


print(f"third course: {courses[2]}")
