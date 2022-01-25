# The Chessboard and checking legality of any Bishop's moves problem:-
list,a,b='ABCDEFGH',input(),input()
if abs(list.index(a[0])-list.index(b[0]))==abs(int(a[1])-int(b[1])):
    print('YES')
else:
    print('NO')