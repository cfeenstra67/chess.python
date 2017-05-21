from collections import namedtuple

def conflicting(pos1,pos2):
    x1,y1,x2,y2=(*pos1,*pos2)
    dx,dy=(abs(x1-x2),abs(y1-y2))
    if (dx==0 or dy==0 or dx==dy): return True
    return False

side_length=8
start_position=(0,0)

def next_pos(pos,dim):
    x,y=pos
    if (x+1)>=dim: x,y=0,y+1
    else: x+=1
    if y>=dim: return start_position
    return (x,y)
    
def add_pos(*existing,target):
    for pos in existing: 
        if conflicting(pos,target): return None
    return (*existing,target)
        

def queen_locations(num_queens=side_length,s_length=side_length):
    def locs_w_start(start_loc):
        cursor=start_loc
        positions=()
        while len(positions)<num_queens:
            attempt=add_pos(*positions,target=cursor)
            cursor=next_pos(cursor,s_length)
            if not attempt is None: positions=attempt
            if cursor==start_loc: return None
        return positions
    start=start_position
    start=next_pos(start,s_length)
    while start!=start_position:
        result=locs_w_start(start)
        if not result is None: return result
        start=next_pos(start,s_length)
    return None

if __name__=='__main__':
    import time
    good=[]
    start=time.time()
    for i in range(1,25):
        works=(not queen_locations(i,i) is None)
        if works: good.append(i)
        print(str(i)+":"+str(works))  
    end=time.time()
    elapsed=end-start
    print({'time elapsed':elapsed,'possible n queen board setups':good})