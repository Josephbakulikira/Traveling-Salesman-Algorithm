# Traveling-Salesman-Algorithm
 Subscribe to My youtube Channel : [Auctux](https://www.youtube.com/c/Auctux)
 ---
 Traveling Salesman using 3 algorithms:
 - Brute force
   - Random
   - Lexicographical order
 - genetic algorithm
 - Ant Colony optimization
   - Elitist
   - Max-Min
## Requirements
> **Pygame** : pip install pygame

---
## Controls
- **Esc**   To close the window
- **Space** To Pause and Start Simulation
- **Enter or Return** To toggle the UI Panel
---
```python:main.py
# Brute force solution , just by using going through all the possible combination 
# with a random function until we find the shortest distance
manager.BruteForce() 
# using Lexicographical order to solve the problem by going in order into all the possible routes
manager.Lexicographic()
# using genetic algorithm to find the fittest one
manager.GeneticAlgorithm()
# using AntColonyOptimization(name:String) 
manager.AntColonyOptimization("ACS") # or "ELITIST" or "MAX-MIN"

```
---
![Screenshot (240)](https://user-images.githubusercontent.com/48150537/136697477-262bc770-9986-44ba-9441-7ea6964fb487.png)
---
## Unsolved Issues & Bugs
     The code is a little bit redundant , it's need some refactoring.
     And the ui also need some retouch
---
![Screenshot (241)](https://user-images.githubusercontent.com/48150537/136697483-3936c2de-323b-474a-95f8-7976a9447a96.png)
