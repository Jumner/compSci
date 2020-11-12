#include <iostream>

#include "tri.hpp"
#include "point.hpp"

tri::tri( // Tri constructor
	point initA,
	point initB,
	point initC
): a(initA), b(initB), c(initC) {
	std::cout << "Tri constructed" << std::endl;
}

tri::~tri() {
	std::cout << "Tri destructed :)" << std::endl;
}