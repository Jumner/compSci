#pragma once
//point.hpp

struct point3d
{
	double x;
	double y;
	double z;
};

class point // Point used in triangles
{ 

public:
	double x, y, z;		 // Position of this point
	point3d projected; //projected location of this point

	point( // Point constructor
			double initX,
			double initY,
			double initZ);

	~point(); // Point destructor

	bool operator==(point &obj);
};