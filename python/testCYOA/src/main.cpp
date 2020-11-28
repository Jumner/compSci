#include "include.hpp"

#include <string>
#include <vector>
#include <iostream>

static PyObject* readFilePy(PyObject* self, PyObject* args) {
	const char* path;
	if(!PyArg_ParseTuple(args, "s", &path)) return 0;
	std::vector<std::string> lines = readFile(path);	
	std::vector<choice> choices = {};
	for(std::string line: lines) {
		if (line.find("\", ") == std::string::npos) line.replace(line.find("\"]"), 3, "\", ]");
		// Fix an issue with remainder when there is only text
		// It's a bandaid solution but it will do for now
		choices.push_back(choice(line));
	}

	while(choices.size() > 1) { // This is the most brute force thing I've ever made 🤢
		// Repeat until all the elements are sorted into one
		for(int i = 0; i < choices.size(); i ++) {
			// Look for a child element with no children
			if(choices[i].childList.empty()) {
				// If the element has no children
				for(int p = 0; p < choices.size(); p ++) {
					// Look for a parent of the child
					for(int c = 0; c < choices[p].childList.size(); c ++) {
						// Look at the child names of the tested parent
						if(choices[p].childList[c] == choices[i].name) {
							// If the parent has the name of the child in its childList
							choices[p].children.push_back(choices[i]); // Put the child into the parents children vec
							choices.erase(choices.begin()+i); // Remove the child from the choices vec
							choices[p].childList.erase(choices[p].childList.begin()+c); // Remove the name of the child from the childList of the parent
						}
					}
				}
			}
		}
	}

	choices[0].print();

	return Py_BuildValue("s", "hey! It worked, I think");
	// return Py_BuildValue(key.c_str(), lines);
}

static PyObject* testFunc(PyObject* self, PyObject* args)
{
	int param; // I actually have permanent brain damage. No joke

	if (!PyArg_ParseTuple(args, "i", &param))
		return nullptr;
	std::cout << readFile("game/test.cyoa")[0] << std::endl;
	return Py_BuildValue("(ii)", param, param+1); // (ii) for a tuple of ints
}

PyMethodDef cppMethods[] = {
	{"pyName", (PyCFunction)testFunc, METH_VARARGS, 0},
	{"readFile", (PyCFunction)readFilePy, METH_VARARGS, 0},
	{0,0,0,0} // Ngl I got no clue what this does
};

static struct PyModuleDef cppModule = {
	PyModuleDef_HEAD_INIT,
	"cppGood", // Module name
	"Because I hate python with a passion", // Module description __doc__
	-1, // Do you really think I understand what this thing does?
	cppMethods // Send our methods to python 😁
};

PyMODINIT_FUNC PyInit_cppGood(void) {
	PyObject* m = PyModule_Create(&cppModule);
	if (m == nullptr) { // Make sure it worked
		return NULL; // Yikes if this happens 😬
	}
	// std::cout << "\033[96;40mHello\033[0m" << std::endl;
	std::cout << "\033[96;1mcppGoodPythonBad\033[0m" << std::endl << std::endl; // Tee hee
	return m;
}