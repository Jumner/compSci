#include <vector>

#include "tri.hpp"

//prim.hpp

class prim // Class for primitives
{
public:
  static std::vector<tri> unitCube();
  static std::vector<tri> cube(double size);
  static std::vector<tri> rect(double x, double y, double z);
  static std::vector<tri> rect(std::vector<double> size);
};