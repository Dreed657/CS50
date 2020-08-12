people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# Python
people.sort(key=lambda person: person["name"])
print(people)

# C#
people.OrderBy(x => x.Name);
people.ForEach(x => Console.WriteLine(x.Name));