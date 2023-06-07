#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list listint_t
 * @head: Double pointer to the first of the list
 * @number: Number value of the new node
 *
 * Return: Address if the new node. Otherwise returns NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr = NULL, *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (!new || !head)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!(*head))
	{
		*head = new;
		return (new);
	}

	curr = *head;
	while (curr)
	{
		if (curr->n > new->n)
		{
			new->next = curr;
			if (!prev)
				*head = new;
			else
				prev->next = new;
			new->next = curr;
			return (new);
		}
		prev = curr;
		curr = curr->next;
	}
	prev->next = new;
	return (new);
}
