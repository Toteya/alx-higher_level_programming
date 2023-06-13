#include "lists.h"

/**
 * is_palindrome - Checks if a singly-linked list listint_t is a palindrome
 * @head: Double pointer to the first node of the list
 *
 * Return: 1 if the list is a palindrome. Otherwise return 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *pl, *pr, *next, *prev;
	unsigned int i = 0, n, even;

	if (!(*head) || (*head)->next == NULL)
		return (1);

	pl = *head;
	while (pl->next)
	{
		pl = pl->next;
		i++;
	}
	even = i % 2;
	n = (i / 2) + 1 + even;

	pl = pr = *head;
	i = 0;
	while (pr)
	{
		if (i == n)
		{
			next = pr->next;
			pr->next = NULL;
			prev = pr;
			pr = next;
		}
		else if (i > n)
		{
			next = pr->next;
			pr->next = prev;
			prev = pr;
			pr = next;
		}
		else
		{
			pr = pr->next;
		}
		i++;
	}

	pr = prev;
	while (pr)
	{
		if (pl->n != pr->n)
			return (0);
		pl = pl->next;
		pr = pr->next;
	}
	return (1);
}
