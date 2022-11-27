import random
from words import words
import string #import letters in alphabet

def get_valid_word(words):
    word = random.choice(words)  #randomly chooses somthing from the list
    while '_' in word or ' ' in word: #exclude the words with '_' and ' '
        word = random.choice(words)
    return word.upper() # return word -->WORD in upper case

#print(get_valid_word(words))

def hangman():
    word = get_valid_word(words) # guessed word
    word_letters = set(word) #letters in the word saved
    alphabet = set(string.ascii_uppercase) #english alphabet
    used_letters = set() #what the user has guess

    lives = 7
    #getting user input
    while len(word_letters) > 0 and lives > 0: #while set.lengh not 0
        #' '.join(['a', 'b', 'cd'])--> 'a b cd'  return the string separated by sign = '' befor join() from list
        print('You have used these letters: ', ' '.join(used_letters))
        # what current word is (ie W - R)
        print(word)
        print(word_letters)
        # word_list1 = ['-' for letter in word]
        # print(word_list1)


        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #word_list = [letter if letter in word_letters else '-' for letter in word]
        #print _ _ d _ _s in this way sytings5

        user_letter = input('Guess a letter: ').upper() #enter letter in Upper case
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # we delete inserted letter from Set-word_letter
                # condition for while loop
            else:
                lives = lives - 1
                print(f"You have {lives} lives!")

        elif user_letter in used_letters:
            print("Try again. You have already used that character((.")

        else:
            print("It is not wright letter or Invalid character!")
    #we get there when len(word_letters) == 0
    if lives ==0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"You guessed word: {wor}. OOOYYYOUU!!!!")


#----------------------------------my version of arrays and words finding-------------------------------------------
def printList(word):
    # 1 word traslate to list

    word_arr=[]
    for i in word:
        word_arr.append(i)
    #print(word_arr)
    # 2 .insert our letter in new list that contains '-'
    word_letters = set(word)
    def inner_fun(letter):
         word_list1 = ['-'] * len(word)

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
    new_arr=[]
    if len(arr1) == len(arr2):
        for i in range(0, len(arr1)):
            if arr1[i]!='_' and arr2[i]=='-':
                arr2[i]=arr1[i]
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