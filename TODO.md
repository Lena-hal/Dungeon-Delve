# TODO
## new level object format
- objects -> every single object like netity, wall, trigger etc.
- links -> link to another level/location in level
- background -> data for the background used in the level
- extras -> extra level variables, modifiers etc.

## Renderer
Create a render manager that will take the current level and render it to the screen with any modifiers
The renderer should be able to do the following tasks:
- modify the visuals of the objects with custom shaders
- add future support for particle system
- be able to change the camera modes to:
  - static -> the camera is displaying a part of a level and is not moving
  - level view -> shows the whole level 
  - dynamic -> moves with the character

## Shader Manager
can change some property of every pixel on the screen

## FPS
also add delta time integration to stop those slow speed bugs

## Debug mode
add a way to show debug info on the screen (F3 menu)