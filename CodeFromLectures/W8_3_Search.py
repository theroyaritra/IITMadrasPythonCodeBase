def obvious_search(l,x):
    for e in l:
        if(e==x):
            return True
    return False
#print(obvious_search([58,96,57,25,-96],69))