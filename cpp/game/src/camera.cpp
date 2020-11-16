#include <iostream>
#include <math.h>

#include "scene.hpp"
#include "mesh.hpp"
#include "point.hpp"
#include "camera.hpp"

camera::camera()
{
	// camera constructor
	std::cout << "Camera constructed" << std::endl;
}

camera::~camera()
{
	// camera destructor
	std::cout << "Camera destructed" << std::endl;
}

void camera::init(int _fov, int _width, int _height)
{
	//setup camera stuff
	width = _width;
	height = _height;
	aspectRatio = (float)height / (float)width; // set camera aspect ratio
	fov = _fov;																	// Set camera fov
	f = 1 / tan(fov / 2);												//set f property
	hWidth = width / 2;
	hHeight = height / 2;
	fwa = hWidth * f * aspectRatio;
	fh = hHeight * f;
}

void camera::project(mesh &_mesh)
{
	// project a Mesh
	std::cout << "Mesh project" << std::endl;
	for (point &_point : _mesh.verticies)
	{
		// Every point in mesh
		project(_point);
	}
}

void camera::project(point &_point)
{
	// project a point
	std::cout << "Point project" << std::endl;
	_point.projected.x = hWidth + (fwa * _point.x) / _point.z; // Projected x coord
	_point.projected.y = hHeight + (fh * _point.y) / _point.z; // Projected y coord
	_point.projected.z = 0;																		 // I'll add this later when I need it
}