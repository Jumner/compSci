#include <iostream>

#include "scene.hpp"
#include "mesh.hpp"
#include "camera.hpp"

//scene.cpp

scene::scene() {
	//scene constructor
	std::cout << "Scene constructed" << std::endl;

}

scene::~scene() {
	//scene destructor
	std::cout << "Scene destructed" << std::endl;

}

void scene::addMesh(mesh& newMesh) { //default is empty mesh
	//add a mesh to the scene
	//can be ran before and after init

	newMesh.fromTriList(); //make sure it is in vert+ind form
	meshList.push_back(newMesh); //add mesh to list by "reference"

}

void scene::init(int _fov, int width, int height) {
	//init the scene
	std::cout << "Scene init" << std::endl;
	cam.init(_fov, width, height);
	//does nothing rn but will be needed to find normals and stuff
}

void scene::project() { 
	// Project this scene using this camera
	std::cout << "Scene project" << std::endl;
	for(mesh& _mesh: meshList) {
		// Every mesh in the scene
		cam.project(_mesh); // Now project that mesh
	}
}