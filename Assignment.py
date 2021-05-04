# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:06:36 2021

@author: andre
"""

# Import the relevant packages from the python library.

# Import matplotlib which should import a library for creating static, animated, and interactive visualisations in the model. 
import matplotlib as mpl

# The following code sets up the matplotlib environment in tkinter to render the model to a tkinter canvas. This has to be imported before
# matplotlib.pyplot to ensure it works in the model.
mpl.use('TkAgg')

# Import the tkinter package from the python library to access the graphical user interface (GUI) toolkit.
import tkinter 

# Import matplotlib.pyplot which will allow f data to be plotted. This will be imported as plt to reduce complexity/risk of error.
# This module will then be reffered to as plt throughout. 
import matplotlib.pyplot as plt

# Import matplotlib.animation module, to allow animated/live charts to be created. Imported as 'anim' to reduce risk of error.
import matplotlib.animation as anim

# Import random should import the random module, which will allow the random functions within this module to be utilised.
import random 

# Import the agentframeworkassignment file, created as a python file, in order to import the agents class which contains functions 
# determining agent behaviour. This will be imported as af to minimise the risk of error throughout the work.
import agentframeworkassignment as af

# Import csv  from the python library to be able to parse or work with CSV files. 
import csv 

# Import  time to allow access to modules and functions that in some way represent time in the code.
import time 

# Import requests to allow HTTP requests to be made which reduces complexities behind the interface.
import requests

# Import bs4 to enable data to be pulled from HTML and XML files. This makes it easy to scrape information from web pages,
# providing idioms for iterating, searching, and modifying the parse tree, saving the user time. 
import bs4


# Begin timing how long the code will take to run
start = time.time()


# Set a new variable (f) to open the CSV file (in.txt), which contains the environmental data. 
f = open('in.txt', newline='')
# Set a new variable (reader) to read the environmental data into the model. 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# Create an empty list called 'environment' to shift the CSV data into a list, which will hold the environmental data.
environment = []
# Create a for-loop to make each row a new list which will store the CSV data.
for row in reader:
   # Initialise a new list (rowlist) in which values from the environmental data will be stored. 
   rowlist = []
   for value in row:
       # Before each row is processed append the values in each row of the data to the rowlist.
       rowlist.append(value)
   # Append the rowlist to the environment list so that the environment list stores the environmental data. 
   environment.append(rowlist)


# The following block of code tests that data has been properly appended to the environment list. 
# Print the first value in environment list - this is reffered to as [0][0] as in python the first value is refferred to as zero.
print(environment[0][0])
# Assess how long the environment list is - this should assign nrows and ncols to a number corresponding to the length of the rows
# and columns.
nrows = len(environment)
ncols = len(environment[0])
# Print the lengths of the rows and columns in the environment list.
print("nrows", nrows)
print(ncols)
# Print the last value in the environment list.
print(environment[nrows-1][ncols-1])
# Plot the environment data using the plt module - this should open a seperate window containing a plot of the environment.
plt.imshow(environment)
plt.show()


# Create an empty list called 'agents' to store the agent variables set out in agentframeworkassignment.py.
agents = []
# Create a new variable (num_of_agents) to assign how many agents (sheep) there will be. This can be changed to see how the model
# is affected when there are more or less sheep in the environment. 
num_of_agents = 60
# Create a new variable (num_of_iterations) to move the agents/sheep an arbitary number of times. This can be changed to represent 
# different behaviours.
num_of_iterations = 100
# Create a new variable (neighbourhood) to allow agents to search for close neighbours within a defined distance (20). This can be 
# changed to, again, represent different sheep behaviours.
neighbourhood = 20 
# Use random.seed(0) to initialise the pseudo-random number generator in python. This produces more deterministic random data that
# can be reproduced.
random.seed(50)


# The following code creates a new variable (r) which accesses data from the web. This scrapes the HTTP data, downloading 
# x and y variables associated with this webpage. 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# Print the variables from the x and y columns in the web dataset.
print(td_ys)
print(td_xs)


# To create a list of agent coordinates, obtained from a random location within the af file, the following code creates a for-loop 
# (for i in range), using the num_of_agents variable to determine the number of coordinates in the list.
for i in range(num_of_agents):
    # Initialise agent coordinates using data from the web. As web data only contains values between 0 and 100, this has to be 
    # multiplied by 3 to ensure agents are assigned values between 0 and 300, the size of the envrionment data.
    y = int((td_ys[i].text)*3)
    x = int((td_xs[i].text)*3)
    # The code will use the agents.append function to add these sets of coordinates to the empty agents list. At this point the 
    # environment list is passed into the agent constructor, along with the x and y variables.
    agents.append(af.Agent(environment, agents, y, x))


# Make a single agent, connecting the agentframeworkassignment file with this model.
a = af.Agent(environment, agents, y, x)
# Print the x and y variables defined within the af file to ensure the files are properly connected
print(a._y, a._x)
# Test that the variables move randomly, in the way set out in the af file. These values should be 2 less or 2 greater than those
# printed above.
a.move()
print(a._y, a._x)
# Test the eat() method defined in the af file to ensure it links properly to this model.This should print the same values as the move() 
# method above.
a.eat()
print(a._y, a._x)


# Define figure size and axes which, later in the model, should set figure parameters for plotting data in the GUI. 
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Create a global variable (carry_on) that can be utilised both inside and outside functions. This is always set as true unless
# stated otherwise.
carry_on = True


# Create a new function (update) to set the model up for animation, defined by the number of frames. This function should
# essentially give the model some behvaiour by randomly altering self._x and self._y coordinates.
def update(frame_number):
    # Call the global variable carry_on within the function. This is set as true as defined outside the function and remains
    # true until the model reaches a stopping condition.
    global carry_on 
    # Clear the figure before plotting the animation.
    fig.clear()  
    # Create a new empty variable within the function, to store how much the agents have eaten.
    agent_count = 0 
    
    if True: 
        # Pseudo-randomly shuffle the order in which agents are processed to reduce model artifacts (patterns or errors in the way 
        # the model runs).
        random.shuffle (agents)
        # Create a for-loop to give the agents (sheep) some behaviour by calling on the move, move_faster, eat and share_with_neighbours 
        # functions set out in agentframework. This executes the control statements once for each agent in the list. This should move the
        # sheep around the environment and depending on their stores will allow them to execute behaviours defined in agentframework.
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].move_faster()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
        # Still within the update function, create a second for-loop to initiate a stopping function that will stop the animation
        # when all of the agents (sheep) have a certain amount of food in their stores. 
        for i in range(num_of_agents):
            # Create a new variable (eaten_enough) and set this as the  full() function to test whether the sheep have eaten 
            # enough food. 
            eaten_enough = agents[i].full()
            # If eaten_enough is equal to one, indicating sheep are full, add 1 to the agent_count variable.
            if eaten_enough == 1:
                agent_count += 1
                # Test this works by printing the stores of each agent once they are full. This should equal around 1000, as set
                # out in the agentframework file.
                print("Agent", agents[i], "is full, their store is: {}".format(agents[i].store))
        # Once agent_count is equal to the num_of_agents, indicating the each agents stores are full, set carry_on to false to stop 
        # the animation and print a stopping condition.
        if agent_count == (num_of_agents):
            carry_on = False
            print("stopping condition")
            
    # Still inside the update function, use matplotlib.pyplot (imported as plt) to show the environment.
    plt.imshow(environment)
    # Set the y and x-axis limits equal to the length of the envrionment.
    plt.ylim(0, len(environment[0]))
    plt.xlim(0, len(environment))
    # Add a title to the animation.
    plt.title("Agent-based Model of Sheep Moving within an Environment")
    # Add x and y-labels to the axes.
    plt.ylabel("Environment")
    plt.xlabel("Environment")
    # Plot the agents in the environment using a scatter plot. Set the size of the points to 50. 
    # Create a for-loop so that agents with stores less than 500 should be blue and agents with stores greater than 500 should be red. 
    # Here, the y-coordinate will be referred to as agents[i]._y and the x-coordinate will be referred to as agents[i]._x as each agent 
    # can be referred to, simply, as agents[i].
    for i in range(num_of_agents):
        if agents[i].store < 500:
            plt.scatter(agents[i]._x,agents[i]._y, color='blue', s=50) 
        if agents[i].store > 500:
            plt.scatter(agents[i]._x,agents[i]._y, color='red', s=50)     
           
           
# Print the first set of agents in the list to ensure everything is working as it should be
print (agents[i]._y, agents[i]._x)                     


# The following code creates a generator function that loops the animation until num_of_iterations and the stopping condition have been 
# met/initialised.
def gen_function(b = [0]):
    a = 0
    # The next line of code is not actually needed as the carry_on variable has already been assigned. Nonetheless, it is clearer
    # to include this as it identifies that the model will continue to run while the carry_on variable is true.
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and awaits next call.
        a += 1               
    

# Lines 232-233 set up and show the animation. This should be uncommented if the user does not want to run the model
# in a GUI, although to do this lines 10-18 should be commented out using the '#' symbol, and any code after line 233 should
# also be commented out
#animation = anim.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#plt.show()


# The following code creates a function (run) to run an animation. This uses the FuncAnimation function in the animation module to create an 
# animation by repeatedly calling upon the update function. This uses the generator function to pass data in each frame of the animation
# and sets the canvas size to the pre-defined figure size. 
# canvas.draw() from the tkinter function is used to draw this animation within the canvas. The animation should stop running when the 
# sequence of frames is complete as repeat is set to False. 
def run():
    animation = anim.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()


# The following code builds the main GUI window by creating a new variable: root, which is where the animation should be displayed. 
root = tkinter.Tk()
# Give the GUI window a title.
root.wm_title("Agent-based Model of Sheep Moving within an Environment")
# Lay out a matplotlib canvas to be embedded within the GUI window using the figure parameters set out earlier in the model.
canvas = mpl.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# This next section of code creates a menu for the GUI window and associates this with the run function which will allow the GUI to
# run the animation.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
# Create a command using the 'run' function to allow the user to click run in the menu of the GUI window, which should then allow 
# the model to be run.
model_menu.add_command(label="Run model", command=run)


# The following line of code ends the timer that was initiated earlier in the code to establish how long the code takes
# to run.
end = time.time()


# Print the time it takes (in seconds) for code to run between the start and end variables.
print("time = " + str(end - start))


# Create a qutting function that will stop the code running when the GUI window is closed. This can be done before the animation
# has reached it's stopping condition, as well as when the animation has finished running.    
def exit():
    root.quit()
    root.destroy()
root.protocol('WM_DELETE_WINDOW', exit)


# This final line of code sets the GUI waiting for events and should allow the GUI to run the model effectively. This line of code must
# go at the very end.
tkinter.mainloop()







