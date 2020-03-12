import time
import math
from os import system
nums = []
dimlist = []
dim = 1
max = 100
breakc =0 
total = 0
vcount = 0
globaldims = 1
possiblenums= 0
perc = 0
ov = input("Would you like to overwrite previous run? (y/n): ")
if ov == "y":
    overwrite = "w"
if ov == "n":
    overwrite = "a"

dim = int(input("Number of dimensions: ")) - 1
globaldims = dim + 1
max = int(input("Max starting value: "))
f = open(str(dim + 1) + "D" + str(max) + "M" ".txt", overwrite)
start = time.time()

possiblenums = (max -1) ** globaldims

while dim  > -1:
    dimlist.append(dim)
    dim -= 1
    nums.append(1)


print(dimlist)

while True:
    nums[0] +=1
    perc +=1
    for d in dimlist:
        d -=1 
        if nums[d] == max:
           
            
            nums[d] = 1
            nums[d+1] +=1
            breakc +=1


    for n in nums:
        total += n**2
    total = math.sqrt(total)
    if total.is_integer() == True:
        f.write(str(nums) + " " + str(total) + " VALID " + "\n")
        vcount +=1
    if nums[1] == 50:
        system('cls')
        print(str(round(((nums[globaldims - 1])/(max-1))*100 , 1)) + " %")
        middle = time.time()
        print(str(round(middle - start, 1)) + " secs since start")


    total = 0
    if breakc == 2:
        end = time.time()
        delta = end - start
        delta = round(delta, 3)
        print(str(delta) + " SECONDS")
        print(str(possiblenums) + " POSSIBLE CONFIGURATIONS")
        print(str(vcount / (globaldims)) + " VALID SIMPLEXES")
        f.write(str(delta)+ " seconds" + "\n")
        f.write(str(vcount) + " VALID SIMPLEXES" + "\n")
        f.write(str(possiblenums)+ " POSSIBLE CONFIGURATIONS" + "\n")
        f.write(str(globaldims) + " DIMENSIONS  +  " + str(max) + " MAX VALUE")
        f.close
        break
    breakc =0