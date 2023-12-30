'''

File: rhymes.py
Author: Randall Candaso
Course/Section: CSC 120-002
Purpose: This program takes both an inputted word and an inputted 
dictionary, determining which words in the dictionary rhyme with
the inputted one. This is determined by the splitting of syllables/
pronunciations of all the words contained in the dictionary.

'''

def main():
    
    pfile = input()
    word = input()
    new_word = word.upper()
    new_dict = create_dict(pfile)
    sounds, check = determine(new_word, new_dict)
    rhymes = find_similar(sounds, check, new_dict)
    print_out(rhymes, word)

def print_out(rhymes, word):
    '''
    
    Now that the words that rhyme are placed into a dictionary, they are taken
    by the program, sorted, and printed out as many times as they were 
    determined to have rhymed with the original word.
    
    Parameter: rhymes - dictionary containing the words that rhymed and how 
    many times they rhymed
    word - the originally inputted word

    '''
    empty = []
    for i in rhymes:
        index = 0
        while index < rhymes[i]:
            if i != word.upper():
                empty.append(i)
            index += 1
    now_sorted = sorted(empty)
    for i in now_sorted:
        print(i)

def create_dict(file):
    '''
    
    Takes the inputted dictionary file and reads it into the program. Then,
    the words and their pronunciations are created into the program's own
    dictionary.

    Parameter: file - the inputted dictionary file

    Return: the program's own created dictionary
    
    '''
    ready = open(file, 'r')
    empty_dict = {}
    for i in ready:
        splitting = i.split()
        if splitting[0] not in empty_dict:      
            starter = []
            starter.append(splitting[1:])
            empty_dict[splitting[0]] = starter
        else:
            empty_dict[splitting[0]].append(splitting[1:])
    return empty_dict

def determine(word, dictionary):
    '''
    
    Takes the inputted word and determines which part of the pronunciation 
    should be used in determining the other words that rhyme with it.

    Parameters: word - the inputted word by the user
    dictionary - the created dictionary all the words and their 
    pronunciations

    Return: two lists of syllables that will be used to determine which
    words rhyme with the inputted one
    
    '''
    new_dict = {}
    if word in dictionary:
        empty = dictionary[word]
        new_dict[word] = empty
    selected = []
    selected_2 = []
    for i in new_dict:
        for j in new_dict[i]:
            outer = 0      # Extra outer loop created so the inner loop
            count = 0      # can reset if no 1 value is found, causing it 
            index = 0      # to look for 0's afterwards
            while outer < 1:                
                while index < len(j):      
                    if '1' in j[index]:    
                        check = index - 1
                        selected.append(j[index:])        
                        selected_2.append(j[check:])    
                        count += 1                      
                        index = len(j)
                    index += 1          # a 'check' list is created to
                if count == 1:          # to determine the syllable
                    outer = 2           # proceeding the primary one
                else:
                    while index < len(j):
                        if '0' in j[index]:
                            check = index - 1
                            selected.append(j[index:])
                            selected_2.append(j[check:])
                            count += 1
                            index = len(j)
                        index += 1
                outer += 1
    return selected, selected_2

def find_similar(sound, check, dictionary):
    '''
    Using the syllables determined in the previous function, the
    program runs through the whole dictionary and determines which
    words rhyme with the orignally inputted word.

    Parameters: sound - list of pronunciations of the inputted word
    check - a list created to help differentiate words that actually
    rhyme and words that are too similar to the original
    dictionary - the created dictionary all the words and their 
    pronunciations

    Return: a dictionary of words that rhyme with the inputted word 
    and how many times they rhyme with the different number of 
    pronunciations
    
    '''
    temporary = {}
    for i in dictionary:
        for index in dictionary[i]:
            z = 0       # Extra outer loop created so the inner loop 
            outer = 0   # can reset if no 1 value is found, causing it         
            count = 0   # to look for 0's afterwards        
            while outer < 1:                        
                while z < len(index):                   
                    if '1' in index[z]:                 
                        for item in range(len(sound)):
                            if index[z:] == sound[item]:             
                                before = z - 1                      
                                if index[before:] != check[item]:    
                                    if i not in temporary:          
                                        temporary[i] = 1
                                        count += 1
                                    elif i in temporary:
                                        temporary[i] += 1
                                        count += 1
                        if count > 1:
                            z = len(index)
                    z += 1               # Function also checks if the
                if count == 3:           # syllable before in each word
                    outer = 1            # matches too simarly to the
                while z < len(index):    # syllables of the inputted word 
                    if '0' in index[z]:
                        for item in range(len(sound)):
                            if index[z:] == sound[item]:
                                before = z - 1
                                if index[before:] != check[item]:
                                    if i not in temporary:
                                        temporary[i] = 1
                                        count += 1
                                    elif i in temporary:
                                        temporary[i] += 1
                                        count += 1
                        if count > 1:
                            z = len(index)
                    z += 1
                outer += 1
    return temporary

main()