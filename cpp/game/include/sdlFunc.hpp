#pragma once

#include <SDL2/SDL.h>

//sdlFunc.hpp

struct sdlInitReturn {
	int success;
	SDL_Window* window;
	SDL_Surface* surface;
	SDL_Surface* surfaceData;
};

void sdlCleanup(SDL_Window* window, SDL_Surface* surface);

sdlInitReturn sdlInit(const char* windowName, int width, int height);