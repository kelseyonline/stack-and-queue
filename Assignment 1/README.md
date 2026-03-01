Dear Dr. Parag & Krithika, 

I wrote my code by trying to build out everything myself, and then comparing what I wrote to the examples we did in class. For whatever worked, I kept it the same, and adjusted parts that were broken based on the model. Therefore what I created strays a little bit from how we wrote the stack and queue in our examples.

The explanation of how I wrote my code is included throughout the code as comments. Regarding time complexity, we are minimizing time usage by sticking to as many constant time operations as possible. There are only 2 instances of loops in both the stack and queue classes: the size method and __repr__. These two methods must use a while loop to iterate through the entirety of the SLL. Therefore, the time complexity here is O(n), dependent only on the size of the respective stack or queue. 

~KD