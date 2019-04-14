def add_new(ew, name, age, salary):
    this = {"name": name,
    "age": age,
    "salary": salary}
    ew.append(this)

def print_all(ew):
    for el in ew:
        print(el)

def salary_avg(ew):
    i = 0
    suma = 0
    for el in ew:
        i+=1
        suma += el["salary"]
    return round(suma / i, 2)

def salary_min_max(ew):
    salary_list = []
    for el in ew:
        salary_list.append(el["salary"])
    salary_list.sort()
    min = salary_list[0]
    max = salary_list[-1]
    return (min, max)    

ewidencja = []
add_new(ewidencja, "Abacki", 21, 7400)
add_new(ewidencja, "Babacki", 35, 4000)
add_new(ewidencja, "Cabacki", 60, 9200)

print_all(ewidencja)
avg = salary_avg(ewidencja)
print("Srednia pensja: ", avg)

mm = salary_min_max(ewidencja)
print("Minimalna pensja: ", mm[0])
print("Maksymalna pensja: ", mm[1])

