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
		choices.push_back(choice(line));
	}
	for(choice c: choices) {
		c.print();
	}
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
	std::cout << "cppGoodPythonBad" << std::endl; // Tee hee
	std::cout << "Wait did I really get it working?" << std::endl; // Hell yea I did! 🥴
	return m;
}