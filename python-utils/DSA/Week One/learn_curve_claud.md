# 30-Day Python Data Structures & Algorithms Interview Roadmap

## Overview
A comprehensive 30-day roadmap designed for junior software engineer interviews, focusing on Python implementations with 2-3 hours daily commitment. Each day balances theory, practice problems, and hands-on projects.

---

## **Week 1: Foundations & Basic Data Structures**

### **Day 1: Arrays & Lists**
**Topic:** Python Lists, Array Operations, Basic Algorithms

**Learning Resources:**
- [HackerRank Arrays Domain](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays)
- [YouTube: Arrays in Python - CS Dojo](https://www.youtube.com/watch?v=QJw8pLkMm90)
- [YouTube: Array Data Structure - mycodeschool](https://www.youtube.com/watch?v=55l-aZ7_F24)

**Key Concepts:**
- List operations (append, insert, delete, slice)
- Time complexity of operations
- 2D arrays/matrices
- Array traversal patterns

**Practice Problems (HackerRank):**
- [Array DS](https://www.hackerrank.com/challenges/arrays-ds)
- [2D Array - DS](https://www.hackerrank.com/challenges/2d-array)
- [Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation)

**Mini Project:** **Personal Expense Tracker**
Create a command-line expense tracker that stores expenses in lists and provides operations like add, view, and calculate totals by category.

```python
# Sample structure
expenses = []
categories = ["Food", "Transport", "Entertainment", "Bills"]
```

---

### **Day 2: Strings & String Manipulation**
**Topic:** String Processing, Pattern Matching, String Algorithms

**Learning Resources:**
- [HackerRank Strings](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=strings)
- [YouTube: String Algorithms - Abdul Bari](https://www.youtube.com/watch?v=GTJr8OvyEVQ)
- [YouTube: Python String Methods](https://www.youtube.com/watch?v=k9TUPpGqYTo)

**Key Concepts:**
- String immutability in Python
- String methods (split, join, replace, etc.)
- Pattern matching basics
- String comparison and sorting

**Practice Problems (HackerRank):**
- [Super Reduced String](https://www.hackerrank.com/challenges/reduced-string)
- [CamelCase](https://www.hackerrank.com/challenges/camelcase)
- [Strong Password](https://www.hackerrank.com/challenges/strong-password)

**Mini Project:** **Text Analyzer Tool**
Build a tool that analyzes text files for word count, character frequency, palindromes, and basic statistics.

---

### **Day 3: Linked Lists - Basics**
**Topic:** Singly Linked Lists, Basic Operations

**Learning Resources:**
- [HackerRank Linked Lists](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=linked-lists)
- [YouTube: Linked Lists - mycodeschool](https://www.youtube.com/watch?v=NobHlGUjV3g)
- [YouTube: Linked List in Python - Corey Schafer](https://www.youtube.com/watch?v=6r62JV_V9SU)

**Key Concepts:**
- Node structure and pointers
- Insertion (head, tail, middle)
- Deletion operations
- Traversal techniques

**Practice Problems (HackerRank):**
- [Print the Elements of a Linked List](https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list)
- [Insert a node at the head](https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list)
- [Insert a node at the tail](https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list)

**Mini Project:** **Simple Music Playlist**
Create a linked list-based music playlist where songs can be added, removed, and played in sequence.

---

### **Day 4: Linked Lists - Advanced**
**Topic:** Doubly Linked Lists, Circular Lists, Advanced Operations

**Learning Resources:**
- [YouTube: Doubly Linked List - mycodeschool](https://www.youtube.com/watch?v=VOQNf1VxU3Q)
- [YouTube: Reverse a Linked List - Back To Back SWE](https://www.youtube.com/watch?v=MRe3UsRadKw)

**Key Concepts:**
- Doubly linked list implementation
- Reversing linked lists
- Detecting cycles (Floyd's algorithm)
- Merging linked lists

**Practice Problems (HackerRank):**
- [Reverse a linked list](https://www.hackerrank.com/challenges/reverse-a-linked-list)
- [Delete a Node](https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list)
- [Find Merge Point](https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists)

**CSES Problems:**
- [CSES: Missing Number](https://cses.fi/problemset/task/1083)

**Mini Project:** **Browser History Simulator**
Implement browser forward/back functionality using doubly linked lists.

---

### **Day 5: Stacks**
**Topic:** Stack Implementation and Applications

**Learning Resources:**
- [HackerRank Stacks](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=stacks)
- [YouTube: Stack Data Structure - mycodeschool](https://www.youtube.com/watch?v=F1F2imiOJfk)
- [YouTube: Valid Parentheses - Back To Back SWE](https://www.youtube.com/watch?v=CCyDHO1p4wI)

**Key Concepts:**
- LIFO principle
- Stack operations (push, pop, peek, isEmpty)
- Applications: balanced parentheses, expression evaluation
- Python implementation using lists

**Practice Problems (HackerRank):**
- [Balanced Brackets](https://www.hackerrank.com/challenges/balanced-brackets)
- [Equal Stacks](https://www.hackerrank.com/challenges/equal-stacks)
- [Maximum Element](https://www.hackerrank.com/challenges/maximum-element)

**Mini Project:** **Calculator with Parentheses**
Build a calculator that can evaluate mathematical expressions with proper parentheses handling using stacks.

---

### **Day 6: Queues**
**Topic:** Queue Implementation, Variants, and Applications

**Learning Resources:**
- [HackerRank Queues](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=queues)
- [YouTube: Queue Data Structure - mycodeschool](https://www.youtube.com/watch?v=wjI1WNcIntg)
- [YouTube: Circular Queue - GeeksforGeeks](https://www.youtube.com/watch?v=ka-2kZK7McM)

**Key Concepts:**
- FIFO principle
- Queue operations (enqueue, dequeue, front, rear)
- Circular queues and deques
- Priority queues introduction

**Practice Problems (HackerRank):**
- [Queue using Two Stacks](https://www.hackerrank.com/challenges/queue-using-two-stacks)
- [Truck Tour](https://www.hackerrank.com/challenges/truck-tour)

**Mini Project:** **Task Scheduler Simulator**
Create a task scheduling system where tasks are queued and processed in FIFO order with priority levels.

---

### **Day 7: Hash Tables & Dictionaries**
**Topic:** Hash Maps, Dictionary Operations, Collision Handling

**Learning Resources:**
- [YouTube: Hash Tables - CS50](https://www.youtube.com/watch?v=nvzVHwrrub0)
- [YouTube: Hash Maps Explained - Back To Back SWE](https://www.youtube.com/watch?v=shs0KM3wKv8)
- [HackerRank Python Domain - Dictionaries](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-dict-hashmaps)

**Key Concepts:**
- Hash function concepts
- Dictionary operations in Python
- Collision handling strategies
- Time complexity analysis

**Practice Problems (HackerRank):**
- [Ransom Note](https://www.hackerrank.com/challenges/ctci-ransom-note)
- [Two Strings](https://www.hackerrank.com/challenges/two-strings)
- [Sherlock and Anagrams](https://www.hackerrank.com/challenges/sherlock-and-anagrams)

**Mini Project:** **Word Frequency Counter & Autocomplete**
Build a system that counts word frequencies in text files and provides autocomplete suggestions based on frequency.

---

## **Week 2: Trees & Recursion**

### **Day 8: Binary Trees - Basics**
**Topic:** Tree Structure, Traversals, Basic Operations

**Learning Resources:**
- [HackerRank Trees](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=trees)
- [YouTube: Binary Trees - mycodeschool](https://www.youtube.com/watch?v=H5JubkIy_p8)
- [YouTube: Tree Traversals - Abdul Bari](https://www.youtube.com/watch?v=gm8DUJJhmY4)

**Key Concepts:**
- Tree terminology (root, leaf, height, depth)
- Tree traversals (inorder, preorder, postorder, level-order)
- Binary tree properties
- Tree implementation in Python

**Practice Problems (HackerRank):**
- [Tree: Preorder Traversal](https://www.hackerrank.com/challenges/tree-preorder-traversal)
- [Tree: Inorder Traversal](https://www.hackerrank.com/challenges/tree-inorder-traversal)
- [Tree: Postorder Traversal](https://www.hackerrank.com/challenges/tree-postorder-traversal)

**Mini Project:** **Family Tree Generator**
Create a family tree structure where you can add family members and traverse relationships.

---

### **Day 9: Binary Search Trees**
**Topic:** BST Properties, Search, Insert, Delete

**Learning Resources:**
- [YouTube: Binary Search Trees - mycodeschool](https://www.youtube.com/watch?v=pYT9F8_LFTM)
- [YouTube: BST Insert and Search - Back To Back SWE](https://www.youtube.com/watch?v=LwpLXm3eb6A)

**Key Concepts:**
- BST properties and invariants
- Search, insert, delete operations
- BST validation
- In-order traversal gives sorted sequence

**Practice Problems (HackerRank):**
- [Binary Search Tree: Insertion](https://www.hackerrank.com/challenges/binary-search-tree-insertion)
- [Tree: Height of a Binary Tree](https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree)

**CSES Problems:**
- [CSES: Subordinates](https://cses.fi/problemset/task/1674)

**Mini Project:** **Personal Contact Book**
Implement a contact management system using BST for efficient searching and sorting.

---

### **Day 10: Recursion & Backtracking Basics**
**Topic:** Recursive Thinking, Base Cases, Simple Backtracking

**Learning Resources:**
- [HackerRank Recursion](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=recursion)
- [YouTube: Recursion - CS50](https://www.youtube.com/watch?v=mz6tAJMVmfM)
- [YouTube: Backtracking Algorithm - Abdul Bari](https://www.youtube.com/watch?v=DKCbsiDBN6c)

**Key Concepts:**
- Recursive function structure
- Base cases and recursive cases
- Stack overflow and optimization
- Simple backtracking patterns

**Practice Problems (HackerRank):**
- [The Power Sum](https://www.hackerrank.com/challenges/the-power-sum)
- [Recursive Digit Sum](https://www.hackerrank.com/challenges/recursive-digit-sum)
- [Fibonacci Modified](https://www.hackerrank.com/challenges/fibonacci-modified)

**Mini Project:** **Maze Solver**
Create a simple maze solver using backtracking algorithm with visualization.

---

### **Day 11: Advanced Recursion & Divide and Conquer**
**Topic:** Complex Recursive Problems, Divide and Conquer Strategy

**Learning Resources:**
- [YouTube: Divide and Conquer - MIT OpenCourseWare](https://www.youtube.com/watch?v=2YLsrmcQNKA)
- [YouTube: Master Theorem - MIT](https://www.youtube.com/watch?v=6dGWxwGRH4M)

**Key Concepts:**
- Divide and conquer methodology
- Master theorem for complexity analysis
- Recursive tree problems
- Memoization introduction

**Practice Problems (HackerRank):**
- [Password Cracker](https://www.hackerrank.com/challenges/password-cracker)
- [Crossword Puzzle](https://www.hackerrank.com/challenges/crossword-puzzle)

**CSES Problems:**
- [CSES: Weird Algorithm](https://cses.fi/problemset/task/1068)
- [CSES: Repetitions](https://cses.fi/problemset/task/1069)

**Mini Project:** **Sudoku Solver**
Build a Sudoku puzzle solver using backtracking with a simple GUI or text interface.

---

### **Day 12: Heaps & Priority Queues**
**Topic:** Binary Heaps, Heap Operations, Priority Queue Applications

**Learning Resources:**
- [YouTube: Heap Data Structure - mycodeschool](https://www.youtube.com/watch?v=t0Cq6tVNRBA)
- [YouTube: Priority Queues - CS61B Berkeley](https://www.youtube.com/watch?v=Oq2E2yGadnU)
- [Python heapq module documentation](https://docs.python.org/3/library/heapq.html)

**Key Concepts:**
- Heap properties (min-heap, max-heap)
- Heapify operations
- Python heapq module
- Priority queue implementations

**Practice Problems (HackerRank):**
- [QHEAP1](https://www.hackerrank.com/challenges/qheap1)
- [Find the Running Median](https://www.hackerrank.com/challenges/find-the-running-median)

**Mini Project:** **Hospital Emergency Room Simulator**
Create a patient management system where patients are treated based on priority using heaps.

---

### **Day 13: Tries & String Processing**
**Topic:** Trie Data Structure, Prefix Trees, String Matching

**Learning Resources:**
- [YouTube: Trie Data Structure - Tushar Roy](https://www.youtube.com/watch?v=AXjmTQ8LEoI)
- [YouTube: Implementing Trie in Python - CS Dojo](https://www.youtube.com/watch?v=AXjmTQ8LEoI)

**Key Concepts:**
- Trie structure and operations
- Prefix matching
- Space and time complexity
- Applications in autocomplete and spell checkers

**Practice Problems (HackerRank):**
- [Contacts](https://www.hackerrank.com/challenges/contacts)
- [No Prefix Set](https://www.hackerrank.com/challenges/no-prefix-set)

**Mini Project:** **Auto-complete Search Engine**
Build a search engine with auto-complete functionality using tries for efficient prefix matching.

---

### **Day 14: Review & Mock Interview**
**Topic:** Week 2 Consolidation and Practice

**Activities:**
- Review all tree concepts and implementations
- Solve 5-7 mixed problems from previous days
- Conduct a 1-hour mock interview with tree/recursion focus
- Identify weak areas for additional practice

**Practice Problems (Mixed Review):**
- [Tree: Huffman Decoding](https://www.hackerrank.com/challenges/tree-huffman-decoding)
- [Balanced Forest](https://www.hackerrank.com/challenges/balanced-forest)

**Mini Project:** **Binary Tree Visualizer**
Create a tool that can visualize binary trees with different traversal animations.

---

## **Week 3: Sorting, Searching & Advanced Algorithms**

### **Day 15: Sorting Algorithms - Part 1**
**Topic:** Basic Sorting (Bubble, Selection, Insertion)

**Learning Resources:**
- [HackerRank Sorting](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=arrays-and-sorting)
- [YouTube: Sorting Algorithms - GeeksforGeeks](https://www.youtube.com/watch?v=kPRA0W1kECg)
- [YouTube: Sorting Algorithms Visualization](https://www.youtube.com/watch?v=kPRA0W1kECg)

**Key Concepts:**
- Comparison-based sorting
- Stability in sorting
- Time and space complexity analysis
- When to use each algorithm

**Practice Problems (HackerRank):**
- [Insertion Sort - Part 1](https://www.hackerrank.com/challenges/insertionsort1)
- [Insertion Sort - Part 2](https://www.hackerrank.com/challenges/insertionsort2)
- [Correctness and the Loop Invariant](https://www.hackerrank.com/challenges/correctness-invariant)

**Mini Project:** **Sorting Algorithm Visualizer**
Create a visual comparison tool that shows how different sorting algorithms work step-by-step.

---

### **Day 16: Sorting Algorithms - Part 2**
**Topic:** Advanced Sorting (Merge, Quick, Heap Sort)

**Learning Resources:**
- [YouTube: Merge Sort - mycodeschool](https://www.youtube.com/watch?v=TzeBrDU-JaY)
- [YouTube: Quick Sort - mycodeschool](https://www.youtube.com/watch?v=COk73cpQbFQ)
- [YouTube: Heap Sort - Abdul Bari](https://www.youtube.com/watch?v=2DmK_H7IdTo)

**Key Concepts:**
- Divide and conquer sorting
- Partitioning techniques
- Randomized algorithms
- Hybrid sorting approaches

**Practice Problems (HackerRank):**
- [Quicksort 1 - Partition](https://www.hackerrank.com/challenges/quicksort1)
- [Quicksort 2 - Sorting](https://www.hackerrank.com/challenges/quicksort2)
- [Merge Sort: Counting Inversions](https://www.hackerrank.com/challenges/ctci-merge-sort-counting-inversions)

**CSES Problems:**
- [CSES: Distinct Numbers](https://cses.fi/problemset/task/1621)
- [CSES: Apartments](https://cses.fi/problemset/task/1084)

**Mini Project:** **Performance Benchmarking Tool**
Build a tool that benchmarks different sorting algorithms on various data sizes and patterns.

---

### **Day 17: Binary Search & Variants**
**Topic:** Binary Search, Binary Search on Answer, Search Space Reduction

**Learning Resources:**
- [HackerRank Search](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=search)
- [YouTube: Binary Search - CS50](https://www.youtube.com/watch?v=D5SrAga1pno)
- [YouTube: Binary Search Variations - Back To Back SWE](https://www.youtube.com/watch?v=tgVSkMA8joQ)

**Key Concepts:**
- Binary search algorithm and variants
- Search in rotated arrays
- Finding boundaries and ranges
- Binary search on answer space

**Practice Problems (HackerRank):**
- [Ice Cream Parlor](https://www.hackerrank.com/challenges/icecream-parlor)
- [Pairs](https://www.hackerrank.com/challenges/pairs)
- [Triple sum](https://www.hackerrank.com/challenges/triple-sum)

**CSES Problems:**
- [CSES: Sum of Two Values](https://cses.fi/problemset/task/1640)

**Mini Project:** **Dictionary Search Tool**
Create a spell-checker that uses binary search on a sorted word list with suggestions for misspelled words.

---

### **Day 18: Graph Basics & Representations**
**Topic:** Graph Theory Fundamentals, Adjacency Lists/Matrix

**Learning Resources:**
- [YouTube: Graph Theory Introduction - William Fiset](https://www.youtube.com/watch?v=LFKZLXVO-Dg)
- [YouTube: Graph Representations - mycodeschool](https://www.youtube.com/watch?v=9C2cpQZVRBA)

**Key Concepts:**
- Graph terminology (vertices, edges, degree)
- Directed vs undirected graphs
- Graph representation methods
- Adjacency list vs adjacency matrix

**Practice Problems (HackerRank):**
- [Roads and Libraries](https://www.hackerrank.com/challenges/torque-and-development)
- [Journey to the Moon](https://www.hackerrank.com/challenges/journey-to-the-moon)

**Mini Project:** **Social Network Analyzer**
Build a simple social network representation where you can add friends and analyze connections.

---

### **Day 19: Graph Traversals (BFS & DFS)**
**Topic:** Breadth-First Search, Depth-First Search, Applications

**Learning Resources:**
- [YouTube: BFS and DFS - HackerRank](https://www.youtube.com/watch?v=zaBhtODEL0w)
- [YouTube: Graph Algorithms - William Fiset](https://www.youtube.com/watch?v=09_LlHjoEiY)

**Key Concepts:**
- BFS implementation and applications
- DFS implementation and applications  
- Connected components
- Cycle detection

**Practice Problems (HackerRank):**
- [Breadth First Search: Shortest Reach](https://www.hackerrank.com/challenges/bfsshortreach)
- [DFS: Connected Cell in a Grid](https://www.hackerrank.com/challenges/connected-cell-in-a-grid)

**CSES Problems:**
- [CSES: Counting Rooms](https://cses.fi/problemset/task/1192)
- [CSES: Labyrinth](https://cses.fi/problemset/task/1193)

**Mini Project:** **Path Finding Visualizer**
Create a grid-based pathfinding visualizer showing BFS vs DFS traversal patterns.

---

### **Day 20: Greedy Algorithms**
**Topic:** Greedy Strategy, Activity Selection, Huffman Coding

**Learning Resources:**
- [HackerRank Greedy](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=greedy)
- [YouTube: Greedy Algorithms - Abdul Bari](https://www.youtube.com/watch?v=ARvQcqJ_-NY)
- [YouTube: Activity Selection Problem - GeeksforGeeks](https://www.youtube.com/watch?v=poWB2UCuozA)

**Key Concepts:**
- Greedy choice property
- Optimal substructure
- Proving greedy correctness
- Common greedy patterns

**Practice Problems (HackerRank):**
- [Minimum Absolute Difference in an Array](https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array)
- [Marc's Cakewalk](https://www.hackerrank.com/challenges/marcs-cakewalk)
- [Grid Challenge](https://www.hackerrank.com/challenges/grid-challenge)

**CSES Problems:**
- [CSES: Coin Piles](https://cses.fi/problemset/task/1754)
- [CSES: Apple Division](https://cses.fi/problemset/task/1623)

**Mini Project:** **Resource Allocation Optimizer**
Build a system that optimally allocates limited resources using greedy algorithms (e.g., meeting room scheduler).

---

### **Day 21: Review & Problem Solving**
**Topic:** Week 3 Consolidation and Advanced Problem Solving

**Activities:**
- Mixed problem solving session
- Algorithm complexity analysis practice
- Implementation of 3-4 algorithms from memory
- Speed coding practice

**Practice Problems (Mixed Review):**
- [Sherlock and Array](https://www.hackerrank.com/challenges/sherlock-and-array)
- [Minimum Time Required](https://www.hackerrank.com/challenges/minimum-time-required)

**Mini Project:** **Algorithm Performance Dashboard**
Create a comprehensive tool that compares time/space complexity of different algorithms with real data.

---

## **Week 4: Dynamic Programming & Advanced Topics**

### **Day 22: Dynamic Programming - Basics**
**Topic:** DP Fundamentals, Memoization, Tabulation

**Learning Resources:**
- [HackerRank Dynamic Programming](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=dynamic-programming)
- [YouTube: Dynamic Programming - CS Dojo](https://www.youtube.com/watch?v=vYquumk4nWw)
- [YouTube: DP Patterns - Back To Back SWE](https://www.youtube.com/watch?v=YBSt1jYwVfU)

**Key Concepts:**
- Overlapping subproblems
- Optimal substructure
- Memoization vs tabulation
- State representation

**Practice Problems (HackerRank):**
- [The Coin Change Problem](https://www.hackerrank.com/challenges/coin-change)
- [Equal](https://www.hackerrank.com/challenges/equal)
- [Sherlock and Cost](https://www.hackerrank.com/challenges/sherlock-and-cost)

**CSES Problems:**
- [CSES: Dice Combinations](https://cses.fi/problemset/task/1633)
- [CSES: Minimizing Coins](https://cses.fi/problemset/task/1634)

**Mini Project:** **Investment Portfolio Optimizer**
Build a tool that uses DP to find optimal investment strategies given constraints and expected returns.

---

### **Day 23: Classic DP Problems**
**Topic:** Knapsack, LIS, LCS, Edit Distance

**Learning Resources:**
- [YouTube: 0/1 Knapsack - Tushar Roy](https://www.youtube.com/watch?v=8LusJS5-AGo)
- [YouTube: Longest Increasing Subsequence - Back To Back SWE](https://www.youtube.com/watch?v=CE2b_-XfVDk)
- [YouTube: Edit Distance DP - Tushar Roy](https://www.youtube.com/watch?v=We3YDTzNXEk)

**Key Concepts:**
- Knapsack variations
- Sequence alignment problems
- String DP patterns
- Space optimization techniques

**Practice Problems (HackerRank):**
- [Unbounded Knapsack](https://www.hackerrank.com/challenges/unbounded-knapsack)
- [Longest Increasing Subsequence](https://www.hackerrank.com/challenges/longest-increasing-subsequence)

**CSES Problems:**
- [CSES: Coin Combinations I](https://cses.fi/problemset/task/1635)
- [CSES: Coin Combinations II](https://cses.fi/problemset/task/1636)
- [CSES: Grid Paths](https://cses.fi/problemset/task/1638)

**Mini Project:** **Text Diff Tool**
Create a tool similar to `git diff` that shows differences between two text files using LCS/Edit Distance.

---

### **Day 24: Advanced Graph Algorithms**
**Topic:** Shortest Paths, Minimum Spanning Trees

**Learning Resources:**
- [YouTube: Dijkstra's Algorithm - William Fiset](https://www.youtube.com/watch?v=pSqmAO-m7Lk)
- [YouTube: Floyd Warshall Algorithm - Abdul Bari](https://www.youtube.com/watch?v=oNI0rf2P9gE)
- [YouTube: Kruskal's MST Algorithm - William Fiset](https://www.youtube.com/watch?v=JZBQLXgSGfs)

**Key Concepts:**
- Single source shortest paths (Dijkstra)
- All pairs shortest paths (Floyd-Warshall)
- Minimum spanning trees (Kruskal, Prim)
- Negative cycle detection

**Practice Problems (HackerRank):**
- [Dijkstra: Shortest Reach 2](https://www.hackerrank.com/challenges/dijkstrashortreach)
- [Prim's (MST): Special Subtree](https://www.hackerrank.com/challenges/primsmstsub)

**CSES Problems:**
- [CSES: Shortest Routes I](https://cses.fi/problemset/task/1671)
- [CSES: Message Route](https://cses.fi/problemset/task/1667)

**Mini Project:** **GPS Route Planner**
Build a simple GPS-like system that finds shortest routes between locations using graph algorithms.

---

### **Day 25: Union-Find & Advanced Data Structures**
**Topic:** Disjoint Set Union, Segment Trees (Basic)

**Learning Resources:**
- [YouTube: Union Find - William Fiset](https://www.youtube.com/watch?v=ibjEGG7ylHk)
- [YouTube: Segment Trees - Tushar Roy](https://www.youtube.com/watch?v=ZBHKZF5w4YU)

**Key Concepts:**
- Union-Find with path compression
- Union by rank optimization
- Range query data structures
- Lazy propagation basics

**Practice Problems (HackerRank):**
- [Components in a graph](https://www.hackerrank.com/challenges/components-in-graph)
- [Merging Communities](https://www.hackerrank.com/challenges/merging-communities)

**CSES Problems:**
- [CSES: Building Roads](https://cses.fi/problemset/task/1666)

**Mini Project:** **Network Connectivity Monitor**
Build a tool that monitors network connectivity and detects when components get disconnected or connected.

---

### **Day 26: Bit Manipulation**
**Topic:** Bitwise Operations, Bit Tricks, Optimization Techniques

**Learning Resources:**
- [YouTube: Bit Manipulation - CS Dojo](https://www.youtube.com/watch?v=NLKQEOgBAnw)
- [YouTube: Bit Manipulation Tricks - Back To Back SWE](https://www.youtube.com/watch?v=g6OxU-hRGtY)
- [HackerRank Bit Manipulation](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=bit-manipulation)

**Key Concepts:**
- Bitwise operators (&, |, ^, ~, <<, >>)
- Common bit manipulation tricks
- Power of 2 checks
- Bit masking techniques
- XOR properties and applications

**Practice Problems (HackerRank):**
- [Lonely Integer](https://www.hackerrank.com/challenges/lonely-integer)
- [Maximizing XOR](https://www.hackerrank.com/challenges/maximizing-xor)
- [Sum vs XOR](https://www.hackerrank.com/challenges/sum-vs-xor)

**CSES Problems:**
- [CSES: Bit Strings](https://cses.fi/problemset/task/1617)
- [CSES: Gray Code](https://cses.fi/problemset/task/2205)

**Mini Project:** **Binary Calculator & Visualizer**
Create a calculator that performs operations in binary with bit-by-bit visualization of operations.

---

### **Day 27: Advanced Problem Solving Patterns**
**Topic:** Sliding Window, Two Pointers, Pattern Recognition

**Learning Resources:**
- [YouTube: Sliding Window Technique - Back To Back SWE](https://www.youtube.com/watch?v=MK-NZ4hN7rs)
- [YouTube: Two Pointers Technique - CS Dojo](https://www.youtube.com/watch?v=jFZmBQ569So)
- [YouTube: Problem Solving Patterns - Colt Steele](https://www.youtube.com/watch?v=M2uO2nMT0Bk)

**Key Concepts:**
- Sliding window (fixed and variable size)
- Two pointers technique
- Fast and slow pointers
- Pattern recognition in problems
- Time and space optimization techniques

**Practice Problems (HackerRank):**
- [Subarray Division](https://www.hackerrank.com/challenges/the-birthday-bar)
- [Sales by Match](https://www.hackerrank.com/challenges/sock-merchant)

**CSES Problems:**
- [CSES: Sum of Three Values](https://cses.fi/problemset/task/1641)
- [CSES: Subarray Sums I](https://cses.fi/problemset/task/1660)
- [CSES: Subarray Sums II](https://cses.fi/problemset/task/1661)

**Mini Project:** **Stock Trading Analyzer**
Build a tool that analyzes stock price data using sliding window techniques to find optimal buy/sell periods.

---

### **Day 28: System Design Basics & Data Structure Applications**
**Topic:** Scalability Concepts, Cache Design, Real-world Applications

**Learning Resources:**
- [YouTube: System Design Primer - Gaurav Sen](https://www.youtube.com/watch?v=quLrc3PbuIw)
- [YouTube: LRU Cache Design - Back To Back SWE](https://www.youtube.com/watch?v=S6IfqDXWa10)
- [YouTube: Design Patterns in Data Structures](https://www.youtube.com/watch?v=tv-_1er1mWI)

**Key Concepts:**
- LRU Cache implementation
- Database indexing concepts
- Load balancing basics
- Caching strategies
- Data structure choice for specific problems

**Practice Problems (HackerRank):**
- [Count Triplets](https://www.hackerrank.com/challenges/count-triplets-1)
- [Frequency Queries](https://www.hackerrank.com/challenges/frequency-queries)

**Mini Project:** **Multi-level Cache System**
Implement a multi-level caching system with LRU, LFU policies and performance metrics.

---

### **Day 29: Mock Interview & Optimization**
**Topic:** Interview Simulation, Code Optimization, Edge Cases

**Activities:**
- 2-hour mock interview simulation
- Code review and optimization of previous projects
- Edge case identification and handling
- Time and space complexity analysis practice
- Communication skills for technical interviews

**Practice Problems (High Difficulty):**
- [Roads and Libraries](https://www.hackerrank.com/challenges/torque-and-development)
- [Matrix Layer Rotation](https://www.hackerrank.com/challenges/matrix-rotation-algo)

**CSES Problems:**
- [CSES: Two Sets](https://cses.fi/problemset/task/1092)
- [CSES: Palindrome Reorder](https://cses.fi/problemset/task/1755)

**Mini Project:** **Interview Problem Generator**
Create a system that generates random interview problems with solutions and hints.

---

### **Day 30: Portfolio Review & Next Steps**
**Topic:** Portfolio Compilation, Performance Analysis, Future Learning Path

**Activities:**
- Compile all 30 mini-projects into a portfolio
- Performance benchmarking of implementations
- Code documentation and commenting
- GitHub repository organization
- Create a personal DSA cheat sheet

**Final Challenge Problems:**
- [New Year Chaos](https://www.hackerrank.com/challenges/new-year-chaos)
- [Array Manipulation](https://www.hackerrank.com/challenges/crush)

**Final Project:** **Algorithm Learning Platform**
Build a comprehensive web application that combines multiple mini-projects into an educational platform with:
- Interactive algorithm visualizations
- Performance comparisons
- Problem practice interface
- Progress tracking

---

## **Additional Resources & Tips**

### **Weekly Review Schedule:**
- **Week 1:** Arrays, Strings, Lists, Stacks, Queues, Hash Tables
- **Week 2:** Trees, Recursion, Heaps, Tries
- **Week 3:** Sorting, Searching, Graphs, Greedy Algorithms
- **Week 4:** Dynamic Programming, Advanced Graphs, Specialized Topics

### **Python-Specific Tips:**
- Use `collections` module (deque, defaultdict, Counter)
- Leverage list comprehensions and generator expressions
- Understand Python's built-in functions (sorted, min, max, any, all)
- Practice with `heapq` for priority queues
- Use `bisect` module for binary search operations

### **Interview Preparation Checklist:**
- [ ] Can implement all basic data structures from scratch
- [ ] Comfortable with time/space complexity analysis
- [ ] Can explain algorithm choices and trade-offs
- [ ] Practice coding on whiteboard or shared screens
- [ ] Can handle follow-up questions and optimizations
- [ ] Familiar with Python-specific optimizations

### **Recommended Practice Platforms:**
- **Primary:** [HackerRank](https://www.hackerrank.com/)
- **Competitive Programming:** [CSES Problem Set](https://cses.fi/problemset/)
- **Interview Focus:** [LeetCode](https://leetcode.com/)
- **System Design:** [Pramp](https://www.pramp.com/)

### **Time Management (2-3 hours daily):**
- **Theory & Learning:** 45-60 minutes
- **Practice Problems:** 60-90 minutes  
- **Mini Project:** 30-45 minutes
- **Review & Notes:** 15-30 minutes

### **Success Metrics:**
- Complete 80%+ of assigned problems
- Finish all 30 mini-projects
- Can implement major algorithms without references
- Comfortable with live coding sessions
- Ready for junior software engineer interviews

---

## **Final Notes**

This roadmap is designed to take you from DSA basics to interview readiness in 30 days. The key to success is **consistent daily practice** and **hands-on implementation**. Each mini-project reinforces theoretical concepts with practical applications.

Remember to:
- **Code daily** - even 30 minutes helps maintain momentum
- **Focus on understanding** over memorization
- **Practice explaining** your solutions out loud
- **Review and optimize** your code regularly
- **Don't skip the projects** - they're crucial for retention

Good luck with your DSA journey and upcoming interviews! 🚀