def sortReview(review):
    # split() to create list of words in review
    # set() to narrow copies of words in single review
    # count = dict() to begin 
    breakdown = review.split()
    breakdownset = set(breakdown)
    final = dict(breakdownset)
    return finalCount(final)

def finalCount(words):
    for word in words:
        if word in words:
            words += 1
        elif word not in words:
            counts[word] = 1
    return words
    

global output = dict()




 



