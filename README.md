# Sudoku Solver

website used in this project: https://sudoku.game/

This Python script is a Sudoku puzzle solver that employs image processing techniques to capture, process, and solve Sudoku puzzles. The key features and components of this project include:

* Image Capture: The script uses the pyautogui library to capture a screenshot of the Sudoku puzzle displayed on the screen.

* Image Processing: After capturing the puzzle, the script processes the image using the scikit-image library. It performs operations such as resizing, thresholding, and noise removal to prepare the puzzle for analysis.

* Sudoku Detection: The script detects the boundaries of the Sudoku grid by allowing the user to click on two points to define the boundaries. It also identifies individual cells within the grid.

* Number Recognition: Using image processing, the script attempts to recognize and extract the numbers within each cell of the Sudoku grid. The recognized numbers are then stored for solving.

* Automation: The script has an option to automate solving the puzzle on a Sudoku puzzle website by simulating mouse clicks and keyboard inputs.

This project combines computer vision and image processing to create a Sudoku solver that can handle puzzles automatically. It provides a practical demonstration of how image processing can be applied to solve real-world puzzles.

## Installations Required

installations required to run this notebook:

* ```pip install mouse```
* ```pip install pyautogui```
* ```pip install keyboard```
* ```pip install scikit-image```
* ```pip install matplotlib```
* ```pip install numpy```

## Screenshots

**<p align="center">Showing the arrays of the sudoku detected by image proccessing and after solving it</p>**

![Screenshot 1](/READMEAssets/1.png)

##

**<p align="center" >Showing the screenshot of the screen and sudoku numbers after preproccessing</p>**

![Screenshot 2](/READMEAssets/3.png)

## Demo

![Demo](/READMEAssets/2.gif)
