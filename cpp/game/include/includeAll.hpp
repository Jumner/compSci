#pragma once

#include <SDL2/SDL.h>
#include "sdlFunc.hpp"

#include "point.hpp" //point which has x,y,z and projected position
#include "tri.hpp" //containes data for triangles for triarray meshes
#include "vec.hpp" //vectors never used but are always usefull
#include "mesh.hpp" //mesh has tri, vert and ind array for objects
#include "prim.hpp" //generate primitive meshes
#include "scene.hpp" //scene to contain multiple meshes and render them all
#include "camera.hpp" //containes projection data