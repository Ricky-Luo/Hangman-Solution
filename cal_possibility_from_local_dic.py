"""
This file is to calculate the possibilities of certain length groups of the words, 
add save the result to local file system in Json format for improving time performance.

Result file name: possibility_result.Json

@Author: Juehuai Luo
@Last edit time: May-29-2023

"""

import json

# get full dictionay in array form from the text.
def build_dictionary( dictionary_file_location):
        text_file = open(dictionary_file_location,"r")
        full_dictionary = text_file.read().splitlines()
        text_file.close()
        return full_dictionary;

# get full dictionay text in text form from the text.
def get_dic_full_text( dictionary_file_location):
        text_file = open(dictionary_file_location,"r")
        full_dictionary = text_file.read()
        full_dictionary = full_dictionary.replace("\n", "");
        text_file.close()
        return full_dictionary;

# get the all single letters from the entire text.
def get_all_letters(text = ""):
    letters = [];
    for char in text:
        if (letters.count(char) < 1):
             letters.append(char);
    return letters;

 # calculate the possibility of single letters in overall text.
def cal_possibility_in_all(text = "", letters=[]):
    possibility_dict = {};
    text_length = len(text);
    for char in letters:
        possibility = text.count(char) / text_length;
        possibility_dict[char] = possibility;
    sorted_possibility_dict = dict(sorted(possibility_dict.items(), reverse = False));
    return sorted_possibility_dict;

# calculate the possibility of single letters in certain length words.
def cal_possibility_by_word_group(dictionary = [], letters = []):
    word_group = {};
    possibility_by_word_length = {};
    print("Step one: group the words by length")
    for word in dictionary:
        word_len = len(word)
        if word_len == 1:
            print(word)
        if word_len not in word_group:
             word_group[word_len] = [word];
        else:
             word_group[word_len].append(word)
             
    print("Step two: calculate the possibilities by grouped words")
    for item in word_group:
        letter_possibility = {}
        for letter in letters:
           text = "".join(word_group.get(item))
           possibility = text.count(letter) / len(text)
           letter_possibility[letter] = possibility
        letter_possibility = dict(sorted(letter_possibility.items(), key=lambda x: x[1], reverse = True))
        print("字数")
        print(item)
        print(next(iter(letter_possibility)))
        print(iter(letter_possibility))
        possibility_by_word_length[item] = letter_possibility
        
    return possibility_by_word_length


if __name__ == '__main__':

    # get the training text, and do primative process.
    full_dictionary_location = "words_250000_train.txt"
    dic_full_text = get_dic_full_text(full_dictionary_location)
    letters = get_all_letters(dic_full_text)
    dictionary = build_dictionary(full_dictionary_location)

    # calculate the possibility of single letters in overall text.
    possibility_overall = cal_possibility_in_all(dic_full_text, letters)

    # calculate the possibility of single letters in certain length words.
    possibility_by_word_length = cal_possibility_by_word_group(dictionary, letters)
    
    # Save the possibility result in file, for improving time preformance. 
    with open('possibility_result.json', 'w') as file:
         json.dump({'possibility_overall': possibility_overall, 'possibility_by_word_length': possibility_by_word_length}, file)
    
