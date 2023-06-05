#include "lists.h"
/**
 * check_cycle - checks to see if there is a cycle in a linked list
 * @list: head pointer to linked list
 * Return: 1 if cycle exists, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list->next, *slow = list;

	if (list == NULL)
		return (0);
	while (fast && fast->next && slow)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
