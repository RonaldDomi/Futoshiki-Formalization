To run this program you will need pip installed to then:
pip install pygame
pip install z3-solver
pip install tk

The main program is a graphical interface.
The goal of the program is to facilitate the creation and resolution of Futoshiki puzzles. 

The creation of the puzzle is /Creator/matrix.html.
The solution of the puzzle will be the main python program.

The solution will be saved in the same folder as where you loaded it on the program, and it will be named 
with a _solution prefix.

It is recommended to use the graphical interface only to view the solution of boards untill 4x4. If 
the board gets 5x5 or bigger than there will be a problem, the UI is not responsive. In this case it 
is recommended to have a look at the solutions text file.

To create a config file you can use the page html/javascript on the Creator folder. 
It has a placeholder of 3x3, you can enter a new dimmension and then click enter to update the table input.
You may enter the numbers, and then click "envoyer" to save it. If you haven't specified a name on the input 
field it is saved by default with "download.txt"

The Configurations folder comes with some configuration examples, which could be imported directly and then solved.


![Image of solution text file created by the program](/documents/6x6.png "solution.txt")
![Image of Futoshiki puzzles creator](/documents/creator.png "Creator of Futoshiki puzzles")
![Image of the graphical interface with solution](/documents/Futoshiki_Solver.png "Graphical interface solution of 4x4")