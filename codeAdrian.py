def stars(NumberOfStars):
    if NumberOfStars > 0:
      print("*")
      stars(NumberOfStars -1)
print("How many stars to print?")
number=int(input())
stars(number)
