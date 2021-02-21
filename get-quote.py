import random

def print_quote():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) -1
  rnd = random.randint(0,last)
  rnd1 = random.randint(0,last)

  print(quotes[rnd],quotes[rnd1][:-1])
  
def write_quote():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) -1
  rnd = random.randint(0,last)

  f = open("random.txt","a+")
  f.write(quotes[rnd])
  f.close()

if __name__== "__main__":
  print_quote()
  #write_quote()
