#pragma once
//point.hpp

struct point2d {
	double x;
	double y;
};

class point { // Point for tryangle

  public:
    
		double x,y,z; // Position of this point
		point2d projected;
		
		point( // Point constructor
			double initX,
			double initY,
			double initZ
		);
		
		~point(); // Point destructor

		bool operator==(point& obj);
};