import winsound
r = 600  # hz, change this as needed
g = 2 ** (1.0 / 12.0)
Sa = r
Re_k = r * g
Re = r * g ** 2
Ga_k = r * g ** 3
Ga = r * g ** 4
Ma = r * g ** 5
Ma_t = r * g ** 6
Pa = r * g ** 7
Dha_k = r * g ** 8
Dha = r * g ** 9
Ni_k = r * g ** 10
Ni = r * g ** 11

song_list=[Dha_k,Ni_k,Ni,Ni_k,Ma_t,Ni_k,Dha_k,Ma_t,Ma,Dha_k,Ma_t]

for j in range(1):
    for i in song_list:
        print(i)
        winsound.Beep(int(i),1000)

