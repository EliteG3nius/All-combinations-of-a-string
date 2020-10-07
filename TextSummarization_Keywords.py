from gensim.summarization import summarize
from gensim.summarization import keywords

UserInput = input(str("Enter the Text here to summarize:\n"))
print ("Summary of the text:\n")
print (summarize(UserInput))
print ("Keywords of the text:\n")
print (keywords(UserInput))
