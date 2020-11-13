#include <iostream>
#include <vector>

#include "tri.hpp"
#include "point.hpp"

tri::tri(
	point initA,
	point initB,
	point initC
) {
	// Tri point constructor
	points.push_back(initA);
	points.push_back(initB);
	points.push_back(initC);
}

tri::tri(std::vector<point> pointList): points(pointList) {
	// Tri vector constructor
} 

tri::~tri() {
	// Tri destructor
}