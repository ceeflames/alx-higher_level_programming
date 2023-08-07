#include "lists.h"

/**
 * check_cycle - check linked list
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;

	if (ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	else
		return (0);
	while (ptr != list)
	{
		if (ptr->next == NULL)
		{
			return (0);
		}
		ptr = ptr->next;
	}
	return (1);
}
