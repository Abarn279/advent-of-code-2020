import sys 

with open('./inp/13.txt') as f:
    start = int(f.readline())
    bus_ids = list(map(int, (i for i in f.readline().split(',') if i.isdigit())))

def get():
    for time in range(start, sys.maxsize):
        for bus in bus_ids: 
            if time % bus == 0: 
                return (time - start) * bus

print(get())