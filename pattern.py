def pattern(n):
   i = n
   while i>=1:
      # printing stars
      print(" "*(n-i) + "* " * i)
      i-=1 
 
n = int(input('Enter the number of rows: '))
pattern(n)
i = 1
while i<=n:
     
      print(" "*(n-i) + "* " * i)
      i+=1 
 

n = int(input('Enter the number of rows: '))


pattern(n)