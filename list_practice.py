city = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", 
        "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(city)

subjects = ["math", "physics", "chemistry", "anatomy", "biology", "english"]
print(subjects)

print(subjects[-1])

print(city[2])
print(city[4])
print(subjects[3])
print(subjects[5])

print(city[0:2])
print(subjects[1:3])

city[0] = "San Francisco"
city[2] = "Brooklyn"
city[7] = "Hollywood"
city[5] = "Tampa"
print(city)

city.append("Oakland")
city.extend(["New York City", "Los Angeles"])
city.insert(0, "Miami")
print(city)

city.pop(2)
del city[4:6]
print(city)

