#include <vector>
#include <string>
#include <fstream>
#include <iostream>

#include "fileRead.hpp"

//fileRead.cpp

std::vector<qa> readFile() {
	//readFile definition
	std::vector<qa> qArr = {}; //leave it blank for now
	std::string q;
	qa cQa;
	std::ifstream current;
	current.open("tests/current.test"); //open up the current test
	while(std::getline(current, q)) { //grab question from file
		cQa.question = q.substr(0, q.find(':')); //good boy string manipulation 🐕
		cQa.answer = q.substr(q.find(':')+1, q.length()-1);
		// Don't you love string manipulation
		// so many +1's and -1's
		qArr.push_back(cQa);
		// Back to its corner
	}
	current.close();
	return qArr;
}