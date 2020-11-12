#include <iostream>
#include <cmath>

#include "vec.hpp"

//vec.cpp

vec::vec() { // Default 3d vector constructor
	std::cout << "Vec init" << std::endl;
}

vec::vec( // 3d Vector constructor
	double initX,
	double initY,
	double initZ
) {
	std::cout << "Vec constructed" << std::endl;
}

vec::~vec() {
	// 3d Vector destructor

	std::cout << "Vec destructed :)" << std::endl; 
}

double vec::getMag() {
	return sqrt(x*x + y*y + z*z); //Pythag in 3d
}

vec vec::getNormal() { //returns a normalized vector
	mag = getMag();
	vec newVec(x,y,z);
	newVec.x /= mag;
	newVec.y /= mag;
	newVec.z /= mag;
	return newVec;
}