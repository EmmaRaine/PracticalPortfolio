# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:17:26 2021

@author: andre
"""
# Import the random module to allow random functions to be utilised within the code.

import random

# The following code sets up an agent class using the init method to defines agent attributes.
# All object methods require a parameter label to assign to the object; this is self label and essentially means that those 
# x and y values belong to that class.

class Agent():
    def __init__(self, environment, agents, y, x):
        # Set up the envrionment that the agents will move around and eat.
        self.environment = environment
        # Set up a variable used when calling upon agents to share their stores.
        self.agents = agents
        # Define the store of each agent, which will increase as they consume more of the environment.
        self.store = 0 
        # Define the random starting location for each of the agents. This should be within the envrionment given
        # the parameters for this are set as the environment length.
        self._x = random.randint(0, len(environment[0])) 
        self._y = random.randint(0, len(environment))
        # Create a for-loop indicating that when x and y variables are equal to none, then the agent location can be determined by
        # the parameters set out above.
        if (x == None):
            self._x = random.randint(0, len(environment[0]))
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0, len(environment))
        else:
            self._y = y


# The following code makes a move() method within the Agent class. The code will randomly alter the self._x and self._y coordinates 
# using control flow (if-else) statements. The if statement contains a block of code that evaluates a condition and makes a choice. 
# An else statement contains the block of code that executes, if the condition in the if statement is not met.

# If the store of each agent is less than 500, this code will generate a random floating number between 0 and 1 using the 
# random.random() function from the random module. The code should randomly move the coordinates 2 steps depending on which conditions 
# are met; if random.random() is less than 0.5 self.x/self.y coordinates will increase by 2 and if random.random() is greater than 0.5
# self.x/self.y coordiantes will decrease by 2. 

# To deal with boundary issues, a common solution is to allow points leaving the top of an area to come in at the bottom and leaving 
# left, come in on the right (making the space into a Torus). The following code uses the modulus operator (%) which gives and 
# plots the remainder of a division, to ensure agents don't go missing. This is set to 300, the size of the environment to ensure agents
# cannot go missing out of the environment.

    def move(self):
        if self.store < 500:
            if random.random() < 0.5:
                self._x = (self._x + 2) % 300
            else:
                self._x = (self._x - 2) % 300
    
            if random.random() < 0.5:
                self._y = (self._y + 2) % 300
            else:
                self._y = (self._y - 2) % 300
 
    
# The following code creates a move_faster function in the Agent class. This allows the agents to move faster when they have more
# energy (a greater amount of food in their stores).

# This uses the same code as the move method, although if the store of each agent is greater than 500, x and y-coordinates will
# increase or decrease by 5, depending on the random integer that is generated. 

    def move_faster(self):
        if self.store >= 500:
            if random.random() < 0.5:
                self._x = (self._x + 5) % 300
            else:
                self._x = (self._x - 5) % 300
    
            if random.random() < 0.5:
                self._y = (self._y + 5) % 300
            else:
                self._y = (self._y - 5) % 300
                
                      
# The following code makes an eat() method within the Agent class that allows the agents to edit the environment.

# When self._x and self._y are greater than 10, the agents will eat the environment (environment will lose 10). This should be
# added to the agents store. 

    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10


# The following code creates a function to check the agents stores. 
# Create a for-loop that changes the 'full' variable when agents have a certain amount of food in their stores. 

    def full(self):
        if self.store >= 1000: 
            full = 1     # If an agents store is greater than 1000, set the full variable to 1.
        if self.store < 1000:
            full = 0     # Otherwise, the full variable is set to 0. 
        return full


# The following code calculates the euclidean/straight-line distance between the agents using pythagoras theorem.

    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    
# The following code makes a share_with_neighbours() function within the Agent class allowing agents to share their food stores. 
# This code will allow the agent to call upon the function to check their neighbourhood; essentially, this will allow the agent to search 
# for close neighbours and share resources with them.

    def share_with_neighbours(self, neighbourhood):
        # Create a for-loop that calls upon the distance_between() function to search for nearby neighbours. Store this in a new variable:
        # dist.
        for agent in self.agents:
            dist = self.distance_between(agent)
            # If the distance between the agents is less than or equal to the neighbourhood (defined in the model):
            if dist <= neighbourhood: 
                # Add the stores of each agent together
                sum = self.store + agent.store
                # Divide this total by 2 to work out the average stores.
                average = sum /2
                # Set the store of each agent to that average.
                self.store = average
                agent.store = average
                # The following code prints the code above to test that it is working
                #print("sharing " + str(dist) + " " + str(average))
                          
                
# The following three blocks of code implements a property attribute for each of the coordinates, using appropriate set and get methods.          
# The following code sets the propery x and y. 
                 
    @property        
    def x(self):
        return self._x
    def y(self):
        return self._y
        
# The following code uses the get function to obtain an attribute value for x and y. 

    def getx(self):
        return self._x
    def gety(self):
        return self._y
    
# The following code uses the set function to set the attribute values for x and y.

    def setx(self, value):
        self._x = value 
    def sety(self, value):
        self._y = value
