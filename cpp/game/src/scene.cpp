#include <iostream>

#include "scene.hpp"
#include "mesh.hpp"

//scene.cpp

scene::scene() {
	//scene constructor
	std::cout << "Scene constructed" << std::endl;

}

scene::~scene() {
	//scene destructor
	std::cout << "Scene destructed" << std::endl;

}

void scene::addMesh(mesh* newMesh = &mesh()) { //default is empty mesh
	//add a mesh to the scene
	//can be ran before and after init

	newMesh->fromTriList(); //make sure it is in vert+ind form
	meshList.push_back(*newMesh); //add mesh to list by "reference"

}

void scene::init() {
	//init the scene
	std::cout << "Scene init" << std::endl;
	//does nothing rn but will be needed to find normals and stuff
}