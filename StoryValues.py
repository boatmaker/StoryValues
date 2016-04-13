import re
def main():

    # Scoring method- takes the word and returns the value of the word from its
    # letters but not from its postiion
    def score(word):
        total = 0
        for i in word:
            total += charValues[i]
        return(total)

    # Initializing all of the lists, dictionaries, and sets needed for the
    # program
    tempValueList = []
    tempStoryList = []
    storyList = []
    newStoryList = []
    targetScores =[]
    wordValues = {}
    matchedScores = {}
    wordSet = set()
    alphaWordList = []

    # Opening the files needed to reference- the character value document
    # and the story
    valueFile = open('/Users/hgoscenski/GitHub/StoryValues/characterValues-2.txt', 'r')
    storyFile = open('/Users/hgoscenski/GitHub/StoryValues/story.txt', 'r')

    # Takes the opened valueFile and splits it into a list split by \n
    for line in valueFile:
        tempValueList.append(line.split())

    # Takes the first entry in the list and zips it into a dictionary
    charValues = dict(zip(tempValueList[0][0::2], tempValueList[0][1::2]))

    # Takes the value of the charValues and turns it into the dictionary
    for k in charValues:
        charValues[k] = int(charValues[k])

    # Takes the second line of the document and uses them as the target values
    # The target values go into a temporary direectory
    tempTargetScores = tempValueList[1]

    # The values in the temporary directory are turned into integers
    for value in tempTargetScores:
        targetScores.append(int(value))

    # Takes all of the lines in the sotry and puts them into a long temp list
    # delineated by \n
    for line in storyFile:
        tempStoryList.append(line.split())

    # Takes the sublists in the temp list and turns them into a
    # list that is more usable
    for item in tempStoryList:
        for i in item:
            storyList.append(i)

    # Uses a Regular Expression to glob out words that fit the criteria of words
    # i.e. only consisting of letters 'a-z' then places them in a set
    # The set strips the story of any repeated words and then allows it to be
    # utilized for scoring
    for word in storyList:
        if word.isalpha():
            if re.match('[a-z]', word):
                wordSet.add(word)

    # Takes the set and turns it back into a list
    for word in wordSet:
        alphaWordList.append(word)

    # Sorts the list alphabetically
    alphaWordList.sort()

    # Scores the word using the score method defined at the beginning of the
    # program and the position of the word in the alphabetically sorted list
    for index,word in enumerate(alphaWordList):
        wordValues[word] = score(word) + index

    # Checks to see if any of the found words match with the given scores in
    # targetScores
    for k in wordValues:
        for j in targetScores:
            if wordValues[k] == j:
                matchedScores[k] = wordValues[k]

    # Sorting the dictionary based on the value then placing it into a list of
    # tuples that can then be printed
    matchedScoresSorted = [(k,v) for v,k in sorted([(v,k) for k,v in matchedScores.items()])]

    # Prints the sorted list of tuples
    for x in matchedScoresSorted:
        print(x)

main()
