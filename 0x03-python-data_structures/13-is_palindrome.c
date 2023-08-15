#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * find_middle - Finds the middle node of a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the middle node.
 */
listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	return (slow);
}

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	int is_palindrome = 1;
	listint_t *middle = find_middle(*head);
	listint_t *second_half = reverse_list(middle);

	listint_t *temp1 = *head, *temp2 = second_half;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
		{
			is_palindrome = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	reverse_list(second_half);

	return (is_palindrome);
}
