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
  std::size_t startPos = strData.find('\t'); // Last tab character
	startPos = startPos == std::string::npos ? 0 : startPos; // If there is no tab set to 0

	name = substr(strData, startPos, strData.find('['));

	std::cout << "choice constructor: " << name << std::endl;
	std::string data = substr(strData, strData.find('['), strData.find_last_of(']'), true);

	size_t imgDirPos = data.find(", img:\"");
	imgDirPos = imgDirPos == std::string::npos ? 0 : imgDirPos; // Set to 0 if find fails
	imgDir = substr(data, imgDirPos+6, data.find_last_of("\""), true);
	imgDir = imgDirPos == 0 ? "" : imgDir;
	std::cout << "imgDir: " << imgDir << std::endl;	
	text = substr(data, data.find("\""), data.find("\"", 1), true);

	std::string remainder = substr(data, data.find("\", ")+3, imgDirPos);
	std::cout << "Remainder: " << remainder << std::endl;
	std::cout << remainder << std::endl;
	std::vector<std::string> vec = split(remainder, ", ");	
	for (std::string s: vec) {
		std::cout << "s: " << substr(s, s.find('\"'), s.find_last_of('\"'), true) << std::endl;
		opts.push_back(substr(s, s.find('\"'), s.find_last_of('\"'), true));
	}
}

choice::~choice() {
	std::cout << "choice destructor: " << name << std::endl;
}