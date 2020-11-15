#pragma once

#include <vector>

#include "mesh.hpp"

//scene.hpp

class scene {
	//stores meshes for now will add more later
	public:
		std::vector<mesh> meshList;
		scene();
		~scene();
		void addMesh(mesh* newMesh);
		void init();
};