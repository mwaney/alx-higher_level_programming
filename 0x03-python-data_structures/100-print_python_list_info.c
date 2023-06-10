#include <Python.h>
/**
 * print_python_list_info - function to print python info
 * @p: a list
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int len, i, mem;

	len = Py_SIZE(p);
	mem = ((PyListObject *)p)->allocated;
	printf("[*] Size of Python List = %d\n", len);
	printf("[*] Alocated = %d\n", mem);

	for (i = 0; i < len; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
