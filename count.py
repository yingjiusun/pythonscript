def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% s : % d" % (key, value))

# Driver function
if __name__ == "__main__":

    #my_list =["apple", "pear", "peach", "apple", "apple", "peach"]:q!


    my_list = '''
    apple
    pear
    peach
    apple
    apple
    peach
    '''
    #CountFrequency(my_list)
    #CountFrequency(list(my_list.split("\r")))
    print(my_list.split())
    CountFrequency(my_list.split())