import testOne

def mean_num_friends(x):
    x_length = len(x)
    aggregate = 0
    for num_friends in x:
        aggregate += num_friends

    return aggregate/x_length

def median_num_friends(x):
    x_length  = len(x)
    if x_length%2:
        ordered_list = sorted(x)
        return ordered_list[x_length//2]
    else:
        ordered_list = sorted(x)
        return (ordered_list[x_length // 2] + ordered_list[x_length//2 - 1])/2



num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))

print(testOne.addition_ifd(3))