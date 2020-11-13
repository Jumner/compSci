#include <iostream>
#include <vector>

#include "point.hpp"
#include "tri.hpp"
#include "vec.hpp"
#include "mesh.hpp"
#include "prim.hpp"

int main() {
  std::cout << "Starting..." << std::endl << std::endl;
  tri testTri(
    point(0,0,0),
    point(1,1,1),
    point(2,2,2)
  );

  std::vector<tri> triList = prim::rect(10,1,5);

  mesh testMesh(triList);
  testMesh.fromTriList();

  testMesh.printVertInd();
  // std::cout << testMesh.verticies[0]. << std::endl;
}