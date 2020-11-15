#pragma once

#include <iostream>

#include "scene.hpp"
#include "mesh.hpp"
#include "point.hpp"

//camera.hpp

class camera {
	//stores camera properties and does projection	
	public:
		camera();
		~camera();
		void init();
		void project(scene& _scene);
		void project(mesh& _mesh);
		void project(point& _point);
};