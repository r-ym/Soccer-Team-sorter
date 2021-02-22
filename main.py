import csv
import random
import os

def generate_teams(total,teamsize):
    S = set()
    t1 = list(range(1,teamsize+1))
    S.update(t1)
    t2 = list(range(teamsize+1,teamsize*2+1))
    S.update(t2)
    ll = list(range(teamsize*2+1,total+1))
    S.update(ll)
    return(t1,t2,ll,S)

def generate_csv(iter,file):
    writer = csv.writer(file)
    writer.writerow(iter)
# def write_teams(col,file):


def shuffle_team(t1,t2,ll):
    teamsize = len(t1)
    t2 += ll
    ll = [t1.pop(0) for idx in range(len(ll))]
    t1 += t2
    random.shuffle(t1)
    tt1 = [t1.pop(0) for idx in range(teamsize)]
    tt2 = [t1.pop(0) for idx in range(teamsize)]
    return (tt1,tt2,ll)
        
def gen_row(t1,t2,total):
    row = [""]*total
    for i in range(1,len(t1)):
        row[t1[i]-1] = "X"
        row[t2[i]-1] = "O"
    row[t1[0]-1],row[t2[0]-1] = "XX","OO"
    return(row)

def main():
    with open('play.csv', 'w', newline='') as file:
        total = 12
        team_size = 5
        t1,t2,ll,S = generate_teams(total,team_size)
        generate_csv(S,file)
        keep_count = 3
        while keep_count != 0:
            G = set()
            while G != S:
                t1,t2,ll = shuffle_team(t1,t2,ll)
                g1 = False
                g2 = False

                for i in range(len(t1)):
                    if t1[i] in G:
                        continue
                    else:
                        G.add(t1[i])
                        t1.insert(0,t1.pop(i))
                        # print(t1)
                        g1 = True
                    break

                for i in range(len(t2)):
                    if t2[i] in G:
                        continue
                    else:
                        G.add(t2[i])
                        t2.insert(0,t2.pop(i))
                        # print(t2)
                        g2 = True
                    break
                # print(g1,g2)
                if g1 and g2:
                    # print("hi")
                    generate_csv(gen_row(t1,t2,total),file)
                else:
                    continue
            keep_count -= 1

    with open('play.csv') as f, open('game.csv', 'w') as fw:
        csv.writer(fw, delimiter=',').writerows(zip(*csv.reader(f, delimiter=',')))
    os.remove("play.csv")

main()