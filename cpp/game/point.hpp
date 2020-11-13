#pragma once
//point.hpp

class point { // Point for tryangle

  public:
    
		double x,y,z; // Position of this point
		
		point( // Point constructor
			double initX,
			double initY,
			double initZ
		);
		
		~point(); // Point destructor

		bool operator==(point& obj);
};