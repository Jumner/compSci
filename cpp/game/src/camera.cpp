#include <iostream>

#include "scene.hpp"
#include "mesh.hpp"
#include "point.hpp"
#include "camera.hpp"

camera::camera() {
	// camera constructor
	std::cout << "Camera constructed" << std::endl;
}

camera::~camera() {
	// camera destructor
	std::cout << "Camera destructed" << std::endl;
}

void camera::init() {
	//setup camera stuff
	//fov = 2342 stuff like that
}

void camera::project(scene& _scene) { 
	// project a scene
	std::cout << "Scene project" << std::endl;
	for(mesh& _mesh: _scene.meshList) {
		// Every mesh in the scene
		project(_mesh); //project that mesh
	}
}

void camera::project(mesh& _mesh) { 
	// project a Mesh
	std::cout << "Mesh project" << std::endl;
	for(point& _point: _mesh.verticies) {
		// Every point in mesh	
		project(_point);
	}
}

void camera::project(point& _point) { 
	// project a point
	std::cout << "Point project" << std::endl;
	//now for the meat :)
}