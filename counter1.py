def freqnumber(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
          freq[item] += 1
        else:
           freq[item] = 1

    for key, value in freq.items():
        print("% s : % d" % (key, value))


my_fruit = '''
banana
apple
apple
peach
apple
banana
'''

if __name__ == "__main__":
    freqnumber(my_fruit.split())
