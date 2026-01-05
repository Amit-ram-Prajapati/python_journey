evenSum = 0
oddSum = 0
for x in range(1,11):
  if(x%2 == 0):
    evenSum += x;
  else:
    oddSum += x;
print("evenSum : " , evenSum)
print("oddSum : " , oddSum)
