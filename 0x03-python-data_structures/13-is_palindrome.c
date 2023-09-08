#include "lists.h"
/**
 * is_palindrome - checks if is palindrome
 * @head: pointer to pointer to head node
 *
 * Return: 0 if palindrome or 1 on failure
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow->next = reverseList(slow->next);
	slow = slow->next;

	listint_t *current = *head;

	while (slow != NULL)
	{
		if (current->data != slow->data)
			return (0);

		current = current->next;
		slow = slow->next;
	}

	return (1);
}
