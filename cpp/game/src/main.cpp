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
#define WIDTH 640
#define HEIGHT 480

int main() {
  std::cout << "Starting..." << std::endl << std::endl;

	if(SDL_Init(SDL_INIT_VIDEO) != 0) { //sdl init failed
		std::cout << "Error in sdl init: " << SDL_GetError() << std::endl;
		return -1; 
	}

	SDL_Window* window = SDL_CreateWindow("Test game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, SDL_WINDOW_OPENGL);
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

	

	// SDL_Surface* surface = SDL_CreateRGBSurface(0, WIDTH, HEIGHT, 32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF);
	SDL_Surface* surface = SDL_GetWindowSurface(window);
	SDL_Surface* surfaceData = SDL_CreateRGBSurface(0, WIDTH, HEIGHT, 32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF);
	if(!surface) { //surface failed
		std::cout << "Surface creation failed: " << SDL_GetError() << std::endl;
		return -1;
	}

	uint32_t pixelData[WIDTH*HEIGHT];

	// SDL_Delay(1000); //for some reason this is needed

	std::cout << "Starting game loop" << std::endl;

	SDL_Event quitEvent;
	bool gameLoop = true;
	unsigned long frameCount = 0; 
	int g, b;
	bool gMode = true;
	bool bMode = true;
	while(gameLoop) {
		if(SDL_PollEvent(&quitEvent)) {
			if(quitEvent.type==SDL_QUIT) {
				std::cout << "Exiting Game loop" << std::endl;
				break;
			}
		}
		if(gMode) {
			g = (int) (frameCount/3)%255;
		} else {
			g = 255 - (int) (frameCount/3)%255;
		}
		if(bMode) {
			b = (int) (frameCount/7)%255;
		} else {
			b = 255 - (int)(frameCount/7)%255;
		}
		if(g>=255 || g<=0) {
			gMode = !gMode;
		}
		if(b>=255 || b<=0) {
			bMode = !bMode;
		}
			
		

		for(uint32_t& pixel: pixelData) {
			pixel = 0xFF0000FF + g*65536 + b*256;
			//make all pixels orange :)
		}		

		SDL_LockSurface(surfaceData);

		surfaceData->pixels = pixelData;

		SDL_UnlockSurface(surfaceData);

		SDL_UpperBlit(surfaceData, nullptr, surface, nullptr);

		SDL_UpdateWindowSurface(window);

		frameCount++;

	}

	SDL_DestroyRenderer(renderer);
	SDL_FreeSurface(surface);
	SDL_DestroyWindow(window);
	SDL_Quit();

  std::vector<tri> triList = prim::unitCube();

  mesh testMesh(triList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  return 0;
  // std::cout << testMesh.verticies[0]. << std::endl;
}