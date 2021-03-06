#pragma once

#include <vector>

#include "tri.hpp"
#include "point.hpp"

//mesh.hpp

class mesh // Contains mesh data
{ 

public:
	std::vector<tri> triList; // Send mesh tryangles here

	std::vector<point> verticies;
	std::vector<int> indicies;

	mesh();

	mesh(std::vector<tri> new_triList);

	mesh(
			std::vector<point> new_verticies,
			std::vector<int> new_indicies);

	~mesh();

	void fromTriList();

	void printVertInd();

	void move(double x, double y, double z);
};