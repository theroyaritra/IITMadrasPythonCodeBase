def collection_to_file(scores_dataset):
    """
    Convert a collection to a file

    Argument:
        scores_dataset: list of dicts
    Return:
        None
    """
    f=open('scores.csv','w')
    f.write("SeqNo,Name,Gender,City,Mathematics,Physics,Chemistry"+'\n')
    for each in scores_dataset:
        s=''
        s+=str(each['SeqNo'])+','+each['Name']+','+each['Gender']+','+each['City']+','+str(each['Mathematics'])+','+str(each['Physics'])+','+str(each['Chemistry'])+'\n'
        f.write(s)
    f.close()