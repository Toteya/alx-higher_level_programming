#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list has a cycle
 * @list: The list to be checked
 *
 * Return: 0 if there is no cycle, and 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *mark;

	mark = list;

	while (list->next)
	{
		list = list->next;
		if (mark == list)
			return (1);
	}
	return (0);
}
