#include <iostream>
#include <vector>

#include "point.hpp"
#include "tri.hpp"
#include "vec.hpp"
#include "mesh.hpp"

int main() {
  std::cout << "Starting..." << std::endl << std::endl;
  tri testTri(
    point(0,0,0),
    point(1,1,1),
    point(2,2,2)
  );

  std::vector<tri> testList = {testTri, testTri};

  mesh testMesh(testList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  // std::cout << testMesh.verticies[0]. << std::endl;
}