def add_line_numbers():
    try:
        file = open("tex.txt","w")
        file.write("He was a Northern journalist,\n")
        file.write("and it was\n")
        file.write("in the interest of his paper")
        file = open("tex.txt", "r")
        n_file = open("n_" + "tex.txt", "w")
        num_line = 1
        for line in file:
            n_file.write(str(num_line)+ "   " + line)
            num_line += 1
    except IOError:
        print("No file")
add_line_numbers()

def your_lambda_function(func, number):
    arr = []
    for i in number:
        arr.append(func(i))
    return arr
def my_filtered_map(list,your_lambda_function, **minmax):
    list = [x for x in list if type(x) == int or type(x) == float]
    function = lambda x:x*2
    new_list = your_lambda_function(function, list)
    if "min" in minmax:
        new_list = [x for x in new_list if x >= minmax["min"]]
    if "max" in minmax:
        new_list = [x for x in new_list if x <= minmax["max"]]
        return new_list

print(my_filtered_map([1,2,3,"x",5,8,13], your_lambda_function, min=5, max=20))
print(my_filtered_map([True,-2.2,-1,0,1,2],your_lambda_function, max=0))


def bank_account(*filenames):
    accounts = {}
    f = []
    for file in filenames:
        f.append(open(file, 'r'))
    for i in f:
        for line in i:
            sl = line.split(" ")
            if sl[1] == 'D':
                if sl[0] in accounts:
                    accounts[sl[0]] += int(sl[2])
                else:
                    accounts.update({sl[0]: int(sl[2])})
            if sl[1] == 'W':
                if sl[0] in accounts:
                    accounts[sl[0]] -= int(sl[2])
                else:
                    accounts.update({sl[0]: -1 * int(sl[2])})
    return accounts
print(bank_account("bank_01.txt", "bank_02.txt"))