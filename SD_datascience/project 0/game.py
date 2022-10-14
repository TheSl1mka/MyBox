"""Game for found num"""

import numbers
import numpy as np

number = np.random.randint(1, 101) #make a num

#count of truing
count = 0

while True:
    count+=1
    predict_number = int(input("Make ur choose: "))
    
    if predict_number > number:
        print("make lower")
    elif predict_number < number:
        print("make upper")
        
    else:
        print(f"YES!, It's {number}, for just {count} tryies")
        break #the end