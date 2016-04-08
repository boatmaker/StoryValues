import re
def main():

    def score(word):
        total = 0
        for i in word:
            total += charValues[i]
        return(total)

    tempValueList = []
    tempStoryList = []
    storyList = []
    newStoryList = []
    targetScores =[]
    wordValues = {}
    matchedScores = {}
    wordSet = set()
    alphaWordList = []

    valueFile = open('/Users/hgoscenski/GitHub/StoryValues/characterValues.txt', 'r')
    storyFile = open('/Users/hgoscenski/GitHub/StoryValues/story.txt', 'r')

    for line in valueFile:
        tempValueList.append(line.split())

    charValues = dict(zip(tempValueList[0][0::2], tempValueList[0][1::2]))
    for k in charValues:
        charValues[k] = int(charValues[k])
    tempTargetScores = tempValueList[1]
    for value in tempTargetScores:
        targetScores.append(int(value))

    for line in storyFile:
        tempStoryList.append(line.split())

    for item in tempStoryList:
        for i in item:
            storyList.append(i)
    for word in storyList:
        if word.isalpha():
            if re.match('[a-z]', word):
                wordSet.add(word)

    for word in wordSet:
        alphaWordList.append(word)

    alphaWordList.sort()

    # print(alphaWordList)
    for index,word in enumerate(alphaWordList):
        wordValues[word] = score(word) + index

    for k in wordValues:
        # print(k)
        # print(wordValues[k])
        for j in targetScores:
            # print(j, wordValues[k], k)
            if wordValues[k] == j:
                matchedScores[k] = wordValues[k]
            # matchedScores[k] = wordValues[k]

    print(matchedScores)
    print(wordValues['able'])

main()
