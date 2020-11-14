#include <iostream>
#include <vector>

#include "point.hpp"
#include "tri.hpp"
#include "vec.hpp"
#include "mesh.hpp"
#include "prim.hpp"

int main() {
  std::cout << "Starting..." << std::endl << std::endl;

  std::vector<tri> triList = prim::unitCube();

  mesh testMesh(triList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  // std::cout << testMesh.verticies[0]. << std::endl;
}