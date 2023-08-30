import random


def random_id_generator():
    random_id = random.randint(1, 9999)
    yield random_id




def random_city_generator():
    city_list = ['Kormangala', 'HSR Layout', 'Ballary', 'Mumbai', 'Chennai', 'Nellore', 'Gurgon', 'Hyderabad']
    random_city = random.choice(city_list)
    yield random_city


def random_salary_generator():
    random_salary = random.randint(20000,1500001)
    yield random_salary


num_of_employee = int(input("Enter the number of employee details you want to generate: "))
for j in range(num_of_employee):
    #gen = my_generator()
    print(f"------------------------Employee Detail {j+1}------------------------")
    print("Employee ID:",next(random_id_generator()))
    print("Employee city:",next(random_city_generator()))
    print("Employee salary",next(random_salary_generator()))


















