import nltk
import numpy

from nltk.corpus import wordnet 


mydict={'Bestest': 'Fantastic', 'Bizzaroo': 'Strange', 'Blahh': 'Tired',
 'Blanko': 'Forget', 'Blash-T': 'Angry', 'Blissie': 'Happy', 'Bloat-T': 'Bloated',
 'Bluhoo': 'Sad', 'Blushie': 'Embarrass', 'Bye-Q': 'Good-bye', 'Chuckchuck': 'Give up',
 'Clapclap': 'Encore', 'Clingie': 'Hang', 'Cramcram': 'Study', 'Dazzlie': 'Beautiful',
 'Delichu': 'Delicious', 'Delin-Q': 'Bad', 'Digdig': 'Dig', 'Dingbang': 'Noisy',
 'Dingding': 'Realize', 'Dundeal': 'Sell', 'Fend-D': 'Defend', 'Flipflop': 'Switch',
 'Frost-T': 'Freezing', 'Fussfuss': 'Worry', 'Gasp-P': 'Oh no!', 'Giftee': 'Give',
 'Givehoo': 'Ask for', 'Gofor': 'Goal', 'Gogo': 'Ride', 'Goodgo': 'Good luck',
 'Go-P': 'Bathroom', 'Gorush': 'Hurry', 'Gossip-p': 'Small talk', 'Grab-B': 'Get',
 'Greatchu': 'Great', 'Grit-T': 'Courage', 'Hamchu': 'Kind', 'Hambond': 'Bond',
 'Hamboree': 'Party', 'Hamcheer': 'Congrats', 'Hamha': 'Greeting', 'Hamigos': 'Best Pals',
 'Hamlift': 'Piggyback', 'Hammo': 'Friend', 'Hampact': 'Promise', 'Hamscope': 'Aim',
 'Hamsolo': 'Lonely', 'Hamspar': 'Rival', 'Hamtast': 'Perfect', 'Hamteam': 'Cooperate',
 'Hardihar': 'Laugh', 'Herk-Q': 'Powerful', 'Heyhoo': 'Call out', 'Hif-Hif': 'Sniff',
 'Hotchu': 'Hot', 'Huffpuff': 'Carry', 'Hulahula': 'Lollygag', 'Hushgo': 'Reveal',
 'Hushie': 'Secret', 'Jamout': 'Play music', 'Koochi-Q': 'Pretty', 'Krmpkrmp': 'Eat',
 'Lalalala': 'Sing', 'Libert-T': 'Freedom', 'Lookie': 'See', 'Lost-T': 'Lose',
 'Lotsa': 'Many', 'Lovedove': 'Cherished', 'Luck-E': 'Lucky', 'Meep-P': 'Regret',
 'Mega-Q': 'Big', 'Might-T': 'Strong', 'Minglie': 'Play', 'Nogo': 'No can do',
 'Nok-Nok': 'Knock', 'Nokrmp-P': 'Hungary', 'No-P': 'No', 'Nopibloo': "Don't fret",
 'Nopookie': 'Dislike', 'Noworrie': 'Relax', 'Offdoff': 'Remove', 'Oopsie': 'Sorry',
 'Ouchichi': 'Ouch', 'Pakapaka': 'Bite', 'Panic-Q': 'Scary', 'Passchat': 'Tell',
 'Perksie': 'Listen', 'Pooie': 'Uncool', 'Pookie': 'Like', 'Pushie': 'Shove',
 'Putput': 'Put', 'Rubrub': 'Polish', 'Scoochie': 'Climb', 'Scrit-T': 'Scratch',
 'Scrub-E': 'Clean', 'See-tru': 'Invisable', 'Sesam-E': 'Open', 'Shashaa': 'Hide',
 'Shockie': 'Surprise', 'Smidgie': 'Almost', 'Smoochie': 'Love', 'Snorklie': 'Deep',
 'Soak-Q': 'Wet', 'Sparklie': 'Delight', 'Spiffie': 'Stylish', 'Stead-E': 'Solid',
 'Stickie': 'Poke', 'Swellie': "It's OK", 'Tack-Q': 'Roll', 'Ta-dah': 'Show',
 'Teenie': 'Small', 'Thank-Q': 'Thank You', 'Thump-P': 'Startle', 'Tinglie': 'Tingle',
 'Tiptop': 'Exellent', 'Tootru': 'Really', 'Tran-Q': 'Peace', 'Trust-T': 'Reliable',
 'Tuggie': 'Tug', 'Twintoo': 'Identical', 'Twirlie': 'Twirl', 'Vast-T': 'Wide',
 'Wait-Q': 'Wait', 'Wake-Q': 'Wake up', 'Whawha': 'Frantic', 'Wishie': 'Beg',
 'Wit-T': 'Funny', 'Wondachu': 'Wonderful', 'Yep-P': 'Yes', 'Zuzuzu': 'Sleep'}

