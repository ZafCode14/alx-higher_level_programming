#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1 = NULL;
	listint_t *temp2 = NULL;

	if (list == NULL)
		return (0);
	temp1 = list;
	temp2 = list;

	while (temp1 && temp2 && temp2->next)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;

		if (temp1 == temp2)
			return (1);
	}
	return (0);
}
