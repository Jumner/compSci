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
#define SCREEN_SIZE_X 640
#define SCREEN_SIZE_Y 480

int main() {
  std::cout << "Starting..." << std::endl << std::endl;

	SDL_Window* window = SDL_CreateWindow("Test game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_SIZE_X, SCREEN_SIZE_Y, SDL_WINDOW_OPENGL);
	if(!window) { //window failed
		std::cout << "Window creation failed: " << SDL_GetError() << std::endl;
		return -1;
	}
	std::cout << "Window created" << std::endl;

	SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
	if(!renderer) { //renderer failed
		std::cout << "Renderer creation failed: " << SDL_GetError() << std::endl;
		return -1;
	}
	std::cout << "Renderer created" << std::endl;

	// SDL_Delay(1000); //for some reason this is needed

	std::cout << "Starting game loop" << std::endl;

	SDL_Event quitEvent;
	bool gameLoop = true;
	unsigned long frameCount = 0; 
	int v;
	while(gameLoop) {
		if(SDL_PollEvent(&quitEvent)) {
			if(quitEvent.type==SDL_QUIT) {
				std::cout << "Exiting Game loop" << std::endl;
				break;
			}
		}
		v = frameCount%255;
		SDL_SetRenderDrawColor(renderer, v, 50, 0, 255);
		frameCount++;
		SDL_RenderClear(renderer);

		SDL_RenderPresent(renderer);
	}

	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	SDL_Quit();

  std::vector<tri> triList = prim::unitCube();

  mesh testMesh(triList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  return 0;
  // std::cout << testMesh.verticies[0]. << std::endl;
}