#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that Inserts a 
 * number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to be inserted in the node.
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *current;

	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	
	if (*head == NULL || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		current = *head;
		while (current->next && current->next->n < number)
		{
			current = current->next;
		}
		node->next = current->next;
		current->next = node;
	}
	return (node);
}
