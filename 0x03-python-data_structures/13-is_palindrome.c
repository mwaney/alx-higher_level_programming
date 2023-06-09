#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - function to check if linked list is a palindrome
 * @head: double pointer to head of linked list
 * Return: 1 if its a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head, *ptr1 = *head;
	listint_t *prev = NULL, *next = NULL;
	listint_t *beg, *foll;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (ptr1 && ptr1->next)
	{
		ptr = ptr->next;
		ptr1 = ptr1->next->next;
	}
	while (ptr)
	{
		next = ptr->next;
		ptr->next = prev;
		prev = ptr;
		ptr = next;
	}
	beg = *head;
	foll = prev;
	while (foll)
	{
		if (beg->n != foll->n)
			return (0);
		beg = beg->next;
		foll = foll->next;
	}
	return (1);
}
