import re

enums = ["Object", "Action", "Description"]
name = "Chris"

defin = {"i\'m": "0 yourself", "bored": "2 lacking activity", "lacking": "2 not available", "activity": "something being done"}

#Can store each action set by storing words/concepts to actions through
#using eval to reference functions with a string
#How on earth do I get this AI to decide what actions to take when
#Sentances structures:
#	Noun action
#	Action noun
#	Desciption noun
#	Description noun action
#	Description action noun
#Whole point is that the algorithm is meant to find actions based on previous interacts and process searches found for new actions


def operatingOnSelf():
	print("operatingOnSelf")

def negative():
	print("negative")

known = {"yourself": operatingOnSelf, "lacking": negative} #The known actions developed. Has to be after all the function headers to ensure

def main():
	userInput = "i\'m bored"
	words = re.split('\s+', userInput)
	for word in words:
		defination = defin[word]
		wordType = enums[int(re.split('\s+', defination)[0])]
		print(defination)


if __name__ == "__main__":
	main()