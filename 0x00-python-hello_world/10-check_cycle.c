#include "lists.h"

/**
* check_cycle - A function that checks if a singly linked list has a cycle in it
* @list: A pointer to the singly linked list that will be traverse
* 
*Return: 1 if there is a cycle, 0 if otherwise.
*/

int check_cycle(listint_t *list)
{
	listint_t *l1 = list;
	listint_t *l2 = list;

	while(l1 != NULL && l2 != NULL && l2->next != NULL)
	{
		l1 = l1->next;
		l2 = l2->next->next;

		if (l1 == l2)
			return (1);
	}

	return (0);
}
