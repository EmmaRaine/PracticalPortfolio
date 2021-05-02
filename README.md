# GEOG5990: Assignment 1- Agent-based Modelling

### This repository contains the work developed during the practical sessions associated with the 'programming for geographical information analysis' module. This work has been produced in a python console, using the Spyder application.

Overall, this work aims to present an animation of the movement of sheep around an environment, modelling their eating behvaiour and how the sheep share their food stores. Through excellent documentation, useful comments and a simple structure, this model should:

* build agents in a space
* get agents to interact with each other
* read in environmental data
* get agents to interact with the environment
* randomise the order of agent actions
* display the model as a fully functioning animation
* contains the model within a graphical user interface (GUI)
* be initialised using data from the internet

### This model contains two python files, one that deals with agents and one that executes the model

#### agentframeworkassignment.py

This file contains the agent class that defines a variety of functions to determine agent (sheep) behvaiour.
This includes code that does the following:

* places the agents at a random starting point wihtin the environment
* randomly moves the sheep using control-flow statements
* makes the sheep eat the environment to increase their food stores
* makes the sheep share food stores depending on their distance (calculated using pythagoras theorem) to nearby sheep in a a neighbourhood size, as defined in the final model

#### assignment.py

This file is responsible for running the agent-based model allowing, ultimately, the animation to be shown within a GUI. This includes a number of adaptable variables that can changed to show different agent behaviours (num_of_agents, num_of_iterations, neighbourhood, **num_of_steps**). The model includes a stopping condition that will enable the aniation to stop running once the agents have a certain amount of food in their stores.

One issue encountered in the model is that when the animation begins running, the agents are all located in the bottom left-corner of the plot. While they do move around the environment as the animation continues, it is unclear why they exhibit this behaviour. This issue arose when the scale of plot was changed. Inititally, the x and y axis were set to start at 0 and end at 100. Once the animation was working this was changed so that the axes represented the length of the environment.

Additionally, while this is not necessarily an issue, there is some inconvenience when running the model in the GUI. To run the model in a GUI, the Spyder IPython console should to be set to Tkinter. To do this, under the graphics menu in the IPython tab under the tools menu, the backend has to be changed to TKinter. The console then has to be restarted to run the model in GUI, which if it works effectively should produce a pop-up box which contains a menu. In this menu, the model button has to be pressed followed by run model, in order to run the animation in the GUI. The TKinter backend also produces a few issues within the IPython console such as slowing down the programme or not running the code. Mostly, this can be rectified by running "%gui tk" through the console.
