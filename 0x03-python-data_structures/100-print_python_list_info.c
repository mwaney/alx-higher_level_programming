#include <Python.h>
/**
 * print_python_list_info - function to print python info
 * @p: a list
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyObject *info;
	int len, i, mem;

	len = Py_size(p);
	mem = ((PyListObject *)p)->allocated;
	printf("[*] Size of Python List = %d\n", len);
	printf("[*] Alocated = %d\n", mem);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		info = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(info)->tp_name);
	}
}
