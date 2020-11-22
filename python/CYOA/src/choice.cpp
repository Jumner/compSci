#include "include.hpp"

#include <string>
#include <vector>
#include <iostream>

// choice.cpp

std::string substr(std::string text, int start, int end, bool exclusive=false) {
	return text.substr(start+exclusive, (end-start)-exclusive);
}

std::vector<std::string> split(std::string text, std::string pattern) {
	std::vector<std::string> stringVec = {};
	if (text == "") return stringVec;
	size_t pos = text.find(pattern);
	std::string token;
	while((pos = text.find(pattern)) != std::string::npos) {
		token = text.substr(0, pos);
		stringVec.push_back(token);
		text.erase(0, pos+pattern.length());
	}
	stringVec.push_back(text.substr(text.find(pattern)+1));

	return stringVec;
}
choice::choice(std::string strData) {
	//choice constructor
	size_t startPos; // The pos of the last tab char
	std::string data; // Contains text, options and img of the choice
	size_t imgDirPos; // Contains the location of the image directory in the string
	std::string remainder; // Data without the text and img
	std::vector<std::string> optVec; // Contains the options
	// Later this will be an options vector with recursion and stuff

	startPos = strData.find_last_of("\t"); // Last tab character
	startPos = startPos == std::string::npos ? 0 : startPos+1; // If there is no tab set to 0

	name = substr(strData, startPos, strData.find('[')); // The name of the choice

	std::cout << "Choice constructor: " << name << std::endl;
	data = substr(strData, strData.find('['), strData.find_last_of(']'), true);
	
	imgDirPos = data.find(", img:\"");
	imgDirPos = imgDirPos == std::string::npos ? 0 : imgDirPos; // Set to 0 if find fails

	imgDir = imgDirPos == 0 ? "" : substr(data, imgDirPos+6, data.find_last_of("\""), true);

	text = substr(data, data.find("\""), data.find("\"", 1), true);

	remainder = data.substr(data.find("\"", 1)+3);
	remainder = remainder.length() == imgDir.length()+6 ? "" : remainder.substr(0, remainder.length() - (8 + imgDir.length()));

	optVec = split(remainder, ", ");	
	for (std::string s: optVec) {
		opts.push_back(substr(s, s.find('\"'), s.find_last_of('\"'), true));
	}
}

choice::~choice() {
	std::cout << "Choice destructor: " << name << std::endl;
}

void choice::print() {
	// Print a choice for debugging
	std::cout << std::endl;
	std::cout << "Name:        " << name << std::endl;
	std::cout << "DisplayText: " << text << std::endl;
	if (imgDir != "") std::cout << "imgDir:      " << imgDir << std::endl;
	for (std::string s: opts) {
		std::cout << "Opt:         " << s << std::endl;
	}
	std::cout << std::endl;
}