#include <iostream>

#include "point.hpp"
//point.cpp

point::point(
		double initX,
		double initY,
		double initZ) : x(initX), y(initY), z(initZ)
{
	//point constructor
}

point::~point()
{
	//point destructor
}

bool point::operator==(point &obj)
{
	// operator overflow for == to tell if points are the same
	return x == obj.x && y == obj.y && z == obj.z;
}