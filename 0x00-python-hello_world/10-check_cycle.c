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

	while (list)
	{
		mark = list;
		list = list->next;
		while (list)
		{
			if (list == mark)
			{
				return (1);
			}
			list = list->next;
		}
		list = mark->next;
	}
	return (0);
}
