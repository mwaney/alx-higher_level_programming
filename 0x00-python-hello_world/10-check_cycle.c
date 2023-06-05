#include "lists.h"
/**
 * check_cycle - checks to see if there is a cycle in a linked list
 * @list: head pointer to linked list
 * Return: 1 if cycle exists, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
