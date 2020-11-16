// A program that reads from files and creates a que card like program

#include <string>
#include <iostream>
#include <vector>

#include "fileRead.hpp"
#include "randomize.hpp"

int main() {
	std::cout << "Welcome to Jublet 😬" << std::endl << std::endl;
	std::vector<qa> qArr = readFile(); //get a list of qa's
	std::string voidStr;
	randomize(qArr); //randomize the array
	for(qa ioQa: qArr) {
		//every question in the array
		std::cout << ioQa.question << std::endl << std::endl;
		std::getchar(); //wait for user to think about question
		std::cout << ioQa.answer << std::endl << std::endl;
		std::getchar(); //wait for user to think about answer
		system("clear"); //clear the screen
	}
	std::cout << "Congrats, you did it!😆" << std::endl << std::endl;
	std::getchar();
	std::cout << "Again?🥺" << std::endl;
	return 0;
}