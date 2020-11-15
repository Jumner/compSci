#include <iostream>
#include <vector>
#include <string>

// #include <GL/glew.h>
#include "includeAll.hpp" //includes all the hpp files

//window size
#define WIDTH 640
#define HEIGHT 480

int main() {
  sdlInitReturn sdlReturn = sdlInit("Hey it works!", WIDTH, HEIGHT);

	if(sdlReturn.success != 0) { //something went wrong :(
		return 0; //quit to investigate error
	}

	SDL_Window* window = sdlReturn.window;
	SDL_Surface* surface = sdlReturn.surface;
	SDL_Surface* surfaceData = sdlReturn.surfaceData;

	uint32_t pixelData[WIDTH*HEIGHT]; //array of pixels

	std::cout << "Starting game loop" << std::endl;

	SDL_Event quitEvent;
	bool gameLoop = true;
	unsigned long frameCount = 0; 
	unsigned char r,g,b; //in g++ char is unsigned ???
	while(gameLoop) {
		if(SDL_PollEvent(&quitEvent)) {
			if(quitEvent.type==SDL_QUIT) {
				std::cout << "Exiting Game loop" << std::endl;
				break;
			}
		}
		
		r = 0xFF;
		g = 0x50;
		b = 0x00;

		for(uint32_t& pixel: pixelData) {
			pixel = 0x000000FF + (r<<24) + (g<<16) + (b<<8);
			//bitshift just moves them over by a certain amount
		}
		
		displayBuffer(window, surface, surfaceData, pixelData);

		frameCount++;

	}

	sdlCleanup(window, surface);



	scene myScene;
	myScene.init(60, WIDTH, HEIGHT); // 60 fov

	mesh cubeMesh = mesh(prim::unitCube());

	myScene.addMesh(cubeMesh);

	myScene.project(); //maybe im in luck?


  return 0;
}