#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert node
 * @head: head
 * @number: num to add
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (temp->next)
	{
		if ((temp->next)->n >= number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}

	new->next = NULL;
	temp->next = new;

	return (new);
}
