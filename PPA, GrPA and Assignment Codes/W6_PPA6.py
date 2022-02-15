def get_marks(scores_dataset, subject):
    """
    Get the marks scored by all students in subject
	
    Arguments:
        scores_dataset: list of dicts
        subject: string
    Return:
        marks: list of tuples of the form (string, int)
    """
    t=[]
    l=len(scores_dataset)
    for i in range(l):
        for e in scores_dataset[i]:
            if(subject==e):
                a=scores_dataset[i]['Name'],scores_dataset[i][subject]
                t.append(a)
    return t