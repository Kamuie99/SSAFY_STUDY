'''
2
홍길동 95
이순신 77
'''
T = int(input())
sco_dict = {}
for t in range(T):
    k, v = input().split()
    sco_dict[k] = int(v)
# print(sco_dict)

sco_lst = []
for d in sco_dict:
    sco_lst.append(sco_dict[d])

sco_lst.sort()
rank = []
for s in sco_lst:
    for key in sco_dict:
        if s == sco_dict[key]:
            rank.append(key)

print(rank)

