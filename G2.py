# Write the generator Function to print prime Numbers.

print("Please specify range for prime numbers.")

start = int(input("from: "))
end = int(input("upto: "))
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i)