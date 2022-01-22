import random,copy
def randomWord(list):
    if len(list)>0:
        unique=copy.copy(list)
        while(True):
            ind=unique.index(random.choice(unique))
            yield unique[ind]
            unique.remove(unique[ind])
            if len(unique) == 0:
                unique = copy.copy(list)
    else:
        while (True):
            yield None