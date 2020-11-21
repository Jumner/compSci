#include "Python.h"

#include <string>
#include <iostream>

static PyObject* testFunc(PyObject* self, PyObject* args)
{
	int param; // I actually have permanent brain damage. No joke

	if (!PyArg_ParseTuple(args, "i", &param))
		return nullptr;

	return Py_BuildValue("i", param+1);
}

PyMethodDef cppMethods[] = {
	{"pyName", (PyCFunction)testFunc, METH_VARARGS, 0},
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
	std::cout << "cppGoodPythonBad" << std::endl << std::endl; // Tee hee
	return m;
}