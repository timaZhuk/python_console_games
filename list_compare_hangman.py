# ----------------------------------my version of arrays and words finding-------------------------------------------
def printList(word):
    # 1 word traslate to list

    word_arr = []
    for i in word:
        word_arr.append(i)
    # print(word_arr)
    # 2 .insert our letter in new list that contains '-'
    word_letters = set(word)

    def inner_fun(letter):
        word_list1 = ['-'] * len(word)

        # print(word_list1)
        for sym in word_arr:
            if sym == letter:
                index = word_arr.index(letter)
                word_list1.pop(index)
                word_list1.insert(index, letter)
                word_arr.pop(index)
                word_arr.insert(index, 0)
        return word_list1

    return inner_fun


hangman()
# user_input = input('Type something: ')
# print(user_input)
'''
fun=printList("rowrow")
arr_r=fun("r")
#print(arr_r)
arr_w=fun("w")
#print(arr_w)
arr_o=fun("o")

'''


def compareArr(arr1, arr2):
    new_arr = []
    if len(arr1) == len(arr2):
        for i in range(0, len(arr1)):
            if arr1[i] != '_' and arr2[i] == '-':
                arr2[i] = arr1[i]
    print(arr2)
    return arr2


'''
arr_wr=compareArr(arr_r, arr_w)
#print(compareArr(arr_r, arr_w))
full_arr=compareArr(arr_o,arr_wr)
print(''.join(full_arr))

'''

'''
def printList(word):
    # 1 word traslate to list
    word_arr=[]
    for i in word:
        word_arr.append(i)
    print(word_arr)
    # 2 .insert our letter in new list that contains '-'
    word_letters = set(word)
    def inner_fun(letter):

         word_list1 = ['-']*len(word)

         # print(word_list1)
         for sym in word_arr:
            if sym == letter:
                index=word_arr.index(letter)
                word_list1.pop(index)
                word_list1.insert(index,letter)
                word_arr.pop(index)
                word_arr.insert(index,0)
         return word_list1
    return inner_fun


fun=printList("rowrrqwrr")
print(fun("r"))
result:   
['r', 'o', 'w', 'r', 'r', 'q', 'w', 'r', 'r']
['r', '-', '-', 'r', 'r', '-', '-', 'r', 'r']   


#good but not i want 
def printList(word):
    word_letters = set(word)
    def inner_fun(letter):
        for symbl in word:
            word_list1 = ['-' for symbl in word]
            if letter in word:
                word_list1.insert(word.index(letter),letter)
        return word_list1
    return inner_fun


'''