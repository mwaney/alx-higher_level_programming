#include <Python.h>
/**
 * print_python_list_info - function to print python info
 * @p: a list
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int obj_length, i, mem_alc;
	PyObject *obj;

	obj_length = Py_SIZE(p);
	mem_alc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", obj_length);
	printf("[*] Allocated = %d\n", mem_alc);

	for (i = 0; i < obj_length; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
