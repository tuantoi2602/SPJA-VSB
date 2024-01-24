def search(key, my_list):
    for element in my_list:
        if element == key:
            return True
    return False

def create(my_file):
    f1 = open(my_file, "rt")
    my_list = []
    my_list_key = []

    for line in f1:
        list = line.rstrip().split()
        my_list.append(list)
        key = list[0]
        if Searching(key, my_list_key) == False:
            my_list_key.append(key)

    return my_list, my_list_key

def convert(duration):
	minutes = float(duration.split(':')[0])
	seconds = float(duration.split(':')[1])
	return minutes, seconds

def check(phone):
	if phone[0:2] == '00':
		return True
	return False

def compute(my_list, my_list_key):
	list_prices = []
	for key in my_list_key:
		sum = 0.0
		for calls_realized in my_list:
			if calls_realized[0] == key:
				if Check_internal_calls(calls_realized[1]) == True:
					minutes, seconds = Convert_duration(calls_realized[2])
					if seconds != 0:
						prices = minutes * 1.5 + 1.5
					else:
						prices = minutes * 1.5
					sum += prices
		list_prices.append(sum)
	return list_prices

def main():
	my_list, my_list_key = Create_list("calls.txt")
	list_prices = Computing(my_list, my_list_key)
	i = 0
	while(i<len(my_list_key)):
		print("%s: %r CZK" % (my_list_key[i], list_prices[i]))
		i += 1
main()