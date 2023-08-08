#include "lists.h"

/**
* insert_node - inserts a number in a singly linked list
* @head: The head of the linked list
* @number: The number to be inserted.
*
*Return: address of new node or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if(!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}

	while (current->next && number > current->next->n)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return new_node;
}
