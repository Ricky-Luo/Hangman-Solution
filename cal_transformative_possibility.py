"""
This file is to calculate the transformative possibility of all words, 
add save the result to local file system in Json format for improving time performance.

Result file name: transformative_possibility.Json

@Author: Juehuai Luo
@Last edit time: May-29-2023

"""

from collections import defaultdict
import json

# calculate transformative matrix.
def calculate_transition_matrix(words):
    transition_counts = defaultdict(lambda: defaultdict(int))
    letter_counts = defaultdict(int)
    
    # count transformative frequency and words frequency.
    for word in words:
        for i in range(len(word)):
            current_letter = word[i]
            
            for j in range(len(word)):
                 next_letter = word[j]
                 if i != j:
                     transition_counts[current_letter][next_letter] += 1
            
            letter_counts[current_letter] += 1
            
    
    print(transition_counts);
    
    # Count possibility and build transformative matrix
    transition_matrix = defaultdict(lambda: defaultdict(float))
    for current_letter, transitions in transition_counts.items():
        for next_letter, count in transitions.items():
            transition_matrix[current_letter][next_letter] = count / letter_counts[current_letter]
    
    return transition_matrix

# get full dictionay in array form from the text.
def build_dictionary( dictionary_file_location):
        text_file = open(dictionary_file_location,"r")
        full_dictionary = text_file.read().splitlines()
        text_file.close()
        return full_dictionary;


if __name__ == '__main__':

    # get the training text, and do primative process.
    full_dictionary_location = "words_250000_train.txt"
    dictionary = build_dictionary(full_dictionary_location)
    matrix = calculate_transition_matrix(dictionary)
    words_by_length = {}
    transformative_possibility_json = {}
    transformative_possibility_by_length = {}
    
    # Sort the transformative Matrix, and turn it into Json format
    for current_letter, transitions in matrix.items():
        transformative_possibility_json[current_letter] = {}

        for next_letter, probability in transitions.items():
            transformative_possibility_json[current_letter][next_letter] = probability

        transformative_possibility_json[current_letter] = dict(sorted(transformative_possibility_json[current_letter].items(), key=lambda x: x[1], reverse = True))
   
    # Calculate the transformative possibility Group by length, but it was proved useless.
    # for i in range(28):
    #     transformative_possibility_by_length[i] = {}
    #     words_by_length[i] = []

    #     for word in dictionary:
    #         if len(word) == i :
    #             words_by_length[i].append(word)
    #             # dictionary.remove(word)
            
    #     matrix_temp = calculate_transition_matrix(words_by_length[i])
    #     for current_letter, transitions in matrix_temp.items():
    #         transformative_possibility_by_length[i][current_letter] = {}

    #         for next_letter, probability in transitions.items():
    #             transformative_possibility_by_length[i][current_letter][next_letter] = probability

    #         transformative_possibility_by_length[i][current_letter] = dict(sorted(transformative_possibility_by_length[i][current_letter].items(), key=lambda x: x[1], reverse = True))


    # Save the possibility result in file, for improving time preformance. 
    with open('transformative_possibility.json', 'w') as file:
         json.dump({'transformative_possibility': transformative_possibility_json, 'transformative_possibility_by_length': transformative_possibility_by_length}, file)