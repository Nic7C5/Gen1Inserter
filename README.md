# Gen1Inserter
Insert Pokémon fom Generation 2 (Gold, Silver, Crystal) to 1st Generation (Red, Blue) Pokémon Roms. Based on Danny-E's [version](https://github.com/dannye/pokered-gen-II) of pret's [pokered](https://github.com/pret/pokered) disassembly. The program is written in python 2.

##### Getting started
1. Follow all the [steps](https://github.com/pret/pokered/blob/master/INSTALL.md) to assemble (i.e. making a rom file) Pokemon Red/Blue from the pokemon disassembly (I'm using pokered-gen-II by Danny- and parts of pokecrystal). For Windows there's a video tutorial on [Youtube](https://www.youtube.com/watch?v=fYytG7IUUWg).

2. You need to clone three repositories: [This one](https://github.com/Nic7C5/Gen1Inserter), Danny-E's [pokered-gen-II](https://github.com/dannye/pokered-gen-II), and pret's [pokecrystal](https://github.com/pret/pokecrystal) to your computer by entering the following in your commandline (e.g. Cygwin on Windows; enter linwise, press enter and wait, repeat with the following lines).

        git clone https://github.com/dannye/pokered-gen-II
        git clone https://github.com/pret/pokecrystal
        git clone https://github.com/Nic7C5/Gen1Inserter
        
    These directories should have been created in your home directory:
    
    ![](https://dl.dropboxusercontent.com/u/55188886/screen_1.png)

3. Test it by assembling red and/or blue version. Example in Cygwin:

        cd C:\<path>\pokered-gen-II
        make red        #or
        make blue       #or just
        make            #for both roms
    

4. As my program is written in python, you need to have a python interpreter installed on your system. On Windows you're doing this during the installation of Cygwin/Cygwin64. However I have another installed as I faced problems when using *os* features and when trying to install the pack *numpy*. If you are facing similar problems or don't have a python interpreter yet. I reccomend [Anaconda](https://www.continuum.io/downloads), which is available for all platforms for free.

5. Got to '<home>/Gen1Inserter/resources/pic/' and copy the folders 'gmon' and 'gmonback' to '<home>/pokered-gen-II/pic/'.

##### Running the program
Run the commandline program of your choice - I simply use CMD - and run 'insert_pkmn.py'.
        
        cd C:\<path>\Gen1Inserter\resources\    #your path
        python insert_pokemon.py
    
![](https://dl.dropboxusercontent.com/u/55188886/Unbenannt2.PNG)  
![](https://dl.dropboxusercontent.com/u/55188886/Unbenannt.PNG)

Then do what you are asked to.

##### Bugs
* you can reinsert already existing Pokemon.
* error when handling 'multi evolution' data (e.g. evee)
* tm/hm and level learnsets not yet implemented
