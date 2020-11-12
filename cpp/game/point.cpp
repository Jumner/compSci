#include <iostream>

#include "point.hpp"
//point.cpp

point::point(
	double initX,
	double initY,
	double initZ
): x(initX), y(initY), z(initZ) {
	//point constructor

	std::cout << "Point constructed" << std::endl;
}

point::~point() {
	//point destructor
	
	std::cout << "Point destructed :)" << std::endl;
}