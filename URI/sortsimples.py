n, nd, nt = input().split(" ")

n = int(n)
nd = int(nd)
nt = int(nt)

if(n < nd and n < nt):
    if(nd < nt):
        print(str(n)+"\n"+str(nd)+"\n"+str(nt))
    if(nd > nt): 
        print(str(n)+"\n"+str(nt)+"\n"+str(nd))
elif(n > nd and n > nt):
    if(nd < nt):
        print(str(nd)+"\n"+str(nt)+"\n"+str(n))
    if(nd > nt): 
        print(str(nt)+"\n"+str(nd)+"\n"+str(n))
elif(n < nd and n > nt):
        print(str(nt)+"\n"+str(n)+"\n"+str(nd))
elif(n > nd and n < nt):
        print(str(nd)+"\n"+str(n)+"\n"+str(nt))

print("")

print(str(n)+"\n"+str(nd)+"\n"+str(nt))