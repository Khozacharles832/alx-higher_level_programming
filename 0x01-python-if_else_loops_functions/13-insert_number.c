#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - insert a number into a sorted singly linked linked list
 * @head: A pointer to the head of the linked list
 * @number: the number to insert
 *
 * Return: NULL if error, else the a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);
	insert->n = number;

	if (node == NULL || node->n >= number)
	{
		insert->next = node;
		*head = insert;
		return (insert);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	insert->next = node->next;
	node->next = insert;

	return (insert);
}
