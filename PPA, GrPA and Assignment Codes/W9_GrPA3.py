def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return: 
        result: tuple, (integer, integer)
    """
    f=open(filename,'r')
    s=f.readlines()[1:]
    f.close()
    num_players,num_goals=0,0
    m=False
    for line in s:
        x=line.strip().split(',')
        if(x[1]==country):
            num_players+=1
            num_goals+=int(x[2])
            m=True
    if(m):
        return (num_players,num_goals)
    return (-1,-1)