#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Print some basic info about Python lists (PyObject)
 * @p: Pointer to the PyObject 
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	if (!p)
	{
		return;
	}

	PyListObject *list;
	Py_ssize_t size, i;
	PyTypeObject *type;

	size = PyList_Size(p);
	printf("[*] Size of Python List = %lu\n", size);
	list = (PyListObject *) p;
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(PyList_GetItem(p, i));
		printf("Element %lu: %s\n", i, type->tp_name);
	}
}
