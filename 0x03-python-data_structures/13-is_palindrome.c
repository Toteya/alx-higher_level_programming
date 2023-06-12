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
	unsigned int i = 0, n;
	int even;

	if (!(*head) || (*head)->next == NULL)
		return (1);

	p = *head;
	while (p->next)
	{
		p = p->next;
		i++;
	}

	even = i % 2;
	n = i /  2;
	ptr = malloc(sizeof(listint_t *) * (n + 1));
	if (!ptr)
		exit(EXIT_FAILURE);

	*ptr = *head;
	for (i = 0; i < n; i++)
	{
		ptr[i + 1] = ptr[i]->next;
	}

	p = ptr[i + even];
	while (p)
	{
		if (ptr[i]->n != p->n)
		{
			free(ptr);
			return (0);
		}
		p = p->next;
		i--;
	}
	free(ptr);
	return (1);
}
