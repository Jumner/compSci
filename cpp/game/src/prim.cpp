#include <vector>

#include "point.hpp"
#include "tri.hpp"
#include "prim.hpp"

//prim.cpp

std::vector<tri> prim::unitCube() {
  std::vector<tri> triList = {
    //right ----> +x
    //left -----> -x
    //forward --> +y
    //backward -> -y
    //up -------> +z
    //down -----> -z
  
    //front
    //-1, -1, 1 | 1, -1, -1 | -1, -1, -1
    //-1, -1, 1 | 1, -1, 1 | 1, -1 , -1 
    //right
    //-1, 1, 1 | -1, -1, 1 | -1, -1, -1
    //-1, 1, 1 | -1, -1, -1 | -1, 1, -1
    //top
    //-1, 1, 1 | 1, 1, 1 | 1, -1, 1
    //-1, 1, 1 | 1, -1, 1 | -1, -1, 1

    //front face
    tri(point(-0.5, -0.5, 0.5), point(0.5, -0.5, -0.5), point(-0.5, -0.5, -0.5)),
    tri(point(-0.5, -0.5, 0.5), point(0.5, -0.5, 0.5), point(0.5, -0.5, -0.5)),
    //back face
    tri(point(-0.5, 0.5, 0.5), point(0.5, 0.5, -0.5), point(-0.5, 0.5, -0.5)),
    tri(point(-0.5, 0.5, 0.5), point(0.5, 0.5, 0.5), point(0.5, 0.5, -0.5)),
    //right face
    tri(point(-0.5, 0.5, 0.5), point(-0.5, -0.5, 0.5), point(-0.5, -0.5, -0.5)),
    tri(point(-0.5, 0.5, 0.5), point(-0.5, -0.5, -0.5), point(-0.5, 0.5, -0.5)),
    //left face
    tri(point(0.5, 0.5, 0.5), point(0.5, -0.5, 0.5), point(0.5, -0.5, -0.5)),
    tri(point(0.5, 0.5, 0.5), point(0.5, -0.5, -0.5), point(0.5, 0.5, -0.5)),
    //top face
    tri(point(-0.5, 0.5, 0.5), point(0.5, 0.5, 0.5), point(0.5, -0.5, 0.5)),
    tri(point(-0.5, 0.5, 0.5), point(0.5, -0.5, 0.5), point(-0.5, -0.5, 0.5)),
    //bottom face
    tri(point(-0.5, 0.5, -0.5), point(0.5, 0.5, -0.5), point(0.5, -0.5, -0.5)),
    tri(point(-0.5, 0.5, -0.5), point(0.5, -0.5, -0.5), point(-0.5, -0.5, -0.5))
  };

  return triList;

}

std::vector<tri> prim::cube(double size) {
  double hSize = size/2;
  std::vector<tri> triList = {
    //front face
    tri(point(-hSize, -hSize, hSize), point(hSize, -hSize, -hSize), point(-hSize, -hSize, -hSize)),
    tri(point(-hSize, -hSize, hSize), point(hSize, -hSize, hSize), point(hSize, -hSize, -hSize)),
    //back face
    tri(point(-hSize, hSize, hSize), point(hSize, hSize, -hSize), point(-hSize, hSize, -hSize)),
    tri(point(-hSize, hSize, hSize), point(hSize, hSize, hSize), point(hSize, hSize, -hSize)),
    //right face
    tri(point(-hSize, hSize, hSize), point(-hSize, -hSize, hSize), point(-hSize, -hSize, -hSize)),
    tri(point(-hSize, hSize, hSize), point(-hSize, -hSize, -hSize), point(-hSize, hSize, -hSize)),
    //left face
    tri(point(hSize, hSize, hSize), point(hSize, -hSize, hSize), point(hSize, -hSize, -hSize)),
    tri(point(hSize, hSize, hSize), point(hSize, -hSize, -hSize), point(hSize, hSize, -hSize)),
    //top face
    tri(point(-hSize, hSize, hSize), point(hSize, hSize, hSize), point(hSize, -hSize, hSize)),
    tri(point(-hSize, hSize, hSize), point(hSize, -hSize, hSize), point(-hSize, -hSize, hSize)),
    //bottom face
    tri(point(-hSize, hSize, -hSize), point(hSize, hSize, -hSize), point(hSize, -hSize, -hSize)),
    tri(point(-hSize, hSize, -hSize), point(hSize, -hSize, -hSize), point(-hSize, -hSize, -hSize))
  };

  return triList;
}