
class Node:

    def  __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None
    
    def Insert_Begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    """ Asiga a la variable node la clase Node y pasa el data y la cabeza actual de la lista como siguiente
        y esa variable node pasa a hacer la nueva cabeza"""
    
    def Insert_End(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)

    """ Primero verifica si la lista esta vacia, en caso de que si, ese elemento pasa a ser la cabeza y no tiene un siguiente,
        en caso de que no este vacio iteramos por el siguiente elemento de cada uno de los elementos y cuando el siguiente elemento este vacio
        implica que estamos al final, alli es donde agregamos el nuevo elemento"""

    def Insert_Values(self,data_list):
        for data in data_list:
            self.Insert_Begining(data)
    """Itera por la lista y por cada elemento lo añade al principio, OJO!! Se puede modificar para que reinicie la lista encadenada y a su vez
        ponerla en diferente orden"""

    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def Remove_at(self,index):
        if index <0 or index>=self.length():
            print('Index out of reach')
            return

        if index == 0:
            self.head=self.head.next
            return
            
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                Node_to_remove=itr.next
                Node_to_connect=Node_to_remove.next
                itr.next=Node_to_connect
                break
            itr=itr.next
            count+=1
    
    def Insert_at(self,data,index):
        if index <0 or index>=self.length():
            print('Index out of reach')
            return

        if index==0:
            self.Insert_Begining(data)
        
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node_to_attach=itr.next
                itr.next=Node(data,node_to_attach)
                break
            itr=itr.next
            count+=1
    
    def Get_element(self,index):
        if index<0 or index>self.length():
            print("Index out of range")
            return
        if index == 0:
            return self.head.data

        itr=self.head
        count=0
        while itr:
            if index == count:
                return self.head.data
            itr=itr.next
            count+=1
    
    def Remove_by_value(self,data):
        itr=self.head
        while itr:
            if itr.next == None:
                print('that element is not in list')
                return
            if itr.next.data == data:
                node_to_delet=itr.next
                node_to_reconect=node_to_delet.next
                itr.next=node_to_reconect
                return
            itr=itr.next

    def Iterator(self):
        if self.head is None:
            print('Linked list is empty')
            return 
        itr=self.head
        full_list=[]
        while itr:
            full_list.append(itr.data)
            itr=itr.next
        return full_list
    
    def Is_element_present(self,data):
        itr=self.head
        couunt=0
        while itr:
            if itr.data==data:
                return couunt
            couunt+=1
            itr=itr.next
        return 0
        
            
    def printing(self):
        if self.head is None:
            print('Linked list is empty')
            return 
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+','
            itr=itr.next
        print(llstr)
    

if __name__=='__main__':
    ll=Linked_list()
    #ll.Insert_Begining(5)
    ll.Insert_Begining(3)
    #ll.Insert_End(6)
    ll.Insert_Values([10,50,90])
    ll.printing()
    ll.Insert_at('hola', 2)
    ll.Insert_at('ye', 0)
    ll.printing()
    print(ll.Is_element_present('hol'))
    print(ll.Get_element(3))
    print(ll.Iterator())
    ll.Remove_by_value(10)
    ll.printing()
    ll.Remove_by_value(999)
 