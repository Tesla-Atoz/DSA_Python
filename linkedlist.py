# -*- coding: utf-8 -*-
"""LinkedList.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YfUWp9h9KbYfnBM25cOte0dUifeGtFx0
"""

class Node:
  def __init__(self,data=None,next =None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self,data):
    node = Node(data,self.head)
    self.head = node

  def insert_at_end(self,data):
    if self.head is None:
      self.head = Node(data, None)
      return

    itr = self.head
    while itr.next :
      itr = itr.next

    itr.next = Node(data,None)

  def insert_values(self,data_list):
    self.head =None
    for data in data_list:
      self.insert_at_end(data)

  def get_length(self):
    count = 0
    itr = self.head
    while itr :
      count +=1
      itr =itr.next
    return count

  def print(self):
    if self.head is None:
      print("Empty list")
      return
    
    itr = self.head
    llstr = ""
    while (itr):
      llstr += str(itr.data) + '-->'
      itr = itr.next

    print(llstr)
  
  def remove_at(self,index):
      if index <0 or index >= self.get_length():
        raise Exception("invalid error")
      
      if index == 0:
        self.head = self.head.next
        return
      
      count = 0
      itr = self.head
      while itr:
        if count == index -1:
          itr.next = itr.next.next
          break

        itr = itr.next
        count+=1

  def insert_at(self, index,data):
    if index <0 or index >= self.get_length():
        raise Exception("invalid index")

    if index == 0:
      self.insert_at_beginning(data)
      return
    
    count = 0
    itr = self.head
    while itr :
      if count == index -1:
        node = Node(data,itr.next)
        itr.next = node
        break
      
      itr = itr.next
      count+=1




if __name__ == '__main__':
  ll= LinkedList()
  ll.insert_at_beginning(5)
  ll.insert_at_beginning(4)

  ll.insert_at_end(12)
  ll.insert_at_end(1)
  
  ll.print()
  ll.remove_at(3)
  ll.print()
  ll.insert_at(1,3)
  ll.print()
  print(ll.get_length())