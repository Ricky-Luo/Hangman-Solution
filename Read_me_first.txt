

# Working Thread
Because the first information I can obtain from the API at the first round (0 round) is the length of the word, so I can use this imformation to optimize my algorithm. I calculate the all appeared letters' possilility grouped by word length from the train set you offered, and according the result, I can pick the most possible letter by the length at the first round.

Because the train set contains certain structure information, I extract it by building Markov Chain, then I got all letters' transformative possibility to all next letters. 

Then if I get one correct letter at once, I use this letter to get the next most possible letter according transformative possibility matrix.


# Project structure
For the train set is large, do real-time computing is very time consuming. I split the the possibility calculation from the guess algorithm.

1. "cal_possibility_from_local_dic.py": calculating the possibilities of certain length groups of the words, and producing the result: "possibility_result.json".

2. "cal_transformative_possibility": calculating the transformative possibility of all words, and producing the result: "transformative_possibility.json".

3. in the function "__init__" in "hangman_api_user.ipynb", loading the two possibility result: "possibility_result.json", "transformative_possibility.json".

