# Basic Flow Example using CrewAI and Litellm
=====================================================

This project demonstrates a basic example of using CrewAI's flow feature to manage a sequence of tasks, leveraging the power of Litellm for language model interactions.

## Overview
--------

This project uses the CrewAI framework to define a flow that generates a series of random cities, retrieves fun facts about each city, rates the cities based on their fun facts, and finally determines the best city. The flow utilizes Litellm's language model to interact with the user and generate human-like text.

## Code Explanation
-----------------

The `Basic_flow.py` file defines a CrewAI flow that consists of four main tasks:

1. `generate_city`: Generates a list of three random cities.
2. `generate_fun_fact`: Retrieves fun facts about each city using Litellm's language model.
3. `rate_city`: Rates each city based on its fun fact.
4. `best_city`: Determines the best city based on the ratings.

The flow is defined using CrewAI's `Flow` class, which provides a simple and intuitive way to manage complex workflows. The `listen` decorator is used to specify the dependencies between tasks, ensuring that each task is executed in the correct order.

## Benefits of Flows in CrewAI
-----------------------------

CrewAI's flow feature provides several benefits, including:

* **Simplified workflow management**: Flows make it easy to manage complex workflows by breaking them down into smaller, more manageable tasks.
* **Improved code organization**: Flows promote code organization by separating each task into its own function, making it easier to understand and maintain the code.
* **Enhanced collaboration**: Flows enable multiple developers to work on different tasks simultaneously, improving collaboration and reducing conflicts.

## Example Use Case
-----------------

This project is just a small example of what can be achieved using CrewAI's flow feature. In a real-world scenario, you could use flows to manage more complex workflows, such as:

* Automating customer support tasks
* Managing data processing pipelines
* Coordinating team workflows

## Requirements
------------

* CrewAI (`pip install crewai`)
* Litellm (`pip install litellm`)

## Running the Project
--------------------

To run the project, simply execute the `Basic_flow.py` file using Python:
```bash
python Basic_flow.py
```
This will start the flow and execute each task in sequence.

## Conclusion
----------

This project demonstrates the power and simplicity of using CrewAI's flow feature to manage complex workflows. By leveraging Litellm's language model, we can create more human-like interactions and automate tasks more efficiently. We hope this example inspires you to explore the possibilities of using flows in your own projects!