class Node:

    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class SinglyLinkedList:

    def __init__(self,head=None):
        self.head=head
    
    def end_insertion(self,node_data_value):
        new_node=Node(node_data_value)

        if self.head is None:
            self.head=new_node
            return
        
        current_data=self.head
        while current_data.next is not None:
            current_data=current_data.next
        current_data.next=new_node
    
    def start_insertion(self,node_data_value):
        new_node=Node(node_data_value)
        new_node.next=self.head
        self.head=new_node
    
    def display_list(self):

        current_data=self.head
        while current_data is not None:
            print(current_data.data,end="->")
            current_data=current_data.next

        print('None')

list1=SinglyLinkedList()

n=int(input("Enter number of nodes in the list: "))

for nodes in range(n):
    node_data=int(input("Enter node data: "))
    list1.end_insertion(node_data)

list1.start_insertion(60)

list1.display_list()