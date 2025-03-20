"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

    Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
    Obtener el número de elementos almacenados (tamaño).
    Saber si la pila o la cola está vacía.
    Vaciar completamente la pila o la cola.
    Para el caso de la pila:
        Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
        Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina. 
        Leer el elemento superior de la pila sin retirarlo (top).
    Para el caso de la cola:
        Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
        Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.
        Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

"""
class Stack:
    def __init__(self, initial_values=None):
        self.stack = initial_values if initial_values else []

    def push(self, value):
        self.stack.insert(0, value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop(0)

    def top(self):
        if self.is_empty():
            raise IndexError("Top from empty stack")
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

class Queue:
    def __init__(self, initial_values=None):
        self.queue = initial_values if initial_values else []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []