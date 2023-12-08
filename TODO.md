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

## Optimalization
do a lot of rendering optimalizations because its getting laggy rn

# Level Editor Compiled Language
create a "programming" langugage for creating levels:
```
> creates a group of textures named floor
GROUP FLOOR: floor1.png, floor2.png, floor3.png...
> creates a Grid of floor objects starting at X 100, Y 100 with 10x10 objects with spacing 20px, using the FLOOR group as a reference of textures
GRID 100 100 10 10 20 FLOOR
```
and commands like these for the build logic
after compilation this results into a .json file usable as a level