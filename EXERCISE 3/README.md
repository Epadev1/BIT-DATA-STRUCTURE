**Project 85: Data Structures in Everyday Rwandan Contexts – Stacks and Queues
Overview**
Project 85 is an educational exploration of fundamental data structures—specifically stacks and queues—applied to practical, real-world scenarios inspired by daily life in Rwanda. It combines hands-on practical tasks, algorithmic challenges, and reflective discussions to illustrate the Last-In-First-Out (LIFO) principle of stacks and the First-In-First-Out (FIFO) principle of queues. The project draws from relatable contexts like mobile money transactions (MoMo), university chapter navigation (UR), telecom services (Airtel), hospital patient lines (CHUK), and formal events like graduation ceremonies. Through these, learners understand how these structures promote efficiency, fairness, and order in operations. The project is divided into two main sections: Stack Questions and Queue Questions, each with practical exercises, a challenge, and a reflection.
**Stack Questions Section**

This section focuses on stacks, where elements are added (pushed) and removed (popped) from the top, following LIFO. It demonstrates how stacks are ideal for reversible operations but can lead to inefficiencies in sequential processing.

Practical (Rwanda): 
**In MoMo, push ["Enter Number", "Enter Amount", "Confirm"]. Undo one. Which remains?**
This exercise simulates a mobile money (MoMo) transaction workflow in Rwanda, where steps like entering a phone number, amount, and confirmation are pushed onto a stack. Undoing the last action (popping "Confirm") leaves the earlier steps intact, highlighting stacks' utility in "undo" features common in apps like MTN MoMo.

**Practical (Rwanda): UR pushes ["Chapter1", "Chapter2", "Chapter3"]. Pop all. Which is left?**
Modeled after navigating academic chapters at the University of Rwanda (UR), this task pushes chapter titles onto a stack and then pops them all, resulting in an empty structure. It shows how exhaustive removal in LIFO order clears the stack, akin to completing a sequence of study modules.

**Challenge: Reverse "DATAQUEUE" using stack.**
A problem-solving task requiring the reversal of the string "DATAQUEUE" (a nod to queue concepts) via a stack. Characters are pushed in original order and popped to form the reversed string ("EUEUQATAD"), demonstrating stacks' natural role in reversing sequences, useful in text processing or error recovery.
**Reflection: Why stack does not suit long queues?**
A theoretical discussion on why LIFO stacks fail in prolonged waiting lines, such as Rwandan market or bank queues. They unfairly prioritize recent arrivals, causing inefficiency and discontent, unlike FIFO systems that respect arrival order.

**Queue Questions Section**

_This section emphasizes queues, where elements are added to the rear (enqueued) and removed from the front (dequeued), enforcing FIFO. It underscores queues' role in fair, orderly processing in service-oriented environments._
**Practical (Rwanda): At Airtel, 7 clients queue. After 3 served, who is front?**
Inspired by customer service lines at Airtel stores in Rwanda, this simulates a queue of seven clients (e.g., C1 to C7). Serving the first three advances the line, positioning the fourth client (C4) at the front, illustrating FIFO's progression in telecom billing or top-up services.

**Practical (Rwanda): At CHUK, 5 patients queue. Who is second served?**

Based on patient triage at the Centre Hospitalier Universitaire de Kigali (CHUK), this involves a queue of five patients (P1 to P5). The second served is P2, after dequeuing P1, emphasizing queues' fairness in healthcare to prevent jumping the line.

**Challenge: Queue vs stack for graduation ceremony entry. Which is proper?**
An comparative analysis for managing entry at a Rwandan university graduation ceremony. A queue ensures attendees enter in arrival order (fair and orderly), while a stack would reverse it (unfair, favoring latecomers). The queue is deemed proper for maintaining decorum in cultural events.

**Reflection: Why FIFO matches fairness in ceremonies?**
A conceptual exploration of how FIFO queues embody equity in formal gatherings like weddings or graduations in Rwanda. By honoring arrival times, they foster trust and harmony, avoiding the chaos of priority reversals and aligning with communal values of patience and justice.