synonyms = []
mydict_extended={}
for key,val in mydict.items():
  mydict_extended[key]=set([])
  for syn in wordnet.synsets(val): 
      for l in syn.lemmas():
          mydict[key]=mydict_extended[key].add(l.name())
          synonyms.append(l.name())
print(mydict_extended.items())
print(set(synonyms)) 

mydict_extended={}




mydict2={}
for j,k in mydict.items():
  mydict2[k]=j

bi_dict={}
for word in mydict.keys():
  word=word.lower()
  bi = zip(word, word[1:])
  for gram in list(bi):
    bi_dict[gram]=bi_dict.get(gram, 0)+1
    
x=mydict.keys()
tri_dict={}
for word in mydict.keys():
  word=word.lower()
  tri = zip(word, word[1:], word[2:])
  for gram in list(tri):
    tri_dict[gram]=tri_dict.get(gram, 0)+1

trigram_list=list(tri_dict.items())
trigram_counts=[(i,j/625) for i,j in tri_dict.items()]

set(bi_dict.values())
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 19, 23, 28}
sum(bi_dict.values())
#750
prob=[i/750 for i in set(bi_dict.values())]
#prob
#[0.0013333333333333333, 0.0026666666666666666, 0.004, 0.005333333333333333, 0.006666666666666667, 0.008, 0.009333333333333334, 0.010666666666666666, 0.012, 0.013333333333333334, 0.014666666666666666, 0.016, 0.017333333333333333, 0.018666666666666668, 0.021333333333333333, 0.025333333333333333, 0.030666666666666665, 0.037333333333333336]
prob=[round(i/750,3) for i in set(bi_dict.values())]
#prob
#[0.001, 0.003, 0.004, 0.005, 0.007, 0.008, 0.009, 0.011, 0.012, 0.013, 0.015, 0.016, 0.017, 0.019, 0.021, 0.025, 0.031, 0.037]




prob_count_pairs = list(zip(set(bi_dict.values()), prob))
#prob_count_pairs
#[(1, 0.001), (2, 0.003), (3, 0.004), (4, 0.005), (5, 0.007), (6, 0.008), (7, 0.009), (8, 0.011), (9, 0.012), (10, 0.013), (11, 0.015), (12, 0.016), (13, 0.017), (14, 0.019), (16, 0.021), (19, 0.025), (23, 0.031), (28, 0.037)]
xdict={}
for x,y in bi_dict.items():
  if y not in xdict:
    xdict[y] = set()
  xdict[y].add(x)

for idx in sorted(xdict.keys()):
    for j,k in xdict.items():
      if idx==j:
        print(j)
        for kk in k:
          print(kk[0],kk[1],)

#bigrams per lexical item
lens=sum([len(word)/2 for word in mydict.keys()])/len(mydict.keys())
#lens
#3.367424242424242

