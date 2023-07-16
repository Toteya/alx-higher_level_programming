#include "lists.h"

/**
 * is_palindrome - Checks if a singly-linked list listint_t is a palindrome
 * @head: Double pointer to the first node of the list
 *
 * Return: 1 if the list is a palindrome. Otherwise return 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t **ptr, *p;
	unsigned int i = 0, j;

	if (!(*head) || (*head)->next == NULL)
		return (1);

	p = *head;
	while (p->next)
	{
		p = p->next;
		i++;
	}

	ptr = malloc(sizeof(listint_t *) * (i + 1));
	if (!ptr)
		exit(EXIT_FAILURE);

	*ptr = *head;
	for (i = 0; ptr[i]->next; i++)
	{
		ptr[i + 1] = ptr[i]->next;
	}

	j = i;
	for (i = 0; i < j; i++, j--)
	{
		if (ptr[i]->n != ptr[j]->n)
		{
			free(ptr);
			return (0);
		}
	}
	free(ptr);
	return (1);
}
