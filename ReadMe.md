I will suppose the system used for this ReadMe is Windows

you need to have python installed, and to have pip installed.
to install pip you need to follow these instructions:
https://pip.pypa.io/en/stable/installation/

once pip is installed:
pip install pygame
pip install z3-solver
pip install tk

to run the graphical interface run main.py using python

py main.py on Windows
you can press exit to quit any time

configurations folder holds all the files used as entry for the solver
Dimacs is a intermediate file which holds the list of clauses for the current configuration file
Solutions are in the same file as Configurations, but end with _solved.txt. Configuration with 
no solution don't get saved to a file.

a configuration file has a dimmensions number at the start, if the dimmensions doesn't correspond 
to the file, than it will be completed with 0s.

Note: if you import a config file into the graphical interface, the focus won't be on the game so you might 
need to click once more to solve the board.


#-- Important
It is recommended to use the graphical interface only to view the solution of boards untill 4x4. If 
the board gets 5x5 or bigger than there will be a problem. The UI is not responsive, and to view it 
you need to change the width/height of the screen on main.py line 20 and base_solved_table_y on line 43

#-- Creator
To create a config file you can use the page html/javascript on the Creator folder. 
Double click on the html page to open the creator.
It has a placeholder of 3x3, you can enter a new dimmension and then click enter to update the table input.
You may enter the numbers, and then click "envoyer" to save it. If you haven't specified a name on the input 
field it is saved by default with "download.txt"


Te Configurations folder comes with some configuration examples, which could be imported directly and then solved.
If the file is empty or partially completed, it will still work and suppose that the missing data is empty.
If the file contains more data than expected, than it will only take care of what it is supposed to see.