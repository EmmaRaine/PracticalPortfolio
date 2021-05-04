# GEOG5990: Assignment 1- Agent-based Modelling

#### This repository contains the work developed during the practical sessions associated with the 'programming for geographical information analysis' module. This work has been produced in a python console, using the Spyder application. This README file will provide a brief overview of what files are included in this repository, what these files are and do, how the model can be run, issues encountered in the model, tests completed to ensure model functionality and finally opportunities for future development. 

Overall, this work aims to present an animation of the movement of sheep around an environment, modelling different behaviours. This model should:

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

* places the agents at a random starting point within the environment
* randomly moves the sheep around the environment using control-flow statements
* makes the sheep move faster when they have more energy (greater amount of food in their stores)
* makes the sheep eat the environment to increase food stores
* makes the sheep full when they have a certain amount of food stores
* makes the sheep share food stores depending on their distance to nearby sheep in a given neighbourhood size (defined in the final model)

#### assignment.py

This file is responsible for running the agent-based model allowing, ultimately, the animation to be shown within a GUI. This includes a number of adaptable variables that can be changed to reflect and represent different sheep behaviours, creating a flexible model. To change these variables, the number to which they are assigned can be altered.

These variables include:

* **num_of_agents**: the number of sheep within the environment
* **num_of_iterations**: how many times sheep are able to be moved
* **neighbourhood**: the distance between the sheep before they start sharing their food stores

This code will run continually as an animation until a stopping condition, which suggests the sheep’s stores are full, is met. This animation should see the sheep moving around and eating the environment before, when agent stores reach a certain threshold, they speed up and, at the same time, the points representing the sheep change colour. When the sheep finally have enough food in their stores, the IPython console should print 'Stopping condition' and the animation stops running. This animation can be viewed in a graphical user interface (GUI). Here, when the model is run a seperate window should appear. This should contain a menu with the word model and a dropdown list that says run model. If this is selected the model should run in this GUI window. When the GUI window is closed, the code should stop running in the console.

#### in.txt

This file is a text file which contains the environment data. This was read into the model to enable to environment to be plotted and the agents to interact with it. In order for this to be used in the model, it has to be saved in the same directory in which the models are being created.

### Issues encountered when running the model

One issue encountered when developing the model was that when the animation began running, agents were all located in the bottom left-corner of the plot. While they moved around the environment as the animation continued, it was unclear why they exhibited this behaviour. This issue arose when agents were intialised using web data. It was later realised that web data contained x and y values from 0 to 100, opposed to 0 to 300, the length of the environment. Therefore, agents were restricted at first within these constraints. To solve this, where x and y variables were created using data from the web in the model, these lines of code were multiplied by 3. This ensured that agents initialised using web data were on a scale of 0 to 300, to match the size of the environment.

A further issue with the model is that when the model is run in the GUI, a seperate, blank figure opens at the same time as the GUI window. This is not an error with the code but a problem that arises when using spyder to run a GUI, thus could not be rectified. It is likely that in another application this would not be an issue, although this has not been tested. Nonetheless, this isssue is nothing more than a minor inconvenience and does not cause any problems.

Finally, while this is not necessarily an issue, there is some inconvenience when running the model in the GUI. To run the model in a GUI, the Spyder IPython console should to be set to Tkinter. To do this, the backend of the IPython console should be changed to TKinter. To do this on spyder go to tools > Ipython console > graphics > backend > TKinter. The console then has to be restarted to run the model in the GUI. The TKinter backend also produces a few issues within the IPython console such as slowing down the programme or not running the code. Mostly, this can be rectified by running "%gui tk" through the console. The model can be run without the GUI to avoid some of this inconvenience by using the automatic backend and commenting out lines 10 to 18 and 236 to 286 and commenting in lines 232 to 233. This opens the animation in a seperate window that should run the model automatically.

### Model testing

The print() function was used to test the model. Throughout the code, this function was used to print a specified message to the screen. This ensured that what was expected of certain functions, methods and variables was returned in the model. This reveals what is going on inside the code to ensure it was running as it should be. 

In additon to using the print() function, the built-in debugger menu in spyder was used after any additions or alterations to the code in order to 'debug' it. This enabled what was going on in the program to be identified and solved.

### Future development

While this model encapsulates a few different behaviours of the sheep within the environment, there are still other options for enhancing the model further. 
This model speeds up the agents as they increase their stores and makes the agents stop eating once they are full. However, further model enhancement could include making agents steal more resources from other agents if their stores are low, which could be done through adapting the share with neighbours function in agentframeworkassignment.py.

Additionally, the model could add in a new type of agent such as introducing a predator to eat nearby sheep. This would involve developing another agent class for the preadator and defining, within that, a series of functions that would allow them to move around the environment, eat the environment and eat nearby sheep. 

This is just two examples of how the model could be enhanced although there are many more options such as creating a complete population model including reproduction of sheep and wolves.
