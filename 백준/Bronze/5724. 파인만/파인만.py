while True :
  a = int(input())
  if a == 0 :
    break
  else :
    tmp = int((a*(a+1)*(2*a+1))/6)
    print(tmp)