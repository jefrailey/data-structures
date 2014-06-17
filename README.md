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

**Doubly Linked List**

This implementation of a [doubly linked list](http://en.wikipedia.org/wiki/Doubly_linked_list) includes a
class that represents the list, DoublyLinked(), and one that represents a value in the list, Node().
Doubly linked lists are initially empty, but can have values added via DoublyLinked() methods.

DoublyLinked()

    * DoublyLinked()
        *Instantiate an empty list.
    * .insert(value)
        * Add a value at the head of the list.
    * .append(value)
        * Add a value to the tail of the list.
    * .pop()
        * Return the head value and remove it from the list.
    * .shift()
        * Return the tail value and remove it from the list.
    * .remove(value)
        * Remove the first (starting at the head) matching value from the list.

Node()

    * Node(value)
        * Instantiate a node that represents a value.


**Graph**

Graph()

    * Graph()
        *Instantiate an empty graph.
    * .nodes()
        * Returns a list of all nodes in the graph.
    * .edges()
        * Returns a list of all edges in the graph.
    * .add_node(name)
        * Adds an unoconnected node named 'name' to the graph.
    * .del_node(name)
        * Deletes a node named 'name' and all the edges connected to it.
    * .add_edge(name1, name2)
        * Adds an edge to the graph connecting nodes named 'name1' and 'name2'. These nodes are created if they don't exist.
    * .del_edge(name1, name2)
        * Deletes the edge between 'name1' and 'name2' if it exists.
    * .has_node(name)
        * Returns True if the node named 'name' is in the graph. False otherwise.
    * .adjacent(name1, name 2)
        * Returns True if 'name1' and 'name2' have an edge between them. Returns false if they do not. Raises a KeyError if either of them don't exist.
    * .neighbors(name)
        * Returns a list of all nodes connected to node named 'name'.
