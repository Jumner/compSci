#include <iostream>
#include <vector>

#include <GL/glew.h>
#include <SDL2/SDL.h>

#include "point.hpp"
#include "tri.hpp"
#include "vec.hpp"
#include "mesh.hpp"
#include "prim.hpp"

//window size
#define SCREEN_SIZE_X 800
#define SCREEN_SIZE_Y 600

int main() {
  std::cout << "Starting..." << std::endl << std::endl;

  if(SDL_Init(SDL_INIT_EVERYTHING) != 0) {
    std::cout << "SDL init successful :)" << std::endl;
  } else {
    std::cout << "Error in SDL init" << std::endl;
  }

  //now create window!
  SDL_Window* window = SDL_CreateWindow("YAA!", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_SIZE_X, SCREEN_SIZE_Y, SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN);
  if(!window) {
    std::cout << "Damn it no window :(" << std::endl;
    return 0;
  }
  //ENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_SIZE_X, SCREEN_SIZE_Y, SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN);

  std::vector<tri> triList = prim::unitCube();

  mesh testMesh(triList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  // std::cout << testMesh.verticies[0]. << std::endl;
}