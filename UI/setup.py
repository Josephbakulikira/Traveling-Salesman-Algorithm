from UI.ui import *
from manager import width, height

panel = Panel()

PauseButton = Button("Pause", (width - 270, 180), 150, 50, 0, (10, 10, 30), (255, 255, 255))
ResetButton = Button("Reset", (width - 270, 240), 150, 50, 0, (10, 10, 30), (255, 255, 255))
RandomButton = Button("Generate", (width - 270, 300), 150, 50, 0, (10, 10, 30), (255, 255, 255))

AlgorithmChoice = DropDownButton("Select", (width - 350, 400), 300, 50, 6, 2, (10, 10, 30), (255, 255, 255))
AlgorithmChoice.childs[0].text = "Brute Force"
AlgorithmChoice.childs[1].text = "Lexicographic Order"
AlgorithmChoice.childs[2].text = "Genetic Algorithm"
AlgorithmChoice.childs[3].text = "Ant Colony ACS"
AlgorithmChoice.childs[4].text = "AntC Elitist"
AlgorithmChoice.childs[5].text = "AntC Max-Min"
AlgorithmChoice.currentIndex = 2
