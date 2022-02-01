import random
lih = []
coin = ['heads','tails']

def toss():
  for a in range(100):
      flip = random.choice(coin)
      lih.append(flip)
      noHead = lih.count('heads')
      probH = (noHead/100) * 100
      probT = 100 - probH
      
   print(probH, "% is heads ", probT, " % is tails")
toss()
