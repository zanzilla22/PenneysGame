import random
import matplotlib.pyplot as plt
print([1, 2] + [3, 4])
runs = 10000
pullCounts = {}
choiceOrder1 = ['black', 'black', 'red']

for x in range(runs):

  pulls = []
  deck = ["red" for x in range(52)]
  deck[26:] = ["black" for x in range (26)]
  random.shuffle(deck)
  
  def pullCard():
    pulls.append(deck[-1])
    deck.pop(-1)
  
  for x in range(3):
    pullCard()
  
  while(choiceOrder1 != pulls[-3:] and len(deck) != 0):
    pullCard()
  if(len(deck)>0):
    pCount = len(pulls)-2
    pullCounts[pCount] = pullCounts.get(pCount, 0) + 1

pullCounts = dict(sorted(pullCounts.items()))
print(pullCounts)
print('Pulls\tOccurances\n'+ '\n'.join([str(x+1) + '\t' + str(pullCounts.get(x+1, 0)) for x in range(52)]))

plt.bar(list(pullCounts.keys()), list(pullCounts.values()))
plt.xlabel('Pulls')
plt.ylabel('Occurances')
plt.title(f"Histogram for order |{' '.join(choiceOrder1)}| Avg: {round(sum(list(x*pullCounts[x] for x in pullCounts.keys()))/runs, 3)}\n({runs} runs) FP Odds: {pullCounts[1] / runs * 100}%")
print(f"expected fp: %{(1/2)**3*100}")
plt.show()
