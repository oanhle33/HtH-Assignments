cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", 
        "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cities)

subjects = ["math", "physics", "chemistry", "anatomy", "biology", "english"]
print(subjects)

print(subjects[-1])

print(cities[2])
print(cities[4])
print(subjects[3])
print(subjects[5])

print(cities[0:2])
print(subjects[1:3])

cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"
print(cities)

cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0, "Miami")
print(cities)

cities.pop(2)
del cities[4:6]
print(cities)



def print_city(list):
        for el in list:
                print(el)
        return "All cities printed"
print(print_city(cities))

def reorganize_list(list):
        print(cities)
        count = 0
        while count < len(list):
                item1 = list[count] 
                item2 = list[count + 1]

                if len(item1) >= len(item2):
                        count += 1
                        continue
                elif count + 1 == len(list) - 1:
                        break
                else:
                        list.remove(item1)
                        list.append(item1)
                        count += 1
        return list
print(reorganize_list(cities))

def print_city(list):
        for el in list:
                print(el)
        return "All subjects printed"
print(print_city(subjects))

def sort_list(list):
        return sorted(list)
print(sort_list(subjects))



