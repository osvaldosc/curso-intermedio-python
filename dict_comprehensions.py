from cProfile import run


def run():
    
    # my_dict = {}
    # for i in range(1, 101):
    #     my_dict[i] = i**3
    # print(my_dict)    

    # my_dict = {}
    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**3
    # print(my_dict)
    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 !=0}
    # print(my_dict)

    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 !=0}
    # print(my_dict)
    
    dictionary = {num: num**0.5 for num in range(1, 1001) if num % num**0.5 ==0}
    for num, sqrt in dictionary.items():
        print(f'La raiz cuadrada de {num:5}   es {sqrt:5}')
if __name__ == '__main__':
    run()
