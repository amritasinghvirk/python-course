# f(x,y) = x**2-4*y 

def extract_first_last_names(email):

    first_name = email.split(".", 1)[0]
    last_name = email.split(".", 1)[1].split("@", 1)[0]

    return first_name, last_name


print(extract_first_last_names("renuka.singh@epfl.ch"))

first, last = extract_first_last_names("renuka.singh@epfl.ch")


print(f"First: {first}")

print(f"Last: {last}")