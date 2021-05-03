# GEOG5990: Assignment 1- Agent-based Modelling

#### This repository contains the work developed during the practical sessions associated with the 'programming for geographical information analysis' module. This work has been produced in a python console, using the Spyder application. This README file will provide a brief overview of what files are included in this repository, what these files are and do, how the model can be run, issues encountered in the model, tests completed to ensure model functionality and finally opportunities for future development. 

Overall, this work aims to present an animation of the movement of sheep around an environment, modelling their eating behvaiour and how the sheep share their food stores. This model should:

* build agents in a space
* get agents to interact with each other
* read in environmental data
* get agents to interact with the environment
* randomise the order of agent actions
* display the model as a fully functioning animation
* contains the model within a graphical user interface (GUI)
* be initialised using data from the internet

### Repository contents

#### agentframeworkassignment.py

This file contains the agent class that defines a variety of functions to determine agent (sheep) behvaiour.
This includes code that does the following:

* places the agents at a random starting point wihtin the environment
* randomly moves the sheep using control-flow statements
* makes the sheep eat the environment to increase their food stores
* makes the sheep share food stores depending on their distance to nearby sheep in a given neighbourhood size (defined in the final model)

#### assignment.py

This file is responsible for running the agent-based model allowing, ultimately, the animation to be shown within a GUI. This includes a number of adaptable variables that can be changed to reflect and represent different sheep behaviours, creating a flexible model. To change these variables, the number to which they are assigned can be altered.

These variables include:

* **num_of_agents**: the number of sheep within the environment
* **num_of_iterations**: how many times sheep are able to be moved
* **neighbourhood**: the distance between the sheep before they start sharing their food stores
* **num_of_steps**: how many times agents will be run through the for-loop within the update function that sets the animation


This code will run continually as an animation until a stopping condition, which suggests the sheep’s stores are full, is met.  At this point, the IPython console should print 'Stopping condition'. This animation can be viewed in a graphical user interface (GUI). When the model is run a seperate window should appear. This should contain a menu with the word model and a dropdown list that says run model. If this is selected the model should run in this GUI window. 

#### in.txt

This file is a text file which contains the environment data. This was read into the model to enable to environment to be plotted and the agents to interact with it. In order for this to be used in the model, it has to be saved in the same directory in which the models are being created.

### Issues encountered when running the model

One issue encountered in the model is that when the animation begins running, the agents are all located in the bottom left-corner of the plot. While they do move around the environment as the animation continues, it is unclear why they exhibit this behaviour. This issue arose when the scale of plot was changed. Inititally, the x and y axis were set to start at 0 and end at 100. Once the animation was working this was changed so that the axes represented the length of the environment. This was solved by...

A further issue with the model is that when the model is run in the GUI, a seperate, blank figure opens at the same time as the GUI window. This is not and error with the code but a problem that arises when using spyder to run a GUI, thus could not be rectified. It is likely that in another application this would not be an issue, although this has not been tested. Nonetheless, this isssue is nothing more than a minor inconvenience and does not cause any problems.

Finally, while this is not necessarily an issue, there is some inconvenience when running the model in the GUI. To run the model in a GUI, the Spyder IPython console should to be set to Tkinter. To do this, the backend of the IPython console should be changed to TKinter. To do this on spyder go to tools > Ipython console > graphics > backend > TKinter. The console then has to be restarted to run the model in the GUI. The TKinter backend also produces a few issues within the IPython console such as slowing down the programme or not running the code. Mostly, this can be rectified by running "%gui tk" through the console. The model can be run without the GUI to avoid some of this inconvenience using the automatic backend and commenting out lines ... to ... and commenting in lines ... to ... This opens the animation in a seperate window that should run the model automatically.

### Model testing

The print() function was used to test the model. Throughout the code, this function was used to print a specified message to the screen. This ensured that what was expected of certain functions, methods and variables was returned in the model. This reveals what is going on inside the code to ensure it was running as it should be. 
In additon to using the print() function, the built-in debugger menu in spyder was used after any additions or alterations to the code in order to 'debug' it. This enabled what is going on in the program to be identified.

### Future development

While this model encapsulates a few different behaviours of the sheep within the environment, there are still other options for enhancing the model further. 
This model speeds up the agents as they increase their stores and makes the agents stop eating once they are full. However, further model enhancement could include making agents steal more resources from other agents if their stores are low, which could be done through adapting the share with neighbours function in agentframeworkassignment.py.
Additionally, the model could add in a new type of agent such as introducing a predator to eat nearby sheep. This would involve developing another agent class for the preadator and defining within that a series of functions that would allow them to move around the environment, eat the environment and eat nearby sheep. 

This is just two examples of how the model could be enhanced although there are many more options such as creating a complete population model inckuding breeding of sheep and wolves.
