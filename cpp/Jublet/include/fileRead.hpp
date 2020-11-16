#pragma once

#include <vector>
#include <string>

struct qa {
	std::string question;
	std::string answer;
};

std::vector<qa> readFile();