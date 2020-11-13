#include <vector>

#include "tri.hpp"

//prim.hpp

class prim { //class for primitives
  public:
    static std::vector<tri> unitCube();
    static std::vector<tri> cube(double size);

};