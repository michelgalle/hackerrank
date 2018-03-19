n = int(input())
stack = []
stri = ''
for i in range(n):
    l = list(input().split())
    if(int(l[0]) == 1):
        stri += str(l[1])
        stack.append(len(str(l[1])))
    if(int(l[0]) == 2):
        stack.append(stri[-int(l[1]):])
        stri = stri[:-int(l[1])]
    if(int(l[0]) == 3):
        print(stri[int(l[1]) - 1])
    if(int(l[0]) == 4):
        x = stack.pop()
        if(type(x) is int):
            stri = stri[:-x]
        else:
            stri+=x