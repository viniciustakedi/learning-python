info_one = input()  
info_two = input() 
info_thr = input()  

if info_one == "vertebrado":
    if info_two == "ave":
        if info_thr == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if info_thr == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if info_two == "inseto":
        if info_thr == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if info_thr == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
