#include <iostream>
#include <vector>
#include <string>

// #include <GL/glew.h>
#include "includeAll.hpp" //includes all the hpp files

//window size
#define WIDTH 800
#define HEIGHT 400

int main() {

	scene myScene; //create scene
	myScene.init(60, WIDTH, HEIGHT); // 60 fov setup scene

	mesh cubeMesh = mesh(prim::unitCube()); //create cube mesh

	myScene.addMesh(cubeMesh); //add mesh to scene


	myScene.meshList[0].move(0, 0, 2);
	
	myScene.meshList[0].printVertInd();

	myScene.project(); //maybe im in luck? project scene geometry

	myScene.meshList[0].printVertInd(); //print data

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
		for(point point: myScene.meshList[0].verticies) {
			if(point.projected.x > 0 && point.projected.x < WIDTH && point.projected.y > 0 && point.projected.y < HEIGHT) {
				pixelData[(int)(floor(point.projected.y)*WIDTH+floor(point.projected.x))] = 0x000000FF; //make points black
			}
		}
		
		displayBuffer(window, surface, surfaceData, pixelData);

		frameCount++;
		// gameLoop = false; //dont bother rendering

	}

	sdlCleanup(window, surface);

  return 0;
}