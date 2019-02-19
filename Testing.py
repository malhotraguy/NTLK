import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
text=open("text_test.txt","r", encoding="utf-8").read()
#text="""The Global Warming Quandary?
#The debate on global warming continues even though overwhelming scientific evidence has been supported that this is indeed a problem the world faces. Scientists have shown that global warming is at its “tipping point” and yet the world governments make no solid effort in claiming that the Earth is facing such a vulnerability. In today’s world, there appears to be a battle raging between global warming alarmists and global warming skeptics. This prevents cooperation on the issue and halts real progress to reduce or reverse global warming. Undoubtedly, every nation can agree that the Earth is important in sustaining life and must be protected for continual survival of life. To ensure a healthier and safer world for future generations, the problem of global warming should be properly substantiated and addressed with realistic solutions by the world governments.
#So, why is global warming so controversial, highly contentious and debatable? There appears to be several factors that cause global warming controversies, such as politics, poor messaging of global warming, the media, and economic costs due to our dependency on fossil fuels. Many of these things can make it difficult for the objective observer to realize the scope of the problem and often turn many people into skeptics of global warming. Fowler, an adjunct professor at George Mason University, states that “global warming, in fact, has to some degree displaced evolution as the subject where public disagreement over science has turned into politicized controversy """
print(text)
#tokenized_text=sent_tokenize(text)
tokenized_text=word_tokenize(text)
print(tokenized_text)
print(len(tokenized_text))
fdist = FreqDist(tokenized_text)
print(fdist["the"])
print(fdist.most_common(3))