bigram_counts=[[('b', 'e'), 0.0026666666666666666], [('e', 's'), 0.004], [('s', 't'), 0.012], [('t', 'e'), 0.006666666666666667], [('b', 'i'), 0.0013333333333333333], [('i', 'z'), 0.0013333333333333333], [('z', 'z'), 0.0026666666666666666], [('z', 'a'), 0.0013333333333333333], [('a', 'r'), 0.006666666666666667], [('r', 'o'), 0.0026666666666666666], [('o', 'o'), 0.021333333333333333], [('b', 'l'), 0.010666666666666666], [('l', 'a'), 0.014666666666666666], [('a', 'h'), 0.004], [('h', 'h'), 0.0013333333333333333], [('a', 'n'), 0.006666666666666667], [('n', 'k'), 0.0026666666666666666], [('k', 'o'), 0.0026666666666666666], [('a', 's'), 0.008], [('s', 'h'), 0.013333333333333334], [('h', '-'), 0.0013333333333333333], [('-', 't'), 0.016], [('l', 'i'), 0.018666666666666668], [('i', 's'), 0.0026666666666666666], [('s', 's'), 0.006666666666666667], [('s', 'i'), 0.005333333333333333], [('i', 'e'), 0.037333333333333336], [('l', 'o'), 0.010666666666666666], [('o', 'a'), 0.0026666666666666666], [('a', 't'), 0.004], [('t', '-'), 0.014666666666666666], [('l', 'u'), 0.004], [('u', 'h'), 0.0013333333333333333], [('h', 'o'), 0.006666666666666667], [('u', 's'), 0.010666666666666666], [('h', 'i'), 0.014666666666666666], [('b', 'y'), 0.0013333333333333333], [('y', 'e'), 0.0026666666666666666], [('e', '-'), 0.004], [('-', 'q'), 0.016], [('c', 'h'), 0.018666666666666668], [('h', 'u'), 0.017333333333333333], [('u', 'c'), 0.005333333333333333], [('c', 'k'), 0.008], [('k', 'c'), 0.0013333333333333333], [('c', 'l'), 0.004], [('a', 'p'), 0.004], [('p', 'c'), 0.0013333333333333333], [('i', 'n'), 0.010666666666666666], [('n', 'g'), 0.009333333333333334], [('g', 'i'), 0.006666666666666667], [('c', 'r'), 0.005333333333333333], [('r', 'a'), 0.005333333333333333], [('a', 'm'), 0.025333333333333333], [('m', 'c'), 0.004], [('d', 'a'), 0.004], [('a', 'z'), 0.0013333333333333333], [('z', 'l'), 0.0013333333333333333], [('d', 'e'), 0.004], [('e', 'l'), 0.004], [('i', 'c'), 0.005333333333333333], [('n', '-'), 0.0026666666666666666], [('d', 'i'), 0.008], [('i', 'g'), 0.005333333333333333], [('g', 'd'), 0.0026666666666666666], [('g', 'b'), 0.0013333333333333333], [('b', 'a'), 0.0013333333333333333], [('d', 'u'), 0.0013333333333333333], [('u', 'n'), 0.0013333333333333333], [('n', 'd'), 0.005333333333333333], [('e', 'a'), 0.005333333333333333], [('a', 'l'), 0.005333333333333333], [('f', 'e'), 0.0013333333333333333], [('e', 'n'), 0.0026666666666666666], [('d', '-'), 0.0026666666666666666], [('-', 'd'), 0.0026666666666666666], [('f', 'l'), 0.0026666666666666666], [('i', 'p'), 0.004], [('p', 'f'), 0.0013333333333333333], [('o', 'p'), 0.008], [('f', 'r'), 0.0013333333333333333], [('o', 's'), 0.005333333333333333], [('f', 'u'), 0.0026666666666666666], [('s', 'f'), 0.0013333333333333333], [('g', 'a'), 0.0026666666666666666], [('s', 'p'), 0.005333333333333333], [('p', '-'), 0.008], [('-', 'p'), 0.010666666666666666], [('i', 'f'), 0.006666666666666667], [('f', 't'), 0.0026666666666666666], [('e', 'e'), 0.008], [('i', 'v'), 0.0013333333333333333], [('v', 'e'), 0.004], [('e', 'h'), 0.0013333333333333333], [('g', 'o'), 0.014666666666666666], [('o', 'f'), 0.004], [('f', 'o'), 0.0013333333333333333], [('o', 'r'), 0.006666666666666667], [('o', 'g'), 0.0026666666666666666], [('o', 'd'), 0.0013333333333333333], [('d', 'g'), 0.0026666666666666666], [('o', '-'), 0.0026666666666666666], [('r', 'u'), 0.009333333333333334], [('g', 'r'), 0.004], [('a', 'b'), 0.0013333333333333333], [('b', '-'), 0.0026666666666666666], [('-', 'b'), 0.0013333333333333333], [('r', 'e'), 0.0026666666666666666], [('t', 'c'), 0.0026666666666666666], [('r', 'i'), 0.004], [('i', 't'), 0.005333333333333333], [('h', 'a'), 0.030666666666666665], [('m', 'b'), 0.0026666666666666666], [('b', 'o'), 0.0026666666666666666], [('o', 'n'), 0.0026666666666666666], [('h', 'e'), 0.004], [('e', 'r'), 0.005333333333333333], [('m', 'h'), 0.0013333333333333333], [('m', 'i'), 0.005333333333333333], [('m', 'l'), 0.0013333333333333333], [('m', 'm'), 0.0013333333333333333], [('m', 'o'), 0.004], [('m', 'p'), 0.006666666666666667], [('p', 'a'), 0.009333333333333334], [('a', 'c'), 0.004], [('c', 't'), 0.0013333333333333333], [('m', 's'), 0.004], [('s', 'c'), 0.006666666666666667], [('c', 'o'), 0.0026666666666666666], [('p', 'e'), 0.0026666666666666666], [('s', 'o'), 0.0026666666666666666], [('o', 'l'), 0.0013333333333333333], [('m', 't'), 0.0026666666666666666], [('t', 'a'), 0.004], [('r', 'd'), 0.0013333333333333333], [('i', 'h'), 0.0013333333333333333], [('r', 'k'), 0.005333333333333333], [('k', '-'), 0.008], [('e', 'y'), 0.0013333333333333333], [('y', 'h'), 0.0013333333333333333], [('f', '-'), 0.0013333333333333333], [('-', 'h'), 0.0013333333333333333], [('o', 't'), 0.004], [('u', 'f'), 0.0026666666666666666], [('f', 'f'), 0.006666666666666667], [('f', 'p'), 0.0013333333333333333], [('p', 'u'), 0.005333333333333333], [('u', 'l'), 0.0026666666666666666], [('h', 'g'), 0.0013333333333333333], [('j', 'a'), 0.0013333333333333333], [('o', 'u'), 0.0026666666666666666], [('u', 't'), 0.004], [('o', 'c'), 0.005333333333333333], [('i', '-'), 0.0013333333333333333], [('k', 'r'), 0.004], [('r', 'm'), 0.004], [('p', 'k'), 0.0013333333333333333], [('i', 'b'), 0.0026666666666666666], [('r', 't'), 0.0013333333333333333], [('o', 'k'), 0.008], [('k', 'i'), 0.006666666666666667], [('t', 's'), 0.0013333333333333333], [('s', 'a'), 0.0026666666666666666], [('o', 'v'), 0.0026666666666666666], [('e', 'd'), 0.0013333333333333333], [('d', 'o'), 0.0026666666666666666], [('-', 'e'), 0.005333333333333333], [('m', 'e'), 0.0026666666666666666], [('e', 'p'), 0.0026666666666666666], [('e', 'g'), 0.0013333333333333333], [('a', '-'), 0.0026666666666666666], [('g', 'h'), 0.0013333333333333333], [('h', 't'), 0.0013333333333333333], [('g', 'l'), 0.0026666666666666666], [('n', 'o'), 0.012], [('-', 'n'), 0.0013333333333333333], [('p', 'i'), 0.0026666666666666666], [('p', 'o'), 0.004], [('o', 'w'), 0.0013333333333333333], [('w', 'o'), 0.0026666666666666666], [('r', 'r'), 0.0013333333333333333], [('f', 'd'), 0.0013333333333333333], [('p', 's'), 0.0013333333333333333], [('a', 'k'), 0.005333333333333333], [('k', 'a'), 0.0026666666666666666], [('n', 'i'), 0.0026666666666666666], [('c', '-'), 0.0013333333333333333], [('k', 's'), 0.0013333333333333333], [('o', 'i'), 0.0013333333333333333], [('t', 'p'), 0.0013333333333333333], [('u', 'b'), 0.004], [('b', 'r'), 0.0013333333333333333], [('s', 'e'), 0.0026666666666666666], [('t', 'r'), 0.005333333333333333], [('m', '-'), 0.0013333333333333333], [('a', 'a'), 0.0013333333333333333], [('s', 'm'), 0.0026666666666666666], [('i', 'd'), 0.0013333333333333333], [('s', 'n'), 0.0013333333333333333], [('k', 'l'), 0.0026666666666666666], [('f', 'i'), 0.0013333333333333333], [('a', 'd'), 0.0013333333333333333], [('t', 'i'), 0.004], [('s', 'w'), 0.0013333333333333333], [('w', 'e'), 0.0013333333333333333], [('l', 'l'), 0.0013333333333333333], [('t', 'h'), 0.0026666666666666666], [('u', 'm'), 0.0013333333333333333], [('p', 't'), 0.0013333333333333333], [('t', 'o'), 0.004], [('t', 'u'), 0.0013333333333333333], [('u', 'g'), 0.0013333333333333333], [('g', 'g'), 0.0013333333333333333], [('t', 'w'), 0.0026666666666666666], [('w', 'i'), 0.005333333333333333], [('n', 't'), 0.0013333333333333333], [('i', 'r'), 0.0013333333333333333], [('r', 'l'), 0.0013333333333333333], [('v', 'a'), 0.0013333333333333333], [('w', 'a'), 0.0026666666666666666], [('a', 'i'), 0.0013333333333333333], [('k', 'e'), 0.0013333333333333333], [('w', 'h'), 0.0026666666666666666], [('a', 'w'), 0.0013333333333333333], [('z', 'u'), 0.004], [('u', 'z'), 0.0026666666666666666]]
a=[i for i,j in bigram_counts]
aa = [i[0]+i[1] for i in a]

