#include <iostream>

#include "point.hpp"
#include "tri.hpp"

int main() {
  std::cout << "Starting..." << std::endl << std::endl;
  tri testTri(
    point(0,0,0),
    point(1,1,1),
    point(2,2,2)
  );
  std::cout << testTri.c.x << std::endl;
}