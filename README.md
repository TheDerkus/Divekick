# Divekick

You'll need python to play, I'm not keeping track of library dependencies

Simply enter versus mode, pick Dive for both players, pick Kick gem for both players, and start the program as soon as the loading screen ends. To help with this, you can pause before round start and then start the program, as it respects the game being paused.

Only works on Windows right now.
The program sends keypresses to the active window, so make sure that window is Divekick. The program will make Divekick the active window when it starts running.

To end the program prematurely, simply pause and use ctrl-C to kill the process in the shell (yes I am a good programmer stop looking at me).

The program will play out 5 rounds, ignoring ties, and will control both players.

It will also save data about the rounds to a folder called 'tmp', which will reside in the same directory as the python files.

The program uses j, k, d, and f for p1 and p2 controls. Change the corresponding variables in divekick.py to adjust.
