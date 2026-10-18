 

number= [13,22,32,33,43,56,77]
even_count=0
odd_count=0

for num in number:
  if num % 2== 0:
   even_count+= 1

  else:
    odd_count+=1
print(f"even{even_count}")
print(f"odd{odd_count}")      