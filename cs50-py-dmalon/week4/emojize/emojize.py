# pip install emoji

import emoji

def main():
    emo_string = input("Input: ")
    # emo_string = ":1st_place_medal:"
    printEmoji(emo_string)

def printEmoji(emo_string):
    print("Output: ", emoji.emojize(emo_string, language='alias'))

main()