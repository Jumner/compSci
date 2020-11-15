#pragma once

#include <iostream>

#include "mesh.hpp"
#include "point.hpp"
#include "scene.hpp"

//camera.hpp

class camera {
	// stores camera properties and does projection	
	int fov; // fov of the camera
	double f; // Used for projection = 1/tan(fov/2)
	double aspectRatio; // w/h
	int width, height;
	int zFar;
	int zNear;
	int q; // Used for projection of z
	//z = (zFar/zFar-zNear)-(zFar*zNear/zFar-zNear)
	//yes im following the olc video for projection but what do you want from me?
	//there are like 5 wikipedia pages with similar names and I don't have a good grasp of matrixes
	public:
		camera();
		~camera();
		void init(int _fov, int width, int height);
		void project(mesh& _mesh);
		void project(point& _point);
};