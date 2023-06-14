#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - function that outputs bytes info
 * @p: Python Object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int obj_size, i, end;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == NULL)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	obj_size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", obj_size);
	printf("  trying string: %s\n", str);

	if (obj_size >= 10)
		end = 10;
	else
		end = obj_size + 1;

	printf("  first %ld bytes:", end);

	for (i = 0; i < end; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
 * print_python_list - fucntion to print list information to output
 * @p: Python Object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	long int obj_size, i;
	PyObject *obj;
	PyListObject *list;

	obj_size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", obj_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < obj_size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
