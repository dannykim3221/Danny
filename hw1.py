def get_radius(prompt):
    r = int(input(prompt))
    #print(f"반지름 {r}인 원의 넓이 = 3.14 * {r} * {r} = {3.14 * r * r} ")
    return r

def get_circle_area(r):
    area = 3.14 * r * r
    return area

prompt = "넓이를 구하고자 하는 원의 반지름은? "
radius = get_radius(prompt)
area = get_circle_area(radius)
print("반지름", radius, "인 원의 넓이 = 3.14 *", radius, "*", radius, "=", area)


#get_radius("넓이를 구하고자 하는 원의 반지름은? ")
