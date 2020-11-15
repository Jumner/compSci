#include <iostream>
#include <vector>
#include <string>

// #include <GL/glew.h>
#include <SDL2/SDL.h>
#include "sdlFunc.hpp"

#include "point.hpp"
#include "tri.hpp"
#include "vec.hpp"
#include "mesh.hpp"
#include "prim.hpp"

//window size
#define WIDTH 640
#define HEIGHT 480

int main() {
  sdlInitReturn sdlReturn = sdlInit("Hey it works!", WIDTH, HEIGHT);

	if(sdlReturn.success != 0) { //something went wrong :(
		return 0;
	}

	SDL_Window* window = sdlReturn.window;
	SDL_Surface* surface = sdlReturn.surface;
	SDL_Surface* surfaceData = sdlReturn.surfaceData;

	uint32_t pixelData[WIDTH*HEIGHT];

	std::cout << "Starting game loop" << std::endl;

	SDL_Event quitEvent;
	bool gameLoop = true;
	unsigned long frameCount = 0; 
	int r, g, b;
	while(gameLoop) {
		if(SDL_PollEvent(&quitEvent)) {
			if(quitEvent.type==SDL_QUIT) {
				std::cout << "Exiting Game loop" << std::endl;
				break;
			}
		}
		r = (int) frameCount%256;
		g = (int) (frameCount/3)%256;
		b = (int) (frameCount/7)%256;

		for(uint32_t& pixel: pixelData) {
			pixel = 0x000000FF + (r<<24) + (g<<16) + (b<<8);
			//bitshift just moves them over by a certain amount
		}

		SDL_LockSurface(surfaceData);

		surfaceData->pixels = pixelData;

		SDL_UnlockSurface(surfaceData);

		SDL_UpperBlit(surfaceData, nullptr, surface, nullptr);

		SDL_UpdateWindowSurface(window);

		frameCount++;

	}

	sdlCleanup(window, surface);

  std::vector<tri> triList = prim::unitCube();

  mesh testMesh(triList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  return 0;
  // std::cout << testMesh.verticies[0]. << std::endl;
}