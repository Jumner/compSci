#include "include.hpp"

#include <string>
#include <vector>
#include <iostream>

// choice.cpp

std::string substr(std::string text, int start, int end) {
	return text.substr(start, end-start);
}

choice::choice(std::string text) {
	//choice constructor
  std::size_t startPos = text.find('\t'); // Last tab character
	startPos = startPos == std::string::npos ? 0 : startPos; // If there is no tab set to 0

	name = substr(text, startPos, text.find('['));

	std::cout << "choice constructor: " << name << std::endl;
	
	std::cout << text << std::endl;
}

choice::~choice() {
	std::cout << "choice destructor: " << name << std::endl;
}