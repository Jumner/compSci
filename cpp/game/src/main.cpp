#include <iostream>
#include <vector>

// #include <GL/glew.h>
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

	//declare surface
	SDL_Surface* surface = nullptr;

  if(SDL_Init(SDL_INIT_VIDEO) == 0) {
    std::cout << "SDL init successful :)" << std::endl;
  } else {
    std::cout << "Error in SDL init" << std::endl;
	  std::cout << "Init gave error: " << SDL_Init(SDL_INIT_EVERYTHING) << std::endl;
		return 0;
	}

  //now create window!
  SDL_Window* window = SDL_CreateWindow("Hell yea", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_SIZE_X, SCREEN_SIZE_Y, SDL_WINDOW_SHOWN);
  if(window) {
		std::cout << "Window created!" << std::endl;
		surface = SDL_GetWindowSurface(window);
		SDL_FillRect(surface, NULL, SDL_MapRGB(surface->format, 0xFF, 0xFF, 0xFF));
		SDL_UpdateWindowSurface(window);
		SDL_Delay(5000);
	} else  {
    std::cout << "Damn it no window :(" << std::endl;
    return 0;
  }

  std::vector<tri> triList = prim::unitCube();

  mesh testMesh(triList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  // std::cout << testMesh.verticies[0]. << std::endl;
}