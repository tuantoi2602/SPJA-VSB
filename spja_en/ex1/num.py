def filter_numbers(*tup):
    fil = list(filter(lambda x: type(x) == int or type(x) == float, tup))
    fil.sort()
    return fil
print(filter_numbers(1.2, "sdas", 4, [12], 3.4, "12", -3, True, 5, 8.1))


def check_brackets(str):
    count = 0
    for i in str:
        if i == "(":
            count = count + 1
        elif i == ")":
            count = count - 1
        if count < 0:
            return False
    return count == 0
print(check_brackets("(a+b)/(b*(a+c))"))
print(check_brackets("(a+b))/((b*(a+c))"))
print(check_brackets("(a+b)/(b*(a+c)"))

def f(x):
    return x*(x-2)
def fun_extrems(function,a,b):
    arr =[]
    for i in range(a,b):
        arr.append(f(i))
    return min(arr)
print(fun_extrems(f,-5,5))

def number_of_vowels(string):
    vowels = 'aeiou'
    key = dict()
    bi = key.fromkeys(vowels,0)
    op = string.lower()

    for i in op:
        if i in bi:
            bi[i] += 1
    for i in vowels:
        if bi[i] == 0:
            bi.__delitem__(i)
    return bi
print(number_of_vowels(('Technical University')))




