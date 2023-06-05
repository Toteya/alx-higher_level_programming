#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/* Data Structures */

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct listaddr_s - singly-linked list
 * @val: Address of a list
 * @next: Pointer to the next node
 *
 * Description: Stores the unique addresses of the nodes in a listint_t list.
 */
typedef struct listaddr_s
{
	listint_t *val;
	struct listaddr_s *next;
} listaddr_t;

/* Function Prototypes */

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
