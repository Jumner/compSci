#include "Python.h"

#include <string>
#include <iostream>

static PyObject* testFunc(PyObject* self, PyObject* args)
{
	PyObject* param = nullptr; // Not even the nullptr can save me 😿


	if (!PyArg_ParseTuple(args, "i", &param))
		return nullptr; // Nor can this one

	return Py_BuildValue("s", "Bruh segmentation error my ass");
	// One the bright side it takes an int and returns a string
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
	return m;
}