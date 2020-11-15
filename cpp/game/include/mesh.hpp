#pragma once

#include <vector>

#include "tri.hpp"
#include "point.hpp"

//mesh.hpp

class mesh { //contains mesh data

	public:

		std::vector<tri> triList; //send mesh tryangles here

		std::vector<point2d> projected;
		std::vector<point> verticies;
		std::vector<int> indicies;

		mesh();

		mesh(std::vector<tri> new_triList);

		mesh(
			std::vector<point> new_verticies,
			std::vector<int> new_indicies
		);

		~mesh();

		void fromTriList();

		void printVertInd();

};