'''

Intro
To solve this challenge, feel free to use any and all resources available to you. Once you start the exercise, you’ll have two hours to complete and submit your solution.

Challenge - Pig Latin
Pig Latin is a farcical “language” used to entertain children, but also to teach them some valuable language concepts along the way. Translating English to Pig Latin is simple:

Take the first consonant (or cluster of consonants) of a word, move it to the end of the word, and add a suffix of “ay”
If a word begins with a vowel, just add “way” at the end
For the sake of readability, separate the Pig Latin-ized parts of the word with a dash -
Your challenge is to implement the method pigLatinize that takes a string phrase and translates it to Pig Latin. You’re free to add additional classes, variables, and methods if you would like.

The input phrase could be as short as a single word, or as long as multiple sentences or paragraphs. Whitespace, capitalization, and punctuation should be honored and maintained in your final answer.

Examples
“pig” => “ig-pay”
“pig latin” => “ig-pay atin-lay”
“Pig Latin” => “ig-Pay atin-Lay”
'''
def pig_latinize(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)):
        word = sentence[i]
        if word[-1].isalpha():
            if word[0] in ['a', 'e', 'i', 'o', 'u']:
                sentence[i] = word + '-way'
            else:
                sentence[i] = word[1::] + '-' + word[0] + 'ay'
        else:
            if word[0] in ['a', 'e', 'i', 'o', 'u']:
                sentence[i] = word[:-1:] + '-way' + word[-1] 
            else:
                sentence[i] = word[1:-1:] + '-' + word[0] + 'ay' + word[-1] 

    return ' '.join(sentence)


if __name__ == '__main__':
    test_string = "Pig Latin is a farcical language."
    print(pig_latinize(test_string))
