#include <vector>
#include <random>
#include <time.h>
#include <iostream>

#include "randomize.hpp"

//randomize.cpp

void randomize(std::vector<qa>& qaVec) {
	srand(time(NULL));
	std::vector<qa> tempVec = {};
	int num;
	while(!qaVec.empty()) {
		//while tempVec is not empty

		num = rand() % qaVec.size();
		tempVec.push_back(qaVec[num]);
		qaVec.erase(qaVec.begin()+num);
	}
	qaVec = tempVec;
}