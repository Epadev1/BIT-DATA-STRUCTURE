#Stack practical in MOMO push
print("MOMO PUSH")
stack=[]
stack.append("Enter Number")
stack.append("Enter Amount")
stack.append("Confirm")

stack.pop()
print("Remaining stack in MOMO:",stack)

#Stack practical in UR push
print("UR PUSH")
stack=[]
stack.append("Chapter1")
stack.append("Chapter2")
stack.append("Chapter3")

stack.pop()
stack.pop()
stack.pop()
print ("Remaining stack in UR:",stack)



#queue practice in Airtel when 7clients are served 
print("AIRTEL QUEUE")
queue=[]
queue.append("Client 1")
queue.append("Client 2")
queue.append("Client 3")
queue.append("Client 4")
queue.append("Client 5")
queue.append("Client 6")

#after 3 served who is front
queue.pop(0)
queue.pop(0)
queue.pop(0)
print("Client in front after 3 served is: ",queue[0])


#QueueAt CHUK when 5patients are served
print("CHUK QUEUE")
queue=[]
queue.append("Patient 1")
queue.append("Patient 2")
queue.append("Patient 3")
queue.append("Patient 4")
queue.append("Patient 5")
queue.append("Patient 6")
#after 3 served who is in front
queue.pop(0)
print("The second served Patient is: ",queue[0])


