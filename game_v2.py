"""Game for found num: comp is making and comp is finding"""

import numbers
import numpy as np

def random_predict(number:int=1) -> int: #make a num
    """Random finding
    Args:
        number (int, optional): making bum, defaults to 1.
        
    Returns:
        int: count of tryes
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) #trying
        if number == predict_number:
            break #quit
    return count

def score_game(random_predict) -> int:
    """how many tryies at circle for 1000 tryies

    Args:
        randon_predict ([type]): func of finding

    Returns:
        int: circle count
    """
    count_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(1, 101, size=(1000)) #list on nums

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ur func finding a num at a cirlce for {score} tryies')
    return score
    
if __name__ == '__main__':
    score_game(random_predict)