b=[i for i,j in trigram_counts]
bb = [i[0]+i[1]+i[2] for i in b]
prob_dist=[i[1] for i in bigram_counts]

filtered_bigram_counts=[(i[0],i[1]*750) for i in bigram_counts if i[1]>0.008]

filtered_bigram_counts=[(i[0],i[1]*750) for i in bigram_counts if i[1]>0.008]
filtered_total=sum(i[1] for i in filtered_bigram_counts)

a=[i for i,j in filtered_bigram_counts]
aa = [i[0]+i[1] for i in a]

  
filtered_prob_dist=[i[1]/filtered_total for i in filtered_bigram_counts]
for i in range(10):
  print("".join(list(numpy.random.choice(a=aa,size=3, replace=None, p=filtered_prob_dist))))



##prob_dist_trigram=[i[1] for i in trigram_counts]
##
##
##for i in range(10):
##  print("".join(list(numpy.random.choice(a=bb,size=3, replace=None, p=prob_dist_trigram))))
filtered_prob_dist_trigram=''


predictions=[]
for i in range(100):
	predictions.append(("".join(list(numpy.random.choice(a=aa,size=3, replace=None, p=filtered_prob_dist)))))


def format_results(predictions):
  sanitized=set([])
  for i in predictions:
    if i.startswith("-"):
      pass
    elif i[-2]=="-":
      i = i[:-1]+i[-1].upper()
      print(i)
      sanitized.add(i)
    else:
      print(i)
      sanitized.add(i)
  return sanitized

def reduce_vowels(word):
  newword=''
  for i in range(len(word)):
    print(i, newword)
    if len(newword)>=1:
	    if newword[-1]==word[i]:
		    pass
	    else:
		    newword+=word[i]
    else:
	    newword+=word[i]
  print(newword)
  return newword

def hamify(word):
  pass


san=format_results(predictions)
print(san)

san2=set([])
for word in san:
  nw=reduce_vowels(word)
  sand2.add(nw)
  
