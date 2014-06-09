Data-Structures
===============

This repository contains example data structures implemented in python. All implementations
were co-written with [Nathan Hubbell](https://github.com/lnhubbell). All other collaborators and
sources of inspiration are listed under the structure to which they contributed.


Structures
-----------------

**Linked List**

This implementation of a [linked list](http://en.wikipedia.org/wiki/Linked_list) includes a class that
represents the list, LinkedList(), and a class that represents an object contained in the list, Node().
Linked lists are initially empty, but can have datum added to them via a LinkedList() method.

LinkedList():

    * LinkedList(head_node=None)
        * Instantiate a LinkedList with the given Node as the first node in the list.
    * .insert(val)
        * Instantiate a Node containing val and place it at the head of the linked list.
    * .pop()
        * Return the value of the Node at the head of the list and remove the Node from the list.
    * .size()
        * Return the length of the linked list.
    * .search(val)
        * Return the first Node that holds the value; returns None if not in the linked list.
    * .remove(node)
        * Remove the given Node from the linked list; assumes node is in the list.

Node():

    *Node(value, the_next=None):
        * Instantiate a Node with a given value and a pointer to another given Node.


**Stack**

This implementation of a [stack](http://en.wikipedia.org/wiki/Stack_(abstract_data_type)) includes a
class that represents the stack, Stack(), and one that represents a datum in the stack, Data().
Stacks are initially empty, but can have datum added via a Stack() method.

Stack():

    * Stack()
        * Instantiate an empty Stack.
    * .push()
        * Add a new Data to the stack.
    * .pop()
        * Remove the Data object from the top of the stack and return its value.

Data():

    * Data(value, is_above=None)
        * Instantiate a Data with a given value on top of another given Data.


**Parenthesis checker**

This implementation of a parenthesis checker accepts a unicode string and determines whether
or not any parentheses are balanced. It returns the following values based on the number
of parenthesis:

    * 1: If there are more closed parenthesis (")") than open ("(").
    * -1: If there are more open parenthesis  than closed.
    * 0: If the parenthesis are equal in number and balanced in distribution.
    * "All the right pieces in all the wrong places." if the parenthesis are equal in number, but
        imbalanced in distribution.

This was insipired by conversations with [Lawrence Fritts](https://github.com/lfritts).