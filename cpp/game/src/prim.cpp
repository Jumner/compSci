#include <vector>

#include "point.hpp"
#include "tri.hpp"
#include "prim.hpp"

//prim.cpp

std::vector<tri> prim::unitCube()
{
  return rect(1, 1, 1);
}

std::vector<tri> prim::cube(double size)
{
  double hSize = size / 2;
  return rect(hSize, hSize, hSize);
}

std::vector<tri> prim::rect(double x, double y, double z)
{ //makes rectangle
  double hX = x / 2;
  double hY = y / 2;
  double hZ = z / 2;
  std::vector<tri> triList = {
      //front face
      tri(point((-hX), (-hY), hZ), point(hX, (-hY), (-hZ)), point((-hX), (-hY), (-hZ))),
      tri(point((-hX), (-hY), hZ), point(hX, (-hY), hZ), point(hX, (-hY), (-hZ))),
      //back face
      tri(point((-hX), hY, hZ), point(hX, hY, (-hZ)), point((-hX), hY, (-hZ))),
      tri(point((-hX), hY, hZ), point(hX, hY, hZ), point(hX, hY, (-hZ))),
      //right face
      tri(point((-hX), hY, hZ), point((-hX), (-hY), hZ), point((-hX), (-hY), (-hZ))),
      tri(point((-hX), hY, hZ), point((-hX), (-hY), (-hZ)), point((-hX), hY, (-hZ))),
      //left face
      tri(point(hX, hY, hZ), point(hX, (-hY), hZ), point(hX, (-hY), (-hZ))),
      tri(point(hX, hY, hZ), point(hX, (-hY), (-hZ)), point(hX, hY, (-hZ))),
      //top face
      tri(point((-hX), hY, hZ), point(hX, hY, hZ), point(hX, (-hY), hZ)),
      tri(point((-hX), hY, hZ), point(hX, (-hY), hZ), point((-hX), (-hY), hZ)),
      //bottom face
      tri(point((-hX), hY, (-hZ)), point(hX, hY, (-hZ)), point(hX, (-hY), (-hZ))),
      tri(point((-hX), hY, (-hZ)), point(hX, (-hY), (-hZ)), point((-hX), (-hY), (-hZ)))};

  return triList;
}

std::vector<tri> prim::rect(std::vector<double> size)
{
  return prim::rect(size[0], size[1], size[2]);
}