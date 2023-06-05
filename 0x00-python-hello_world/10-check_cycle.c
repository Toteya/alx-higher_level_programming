#include "lists.h"

void free_listaddr(listaddr_t *node);

/**
 * check_cycle - Checks if a singly-linked list has a cycle
 * @list: The list to be checked
 *
 * Return: 0 if there is no cycle, and 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	/* nodes in a register list of all the addresses in list */
	listaddr_t *reg_head, *reg, *new;

	if (!list)
		return (0);

	reg_head = malloc(sizeof(listaddr_t));
	if (!reg_head)
		exit(EXIT_FAILURE);
	reg_head->val = list;
	reg_head->next = NULL;

	reg = reg_head;

	while (list)
	{
		list = list->next;
		while (reg)
		{
			if (reg->val == list)
			{
				free_listaddr(reg_head);
				return (1);
			}
			reg = reg->next;
		}
		reg = reg_head;
		while (reg->next)
			reg = reg->next;
		new = malloc(sizeof(listaddr_t));
		if (!new)
		{
			free_listaddr(reg_head);
			exit(EXIT_FAILURE);
		}
		new->val = list;
		new->next = NULL;
		reg->next = new;
		reg = reg_head;
	}
	free_listaddr(reg_head);
	return (0);
}

/**
 * free_listaddr - Frees a listaddr_t list
 * @node: Pointer to the first node of the list to be freed
 *
 * Return: Nothing.
 */
void free_listaddr(listaddr_t *node)
{
	listaddr_t *ptr;

	ptr = node;
	while (ptr)
	{
		node = node->next;
		free(ptr);
		ptr = node;
	}
}
