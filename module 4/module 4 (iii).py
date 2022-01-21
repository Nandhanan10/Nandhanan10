def datatype (a, b, c, d, e, f, g):
    myinteger = a
    myfloat = b
    myboolean = c
    mystring = d
    mylist = e
    mytuple = f
    mydict = g
    print(f'\nI have a integer :{myinteger}, \nwith a float : {myfloat}, \nhaving a boolean : {myboolean}, \nfollowed by a string : {mystring}, \nforming a list : {mylist},'
          f'\nwith a tuple : {mytuple}, \nin a dictionary : {mydict}')

a = int(input('Type an integer'))
b = float(input('Type a float'))
c = bool(input('Give true or flase'))
d = str(input('Type a name'))
e = list(input('Give a list without comma'))
f = tuple(input("Enter a tuple without comma"))
g = {}
name = input("Enter a Name")
age = int(input("Enter age"))
g.update({name: age})

datatype(a, b, c, d, e, f, g)

