import sys
import statistics

f = open(sys.argv[1])
B, L, D = map(int, f.readline().split())
B_val = {}

for i, v in enumerate(f.readline().split()):
    B_val[i] = int(v)

B_mew = statistics.mean(B_val.values())
B_st = statistics.stdev(B_val.values())

Libs = []
for i in range(L):
    Libs.append([i, list(map(int, f.readline().split())), list(map(int, f.readline().split()))])

Set_Books = set()

# [i, [N, T, M], [IDs]]
def Score(i):
    No_of_books = min((D - i[1][1]) * i[1][2], i[1][0])
    s = sum(
            sorted(
                map(lambda x: B_val[x], 
                    filter(lambda x: x not in Set_Books,
                           [j for j in i[2]]
                           )
                ),
                reverse=True
                )[:No_of_books]
            )
    # print(s, i)
    return (s / i[1][1]) * (sum(i[2]) - B_mew) / (B_st + 0.1)
        


Libs.sort(key=Score, reverse=True)

s = ''
n = 0
while D > 0 and len(Libs):
    if n % int(L**0.5) == 0:
        Libs.sort(key=Score, reverse=True)
    i = Libs.pop(0)

    No_of_books = min((D - i[1][1]) * i[1][2], i[1][0])

    _ = sorted(filter(lambda x: x not in Set_Books, [j for j in i[2]]),
                key= lambda x: B_val[x], 
                reverse=True)[:No_of_books]
    
    if len(_) != 0:
        Set_Books.update(set(_))
        No_of_books = len(_)
        
        s += str(i[0]) + ' ' + str(No_of_books) + '\n'
        s += str(_)[1:-1].replace(',', '') + '\n'

        D -= i[1][1]
        n += 1
    

print(n)
print(s)
