#pragma once

#include "point.hpp"
#include "vec.hpp"
//tri.hpp

class tri { // Triangle class :)
	
	public:

		point a, b, c; //three points of tri

		vec normal;

		tri( // Tri constructor
			point initA,
			point initB,
			point initC
		);

		// Tri constructor
		~tri();
};