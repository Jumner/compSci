#pragma once

#include <SDL2/SDL.h>

//sdlFunc.hpp

struct sdlInitReturn // Return data from sdlInit
{
	int success;
	SDL_Window *window;
	SDL_Surface *surface;
	SDL_Surface *surfaceData;
};

void sdlCleanup(SDL_Window *window, SDL_Surface *surface);

sdlInitReturn sdlInit(const char *windowName, int width, int height);

void displayBuffer(SDL_Window *window, SDL_Surface *surface, SDL_Surface *surfaceData, uint32_t pixelData[]);