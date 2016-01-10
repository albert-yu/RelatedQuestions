# RelatedQuestions

My attempt at solving one of Quora's challenges. 

https://www.quora.com/challenges#related_questions

## General approach
First of all, I wanted to have a clear idea of the meaning of "expected" path time. If we take a very simple tree (a doubly linked list with, say, five nodes), we could consider defining it as the average path time of the nodes to either leaf. This, however, makes no sense as there would be multiple nodes (2, 3, and 4, in the case of 5 nodes) with the same average time, assuming all node times are equal. I thus figured that a better definition, the one that I ultimately implemented, would be the longest possible path time (i.e. the worst case scenario). In the aforementioned five-node example, the one with the shortest longest possible path time would be 3, since it is at the "center" of the tree. 

It is known that in a tree, there are no cycles, so any path from a node to another is unique. What my algorithm does is find the chain in the tree with the longest possible travel time. Each end of this chain must be a leaf, so I can reduce the number of nodes I have to check to only the leaves. With this chain, I can find the middle node, which can vary if the chain has an even number of nodes. This middle node will have the smallest expected path time.
