#include <iostream>
#include <math.h>

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

void camera::init(int _fov, int width, int height) {
	//setup camera stuff
	aspectRatio = width/height; // set camera aspect ratio
	fov = _fov; // Set camera fov
	f = 1/tan(fov/2); //set f property
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
	_point.projected.x = (aspectRatio * f * _point.x)/_point.z; // Projected x coord
	_point.projected.y = (f * _point.y)/_point.z; // Projected y coord
	_point.projected.z = 0; // I'll add this later when I need it
	//now for the meat :)
}