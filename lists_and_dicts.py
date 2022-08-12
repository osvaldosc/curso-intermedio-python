def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "facundo", "lastname": "García"}

    super_list = [
        {"firstname": "facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "Integer_nums": [-1, -2, 0, 1, 2],
        "foating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, " ", value)

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])

    for i in super_list:
	    print(i.items())



if __name__ == '__main__':
    run()

