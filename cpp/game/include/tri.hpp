#pragma once

#include <vector>

#include "point.hpp"
#include "vec.hpp"
//tri.hpp

class tri // Triangle class :)
{

public:
	std::vector<point> points;

	vec normal;

	tri( // Tri constructor
			point initA,
			point initB,
			point initC);

	tri(std::vector<point> pointList);

	// Tri constructor
	~tri();
};