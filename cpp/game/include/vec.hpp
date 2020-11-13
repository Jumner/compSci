#pragma once

//vec.hpp

class vec { //3d vector class

	double mag;

	public:
		double x,y,z;

		vec();

		vec(
			double initX,
			double initY,
			double initZ
		);

		~vec();

		double getMag();

		vec getNormal();
};