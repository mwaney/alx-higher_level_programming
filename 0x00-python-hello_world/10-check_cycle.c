#include "lists.h"
/**
 * check_cycle - checks to see if there is a cycle in a linked list
 * @list: head pointer to linked list
 * Return: 1 if cycle exists, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slowPtr = list;
	listint_t *fastPtr = list;

	if (list == NULL)
		return (0);

	while (fastPtr && fastPtr->next && slowPtr)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;
		if (slowPtr == fastPtr)
			return (1);
	}

	return (0);
}
