# Traveling-Salesman-Algorithm
 Subscribe to My youtube Channel : [Auctux](https://www.youtube.com/c/Auctux)

## Requirements
> **Pygame** : pip install pygame

---
## Controls
- **Esc**   To close the window
- **T**     node Index
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
