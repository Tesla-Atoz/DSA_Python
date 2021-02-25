# -*- coding: utf-8 -*-
"""Queue.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11SmVnKBwuhVvclt8w770-HDIyneTy0jY
"""

from collections import deque

class Queue :
  def __init__(self):
    self.buffer = deque()

  def enqueue(self,val):
    self.buffer.appendleft(val)
  
  def dequeue(self):
    return self.buffer.pop()
  
  def is_empty(self):
    return len(self.buffer) == 0
  
  def size(self):
    return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

from collections import deque
import time
import threading

orders_menu = deque()

def place_order(orders):
  for order in orders:
    print('placing order',order)
    orders_menu.appendleft(order)
    time.sleep(0.5)
 

def serve_order():
  time.sleep(1)
  while len(orders_menu):
    order = orders_menu.pop()
    print('Now serving :',order)
    time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target = place_order,args=(orders,))
t2 = threading.Thread(target = serve_order)

t1.start()

t2.start()

t1.join()
t2.join()

print("ended")