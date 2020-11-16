#pragma once

#include <vector>

#include "mesh.hpp"
#include "camera.hpp"

//scene.hpp

class scene // Stores meshes for now will add more later
{ 
public:
	std::vector<mesh> meshList;
	camera cam; // no params for now
	scene();
	~scene();
	void addMesh(mesh &newMesh);
	void init(int _fov, int width, int height);
	void project(); // Projects the scene geometry using the scene camera
};