#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer
 *
 * Return: 0 if it is not, 1 if it is
 */
int is_palindrome(listint_t **head);
{
	int i, j, k, li;
	int *name;
	listint_t *now;
	listint_t *new;

	*now = *head;
	if (*head == NULL)
		return (1);
	i = 0;
	while (now != NULL)
	{
		now = now->next;
		i++;
	}
	name = malloc(sizeof(int) * i);
	if (name == NULL)
		return (0);
	new = *head;
	for (j = 0; new != NULL && i < n; i++)
	{
		name[i] = new->i;
		new = new->next;
	}
	for (j = 0; j < i/2; j++)
	{
		li = i - j - 1;
		if (name[j] != name[li])
		{
			free(name);
			return (0);
		}
	}
	free(name);
	return (1);
}
