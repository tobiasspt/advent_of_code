import numpy as np

#rotation matrices
Rx = np.array([[1,0,0],[0,0,-1],[0,1,0]])
Ry = np.array([[0,0,1],[0,1,0],[-1,0,0]])
Rz = np.array([[0,-1,0],[1,0,0],[0,0,1]])


def matmul(l):
    res = np.eye(3)
    for item in l:
        res = np.matmul(res,item)
    return res.astype(int)


def make_rotation1(point,num):
    
    c = 0
    l = []
    
    if num == 0:
        return point
    
    for x in range(4):
        
        l.append(Rx)
        c += 1
        if c == num:
            return matmul(l+[point])
    
        for y in range(4):
            
            l.append(Ry)
            c += 1
            if c == num:
                return matmul(l+[point])
            
            for z in range(4):
                
                l.append(Rz)
                c += 1
                if c == num:
                    return matmul(l+[point])
    
    
    
#% finding the 24 unique rotation matrices
rot_l = []
for i in range(4*4*4):
    rot_l.append(make_rotation1(np.eye(3), i))
rotL = []
for item in rot_l:
    if item.tolist() not in rotL: rotL.append(item.tolist())
rotM = []
for item in rotL:
    rotM.append(np.array(item))
def make_rotation(point,num):
    return matmul([rotM[num],point])

 

def rotate_scanner(scanner,num):
    s_rot = []
    for point in scanner:
        s_rot.append(make_rotation(point, num))    
    return s_rot
        
def shift_scanner(scanner,rel_pos):
    s_shift = []
    for point in scanner:
        s_shift.append([point[0]+rel_pos[0],point[1]+rel_pos[1],point[2]+rel_pos[2]])
    return s_shift

#%%

def have_overlap(s1,s2):
    
    for i in range(24):
        
        s2_rot = rotate_scanner(s2, i)
   
        #all points of s2 are translated to all points of s1
        for p1 in s1:
            
            for p2 in s2_rot:
                
                dx = p1[0]-p2[0]
                dy = p1[1]-p2[1]
                dz = p1[2]-p2[2]
        
                c = 0
                
                for item in s2_rot:
                    
                    item = list(item)
                    item[0]+=dx
                    item[1]+=dy
                    item[2]+=dz
                    
                    if item in s1:
                        c+=1
                        
                if c >= 12:
                    
                    return (True,i,[dx,dy,dz],)
                    
    return (False, None, None)

      
    
#%%

file = 'input.txt'

dic = {}

with open(file) as f:
    line  = 'x'
    c = -1
    
    while line :
        line = f.readline()
        
        if line == '':
            continue
        elif line == '\n':
            continue
            
        elif line[:2] == '--':
            c+= 1
            dic[c] = []
            
        else:
            words = line.strip().split(',')
            dic[c].append([int(words[0]),int(words[1]),int(words[2])])

dic_map = {}

for key in dic.keys():
    dic_map[key] = {}
    dic_map[key]['pos'] = dic[key]


dic_connected = {}
dic_connected[0] = dic_map[0]
dic_connected[0]['shift'] = [0,0,0]
dic_connected[0]['rot'] = 0
del dic_map[0]

dic_done   = {}


# looping over all the connected keys. adding not yet connected scanners to the
# connected list after rotating and shifting them
while len(dic_connected) > 0:
    con_keys = list(dic_connected.keys())
    
    for con_key in con_keys:
        
        keys = list(dic_map.keys())
        
        for key in keys:
            overlap, rot_num , rel_pos = have_overlap(dic_connected[con_key]['pos'], dic_map[key]['pos'])
            
            if overlap:
                p_new = shift_scanner(rotate_scanner(dic_map[key]['pos'], rot_num),rel_pos)
                
                dic_connected[key] = {'shift':rel_pos,'rot':rot_num,'pos':p_new}
                
                del dic_map[key]
        
        dic_done[con_key] = dic_connected[con_key]
        del dic_connected[con_key]
        
#

beacons = []
for key in dic_done.keys():
    
    beacons += dic_done[key]['pos']
    
unique_beacons = []
for b in beacons:
    if b not in unique_beacons: unique_beacons.append(b)
    
print(len(unique_beacons))

#%%

#largest manhatten metric between any two 
keys = list(dic_done.keys())
largest_mm = 0

for i in range(len(keys)-1):
    for j in range(i+1,len(keys)):
        k1 = keys[i]
        k2 = keys[j]
        
        pos1 = dic_done[k1]['shift']
        pos2 = dic_done[k2]['shift']
        
        mm = np.sum(np.abs(np.array(pos1)-np.array(pos2)))
        # print(mm)
        if mm > largest_mm:
            largest_mm = mm
print(largest_mm)
        
        