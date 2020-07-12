
def most_frequent():
    string=input("enter any word or statement to count character ")
    mydict={}
    for i in range(0,len(string)):
        if string[i] in string[:i]:
            continue
        else:
            c=string.count(string[i])
            mydict[string[i]]=c
       

    print(sorted(mydict.items(),key = lambda mydict:mydict[1],reverse=True))

most_frequent()
