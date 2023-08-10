#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: A pointer to the head of a linked list
 *
 * Return: 1 if a cycle exists, 0 other wise
 */
int check_cycle(listint_t *list)
{
	listint_t *first_ptr;
	listint_t *second_ptr;

	if (!list)
		return (0);

	first_ptr = second_ptr = list;

	while (first_ptr && second_ptr && second_ptr->next)
	{
		first_ptr = first_ptr->next;
		second_ptr = second_ptr->next;

		if (first_ptr == second_ptr)
			return (1);
	}
	return (0);
}
