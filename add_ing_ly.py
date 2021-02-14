#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
def add_ingly(n):
  l = len(n)

  if l > 2:
    if n[-3:] == 'ing':
      n += 'ly'
    else:
      n += 'ing'
  print("The modified string is:",n)

n=input("Enter string:")
add_ingly(n)
