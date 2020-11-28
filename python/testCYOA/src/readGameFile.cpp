#include <vector>
#include <string>
#include <fstream>
#include <iostream>

#include "include.hpp"

// readGameFile.cpp

std::vector<std::string> readFile(std::string path) {
	// Read contents of file into string array
	std::vector<std::string> lines;
	std::string line;
	std::ifstream gameFile;
	gameFile.open(path);
	while(std::getline(gameFile, line)) {
		// Grab all the lines
		lines.push_back(line);
	}
	return lines;
}