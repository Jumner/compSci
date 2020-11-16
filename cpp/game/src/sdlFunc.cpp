#include <iostream>

#include <SDL2/SDL.h>

#include "sdlFunc.hpp"

//sdlFunc.cpp

void sdlCleanup(SDL_Window *window, SDL_Surface *surface)
{
	//destroy objects and quit sdl
	SDL_FreeSurface(surface);
	SDL_DestroyWindow(window);
	SDL_Quit();
}

sdlInitReturn sdlInit(const char *windowName, int width, int height)
{
	//set up sdl and all the things we need

	//setup result struct
	sdlInitReturn result;
	result.success = 0;
	result.window = nullptr;
	result.surface = nullptr;
	result.surfaceData = nullptr;

	std::cout << "Starting..." << std::endl
						<< std::endl;

	if (SDL_Init(SDL_INIT_VIDEO) != 0)
	{ //sdl init failed
		std::cout << "Error in sdl init: " << SDL_GetError() << std::endl;
		result.success = -1;
		return result;
	}

	result.window = SDL_CreateWindow(windowName, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, SDL_WINDOW_OPENGL);
	if (!result.window)
	{ //window failed
		std::cout << "Window creation failed: " << SDL_GetError() << std::endl;
		result.success = -2;
		return result;
	}
	std::cout << "Window created" << std::endl;

	// SDL_Surface* surface = SDL_CreateRGBSurface(0, WIDTH, HEIGHT, 32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF);
	result.surface = SDL_GetWindowSurface(result.window);
	if (!result.surface)
	{ //window surface failed
		std::cout << "Window surface creation failed: " << SDL_GetError() << std::endl;
		result.success = -3;
		return result;
	}

	result.surfaceData = SDL_CreateRGBSurface(0, width, height, 32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF);
	if (!result.surfaceData)
	{ //data surface failed
		std::cout << "Data surface creation failed: " << SDL_GetError() << std::endl;
		result.success = -4;
		return result;
	}

	return result;
}

void displayBuffer(SDL_Window *window, SDL_Surface *surface, SDL_Surface *surfaceData, uint32_t pixelData[])
{
	SDL_LockSurface(surfaceData);

	surfaceData->pixels = pixelData;

	SDL_UnlockSurface(surfaceData);

	SDL_UpperBlit(surfaceData, nullptr, surface, nullptr);

	SDL_UpdateWindowSurface(window);
}