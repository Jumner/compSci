#include <iostream>
#include <vector>
#include <algorithm>

#include "point.hpp"
#include "tri.hpp"
#include "mesh.hpp"

//mesh.cpp

mesh::mesh() { 
	// Default constructor
	verticies = {}; //known state
	std::cout << "Mesh init" << std::endl;
}

mesh::mesh(std::vector<tri> new_triList
): triList(new_triList) { 
	//construct using list of tri
	std::cout << "Mesh constructor triList" << std::endl;
}

mesh::mesh(
	std::vector<point> new_verticies,
	std::vector<int> new_indicies
): verticies(new_verticies), indicies(new_indicies) { 
	//construct using list of point and indicies

	std::cout << "Mesh constructor triList" << std::endl;
}

mesh::~mesh() {
	//mesh destructor
	
	std::cout << "Mesh destructed :)" << std::endl;
}

void mesh::fromTriList() {
	//create verticy and indicy lists from tri list

	std::cout << "Convert mesh from tri list" << std::endl;

	if(triList.size() == 0) {
		// if there is stuff in trilist
		// without this check data could be deleted
		return;
	}

	bool found;
	verticies.clear(); //empty verticies
	indicies.clear(); //empty indicies

	for(tri _tri: triList) { // foreach tri in triList
		for(point triPoint: _tri.points) { //foreach point in each tri
		
			found = false;

			for(int i = 0; i < verticies.size(); i ++) { // every point
		
				if(triPoint == verticies[i]) { //current point is in verticies
					found = true;

					indicies.push_back(i); //add index of point to indicies

					break;
				}

			}
			
			if(!found) { //current point ! in verticies
				verticies.push_back(triPoint);
				indicies.push_back(verticies.size()-1); //add the last element to indicies
			}

		}
	}

}

void mesh::printVertInd() { 
	//print the verticies and the indicies in a nice way
	std::cout << std::endl << "Mesh: Print verticies" << std::endl;

	for(point _vert: verticies) {
		std::cout << "( " << _vert.x << ", ";
		std::cout << _vert.y << ", ";
		std::cout << _vert.z << " ),";
    std::cout << std::endl;
	}

	std::cout << std::endl << "Mesh: Print indicies" << std::endl;

	for(int i = 0; i < indicies.size(); i += 3) {
	
    std::cout << "( " << indicies[i] << ", ";
    std::cout << indicies[i+1] << ", ";
    std::cout << indicies[i+2] << " ),";
		std::cout << std::endl;

  }
}