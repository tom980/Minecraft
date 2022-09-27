import numpy as np
def reactor_calculation(x_const,y_const,z_const,blocks_in):
    # x_const=3
    # y_const=3
    # z_const=3
    # blocks_in = np.ones((x_const,y_const,z_const))
    blocks = np.zeros((x_const+2,y_const+2,z_const+2))
    blocks[1:-1,1:-1,1:-1] = np.array(blocks_in)
    basis_list = np.array([[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]])

    coeff_fn={0:1,1:3,2:6,3:10,4:15,5:21,6:28}

    heat = np.zeros((x_const+2,y_const+2,z_const+2))
    power = np.zeros((x_const+2,y_const+2,z_const+2))
    active = np.zeros((x_const+2,y_const+2,z_const+2))
    heat_coeff = 18.0
    power_coeff = 60.0

    tasklist1 = []
    tasklist2 = []
    tasklist3 = []
    tasklist4 = []
    tasklist5 = []
    task_ref = {1:tasklist1,2:tasklist2,3:tasklist3,4:tasklist3,5:tasklist3,6:tasklist4,7:tasklist3,8:tasklist3,9:tasklist4,10:tasklist4,11:tasklist5,12:tasklist5,13:tasklist5,14:tasklist3,15:tasklist4,16:tasklist4,17:tasklist3}

    for x, x_dir in enumerate(blocks[1:-1,1:-1,1:-1]):
        for y, y_dir in enumerate(x_dir):
            for z, z_dir in enumerate(y_dir):
                pos=(x+1,y+1,z+1)
                if blocks[pos]!=0:
                    task_ref[blocks[pos]].append(pos)

    for pos in tasklist1:
        if blocks[pos]==1:
            n=0
            for vector in basis_list:
                temppos=np.add(pos,vector)
                count=0
                while count<=4 and blocks[tuple(temppos)]==2:
                    count+=1
                    temppos=np.add(temppos,vector)
                if blocks[tuple(temppos)]==1:
                    n=n+1
            heat[pos]=coeff_fn[n]*heat_coeff
            power[pos]=(n+1)*power_coeff

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
                        if blocks[tuple(np.add(pos,vector))]==4 and active[tuple(np.add(pos,vector))]==1:
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

