import re
def main():
    tempValueList = []
    tempStoryList = []
    valueFile = open('/Users/hgoscenski/GitHub/StoryValues/characterValues.txt', 'r')
    storyFile = open('/Users/hgoscenski/GitHub/StoryValues/story.txt', 'r')

    for line in valueFile:
        tempValueList.append(line.split())

    characterValues = dict(zip(tempValueList[0][0::2], tempValueList[0][1::2]))
    targetScores = tempValueList[1]

    for line in storyFile:
        tempStoryList.append(line.split())
    
    # for entry in tempStoryList:
    #     if entry is str and entry is
    # print(storyList)




    # characterValues = dict(zip(characterValues[0::2], characterValues[1::2]))
    # print(characterValues)
    # print(targetScores)

main()
