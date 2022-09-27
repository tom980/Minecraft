import numpy as np

def reactor_calculation(x_const,y_const,z_const,blocks_in):
    # x_const=3
    # y_const=3
    # z_const=3
    # blocks_in = np.ones((x_const,y_const,z_const))

    blocks = np.zeros((x_const+2,y_const+2,z_const+2))
    blocks[1:-1,1:-1,1:-1] = blocks_in
    basis_list = np.array([[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]])

    coeff_fn=[1,3,6,10,15,21,28]

    heat = np.ones((x_const+2,y_const+2,z_const+2))
    power = np.ones((x_const+2,y_const+2,z_const+2))
    active = np.zeros((x_const+2,y_const+2,z_const+2))

    for x, x_dir in enumerate(blocks[1:-1,1:-1,1:-1]):
        for y, y_dir in enumerate(x_dir):
            for z, z_dir in enumerate(y_dir):
                pos=[x+1,y+1,z+1]
                if blocks[tuple(pos)]==1:
                    n=0
                    for vector in basis_list:
                        pos=np.add([x+1,y+1,z+1],vector)
                        count=0
                        while count<=4 and blocks[tuple(pos)]==2:
                            count+=1
                            pos=np.add(pos,vector)
                        if blocks[tuple(pos)]==1:
                            n=n+1
                    heat[x+1,y+1,z+1]=coeff_fn[n]
                    power[x+1,y+1,z+1]=n+1

    for x, x_dir in enumerate(blocks[1:-1,1:-1,1:-1]):
        for y, y_dir in enumerate(x_dir):
            for z, z_dir in enumerate(y_dir):
                pos=[x+1,y+1,z+1]
                if blocks[tuple(pos)]==2:
                    n=0
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==1:
                            heat[tuple(pos)]=heat[tuple(pos)]+heat[tuple(np.add(pos,vector))]/3
                            power[tuple(pos)]=power[tuple(pos)]+power[tuple(np.add(pos,vector))]/3
                            n=n+1
                            active[tuple(pos)]=1
                    if n==0:
                        heat[tuple(pos)]=1
                        power[tuple(pos)]=0
                    
    for x, x_dir in enumerate(blocks[1:-1,1:-1,1:-1]):
        for y, y_dir in enumerate(x_dir):
            for z, z_dir in enumerate(y_dir):
                pos=[x+1,y+1,z+1]
                if blocks[tuple(pos)] == 3:
                    check=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==1 or (blocks[tuple(np.add(pos,vector))]==2 and active[tuple(np.add(pos,vector))]==1):
                            check=True
                    if check:
                        heat[tuple(pos)]=-60
                        active[tuple(pos)]=1
                elif blocks[tuple(pos)] == 4:
                    check=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==1:
                            check=True
                    if check:
                        heat[tuple(pos)]=-90
                        active[tuple(pos)]=1
                elif blocks[tuple(pos)] == 5:
                    check=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==2 and active[tuple(np.add(pos,vector))]==1:
                            check=True
                    if check:
                        heat[tuple(pos)]=-90
                        active[tuple(pos)]=1
                elif blocks[tuple(pos)] == 8:
                    check=False
                    check2=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==1:
                            check=True
                        if blocks[tuple(np.add(pos,vector))]==0:
                            check2=True
                    if check and check2:
                        heat[tuple(pos)]=-120
                        active[tuple(pos)]=1
                elif blocks[tuple(pos)] == 7:
                    check=0
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==2 and active[tuple(np.add(pos,vector))]==1:
                            check=check+1
                    if check>=2:
                        heat[tuple(pos)]=-130
                        active[tuple(pos)]=1
                elif blocks[tuple(pos)] == 14:
                    check1=False
                    check2=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==1:
                            check1=True
                        if blocks[tuple(np.add(pos,vector))]==2 and active[tuple(np.add(pos,vector))]==1:
                            check2=True
                    if check1 and check2:
                        heat[tuple(pos)]=-160
                        active[tuple(pos)]=1
                elif blocks[tuple(pos)] == 17:
                    check1=False
                    check2=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==0:
                            check1=True
                        if blocks[tuple(np.add(pos,vector))]==2 and active[tuple(np.add(pos,vector))]==1:
                            check2=True
                    if check1 and check2:
                        heat[tuple(pos)]=-110
                        active[tuple(pos)]=1

    for x, x_dir in enumerate(blocks[1:-1,1:-1,1:-1]):
        for y, y_dir in enumerate(x_dir):
            for z, z_dir in enumerate(y_dir):
                pos=[x+1,y+1,z+1]
                if blocks[tuple(pos)]==6:
                    check1=False
                    check2=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==3 and active[tuple(np.add(pos,vector))]==1:
                            check1=True
                        if blocks[tuple(np.add(pos,vector))]==4 and active[tuple(np.add(pos,vector))]==1:
                            check2=True
                    if check1 and check2:
                        heat[tuple(pos)]=-120
                        active[tuple(pos)]=1
                if blocks[tuple(pos)]==9:
                    check1=False
                    check2=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==3 and active[tuple(np.add(pos,vector))]==1:
                            check1=True
                        if blocks[tuple(np.add(pos,vector))]==5 and active[tuple(np.add(pos,vector))]==1:
                            check2=True
                    if check1 and check2:
                        heat[tuple(pos)]=-150
                        active[tuple(pos)]=1
                if blocks[tuple(pos)]==10:
                    check1=0
                    check2=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==3 and active[tuple(np.add(pos,vector))]==1:
                            check1=check1+1
                        if blocks[tuple(np.add(pos,vector))]==0:
                            check2=True
                    if check1==1 and check2:
                        heat[tuple(pos)]=-140
                        active[tuple(pos)]=1
                if blocks[tuple(pos)]==15:
                    check1=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==7 and active[tuple(np.add(pos,vector))]==1:
                            check1=True
                    if check1:
                        heat[tuple(pos)]=-80
                        active[tuple(pos)]=1
                if blocks[tuple(pos)]==16:
                    check1=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==8 and blocks[tuple(pos-vector)]==8 and active[tuple(np.add(pos,vector))]==1 and active[tuple(pos-vector)]==1:
                            check1=True
                    if check1:
                        heat[tuple(pos)]=-120
                        active[tuple(pos)]=1

    for x, x_dir in enumerate(blocks[1:-1,1:-1,1:-1]):
        for y, y_dir in enumerate(x_dir):
            for z, z_dir in enumerate(y_dir):
                pos=[x+1,y+1,z+1]
                if blocks[tuple(pos)]==13:
                    check1=False
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==6 and active[tuple(np.add(pos,vector))]==1:
                            check1=True
                    if check1:
                        heat[tuple(pos)]=-80
                        active[tuple(pos)]=1
                if blocks[tuple(pos)]==11:
                    check1=0
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==0 and blocks[tuple(np.add(pos,-1*vector))]!=0:
                            check1=check1+1
                    if check1==3:
                        heat[tuple(pos)]=-120
                        active[tuple(pos)]=1
                if blocks[tuple(pos)]==12:
                    check1=0
                    for vector in basis_list:
                        if blocks[tuple(np.add(pos,vector))]==1:
                            check1=check1+1
                    if check1>=2:
                        heat[tuple(pos)]=-160
                        active[tuple(pos)]=1

    return [heat[1:-1,1:-1,1:-1],power[1:-1,1:-1,1:-1]]

reactor_calculation(3,3,3,np.ones((3,3,3)))

x_size=3
y_size=3
z_size=3

max_num = 3**(x_size*y_size*z_size)

design = np.zeros((x_size,y_size,z_size))

best_design = np.zeros((x_size,y_size,z_size))
best_power = 0

for i in range(10):
    design = np.random.randint(0,4,size=(x_size,y_size,z_size))

    for x, x_dir in enumerate(design):
        for y, y_dir in enumerate(x_dir):
            for z, z_dir in enumerate(y_dir):
                if design[x,y,z] == 3:
                    design[x,y,z]=np.random.randint(3,18)

    test_heat_mat, test_power_mat = reactor_calculation(x_size, y_size, z_size, design)
    test_heat = np.sum(test_heat_mat)
    test_power = np.sum(test_power_mat)

    if test_power > best_power:
        print(i,test_heat, test_power)
        best_design = design
        best_power = test_power
        #print(best_design)
temp = reactor_calculation(3,3,3,np.array([[[12,12,11],[1,1,1],[11,12,12]],[[1,1,12],[1,12,1],[12,1,1]],[[12,1,12],[12,1,1],[11,1,1]]]))
print(np.sum(temp[0]),np.sum(temp[1]))