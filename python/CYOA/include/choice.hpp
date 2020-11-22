#pragma once

#include <string>
#include <vector>

// choice.hpp

std::string substr(std::string text, int start, int end, bool exclusive);

class choice { // Class that contains the data for a given choice
	std::string imgDir;
	public:
		std::string name;
		std::string text;
		std::vector<std::string> opts; // Just to get it set up
		// std::vector<choice> opts;

		choice(std::string text);
		~choice();

		void print();
};