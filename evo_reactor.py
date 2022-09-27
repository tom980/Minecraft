import numpy as np
import random
import ReactorFitness
import matplotlib.pyplot as plt
import os

def breed(reactor1,reactor2):
    #Create the empty output
    output = np.zeros((x_size,y_size,z_size))

    #Randomly choose a cutoff where we switch from one parent to another
    cutoff = random.randint(0,total_size)
    count = 0
    for i in range(x_size):
        for j in range(y_size):
            for k in range(z_size):
                if count >= cutoff:
                    output[i,j,k] = reactor1[i,j,k]
                else:
                    output[i,j,k] = reactor2[i,j,k]
                count+=1
    
    #Add a random chance for mutation
    prob = random.random()
    if prob<=0.1: #0.01 chance of one block randomly mutating
        for i in range(3):
            randx = random.randint(0,x_size-1)
            randy = random.randint(0,y_size-1)
            randz = random.randint(0,z_size-1)
            output[randx,randy,randz] = random.randint(0,17)
    if prob>=0.9:
        randx1 = random.randint(0,x_size-1)
        randy1 = random.randint(0,y_size-1)
        randz1 = random.randint(0,z_size-1)
        randx2 = random.randint(0,x_size-1)
        randy2 = random.randint(0,y_size-1)
        randz2 = random.randint(0,z_size-1)
        output[randx1,randy1,randz1],output[randx2,randy2,randz2] = output[randx2,randy2,randz2],output[randx1,randy1,randz1]
    
    #Return
    return output

def init_population(pop_size):
    #Initilise populatin with random designs
    population = []
    for _ in range(pop_size):
        population.append(np.random.randint(0,18,size=(x_size,y_size,z_size)))
    return population

def fitness_learn(reactor):
    #A fitness function intended to improve learning
    heat,power = ReactorFitness.reactor_calculation(x_size,y_size,z_size,reactor)
    if np.sum(heat) > 0:
        #Including heat in evaluation allows heat generating reactors but strongly
        #penalises excess heat
        return 0
        return np.sum(power)-np.sum(heat)*10
    else:
        #This gives incentive to minimise heat. Small coefficent prioritises power
        return np.sum(power)-np.sum(heat)*0.4

def fitness_power(reactor):
    #A fitness function to evaluate heat neutral reactors
    heat,power = ReactorFitness.reactor_calculation(x_size,y_size,z_size,reactor)
    if np.sum(heat) > 0:
        return 0
    else:
        return np.sum(power)

def iterate_pop(population,function):
    #Given the population and a fitness function this iterates by one generation
    
    pop_size = len(population)
    newpop = population[:int(pop_size*0.2)] #Keep the best 20%
    population = population[:int(pop_size*0.5)] #Use the best 50% for breeding

    #Repopulate the list back to its original size
    while len(newpop) < pop_size:
        p1 = random.choice(population)
        p2 = random.choice(population)
        newpop.append(breed(p1,p2))
    
    #Sort the list using the fitness function to evaluate designs
    population = newpop
    population.sort(reverse=True,key=function)
    
    return population

#Some constants for the problem
x_size = 3
y_size = 3
z_size = 3
total_size = x_size*y_size*z_size
pop_size = 15

#Initilise the population
population = init_population(pop_size)
population.sort(reverse=True,key=fitness_learn)

#Initilise these to keep track of progress
iteration = [0]
max_power = [0]

#Setup the plotting
figure = plt.figure()
const_line = plt.plot(np.linspace(0,3000,3001),np.linspace(2880,2880,3001))
line1, = plt.plot(iteration,max_power,'-')

#Each loop is one iteration
for i in range(1,3000):
    #Iterate the system
    population = iterate_pop(population,fitness_learn)
    
    #Keep track of the progress
    iteration.append(i)
    max_power.append(fitness_power(population[0]))
    
    #Print the current best design and its power
    os.system('cls')
    print(i,max_power[-1],fitness_learn(population[0]), "Fitness_Learn")
    print(population[0])
    
    #Update the graph being shown
    #line1.set_data(iteration,max_power)
    #figure.gca().relim()
    #figure.gca().autoscale_view()
    #plt.pause(0.0001)

#Print the final best design
print(population[0])
print(ReactorFitness.reactor_calculation(x_size,y_size,z_size,population[0]))
