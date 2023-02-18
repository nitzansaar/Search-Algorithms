
### CS 462 Assignment 2: Search

### due: Monday, 2/27, start of class.

#### 100 points.

Note: please make sure that your name is someplace in your assignment! This is especially true if it's not obvious from your GitHub handle.

To turn in: please submit everything to your github repo. For the written portion of the assignment, please add a document to your repository, as PDF, containing the answers to these questions.
Also, please add a file to your repo called submission.py - this should call each of your tests and run your code.

In this assignment, you'll answer a set of written questions about search, extend some existing 
code to implement classic search algorithms, and use an existing toolkit [(OR-Tools)](https://developers.google.com/optimization) to solve problems in a 
simplified Mars rover environment.

I've also included some other sample environments, specifically the Vacuum and Romania environments, to provide examples for you.

Question 1 (20 points): For each of the following algorithms, please indicate its time and space requirements, and whether it is complete and optimal, it's 

| Algorithm  | Time Complexity  | Space Complexity  | Complete?  | Optimal?  |
|---|---|---|---|---|
| BFS  |   |   |   |   |
| UCS  |   |   |   |   |
| DFS   |   |   |   |   |
| DLS  |   |   |   |   |
| IDS |    |   |   |   |
|A*  |    |    |   |   |




Question 2: Our Mars Rover needs to collect some soil samples. It has three hoppers to
hold these samples. Unfortunately, during the landing, the markings on the hoppers were burned off,
so our agent only knows how much each hopper holds. (careful observers may note the 
resemblance to the Water Jug problem.)

Luckily, our agent has access to some search algorithms that it can use. Using VacuumState as an example, you will need to complete the implementation of the HopperState 
class so that our rover can solve the problem.

a) (5 points) To begin, we need to implement the __eq__, __hash__, and __lt__ methods in the HopperState class in order for the closed list and 
priority queue to function correctly. (You should use cost as the way to compare states. Implement unit tests in a file called
test_HopperState.py that allow you to determine that these methods are working correctly.

b) (10 points) Next, implement successors. For any state, our robot has the following actions:
- It can fill any of the three hoppers. This will result in them being completely full.
- It can dump out any of the three hoppers. This will result in that hopper being empty.
- It can pour soil from hopper A to hopper B. This will have one of two outcomes:
  1. Hopper A is empty, and hopper B contains all the soil from both hoppers.
  2. Hopper B is full, and some leftover soil remains in hopper A.

successors should return a list of successor states. You do not need to generate states that result in no change.
(for example, dumping out an empty bucket.)
Implement a unit test in test_HopperState that allows you to confirm that successor is working correctly.
Note: good coding practices are encouraged here. If you find yourself creating complex loops or nested if/else's, refactor.


c) (5 points) Now let's try it out on the given algorithms. I've provided BFS and DFS implementations for you. 
Run this problem with the following three goals using both BFS and DFS, assuming the hoppers start empty. (Don't do the hard one until you're sure the closed list is working correctly.)
1. Easy: [5 0 0]
2. Medium: [4 0 0]
3. Hard: [4 4 0]

Adapt the code to print out the number of states generated at the end.

d) (10 points) Last, note that DFS has a limit parameter that is not used. Extend DFS to only add new nodes to the search queue if they have cost < limit. 
This will implement DLS for us. Then, write a method called IterativeDeepeningSearch - this should just be a loop that 
calls DLS with increasing limits until the solution is found.

e) (5 points) Please include a table that shows how many states were generated for each of the problems (Easy, Medium, Hard) for BFS, DFS, DLS, and IDS.


Question 3: For this problem, we will need for our rover to find its way from the sample site back to the charger.
Fortunately, we have a map that we can use to find our way. There's a picture of it in the marsmap.docx file; 
the red cells are areas we cannot travel in.

This data is also captured in the MarsMap file.

You will need to:

a) (5 points) Complete the read_mars_graph() method so that you can create a graph. 
I've provided a Graph class for you; if you want to modify it, feel free.
You may want to look at RomaniaGraph to get some ideas.

b) (15 points) In SearchAlgorithms.py, complete the a_star function. 
You will need to implement a straight-line distance heuristic. 
This should compute SLD(p1, p2) = sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2))

SLD should be a separate function that is provided to a_star, *NOT* something encoded within the
algorithm. You should be able to pass in a different heuristic function, such as h1, which always returns 0,
without changing your code.

c) (5 points) Run both A* and uniform cost search (i.e. using h1: h=0 for all states) on the MarsMap and count the number of states generated.
Add this to your results.

Question 4.

For this question, you'll be using the [(OR-Tools)](https://developers.google.com/optimization) toolkit to help out our Mars rover.
I've provided some sample code for you to use as a starting point, as well as code to solve
the Bay Area map coloring problem.

a. (15 points) Our rover needs to set up nine wireless antennae so that its sensors can collect data and send it back. 
Antennae that are close to each other need to operate on different frequencies so that they don't interfere with each other.

Our rover has three possible frequencies (f1, f2 and f3) that it can assign to an antenna.

It knows that:
- Antenna 1 is adjacent to 2,3 and 4.
- Antenna 2 is adjacent to 1, 3, 5, and 6
- Antenna 3 is adjacent to 1, 2, 6, and 9
- Antenna 4 is adjacent to 1, 2, and 5.
- Antenna 5 is adjacent to 2 and 4
- Antenna 6 is adjacent to 2, 7 and 8
- Antenna 7 is adjacent to 6 and 8
- Antenna 8 is adjacent to 7 and 9
- Antenna 9 is adjacent to 3 and 8

(observant readers will note that this is a variant of the map coloring problem.)

Using the map coloring code as an example, use OR-tools to find an assignment of frequencies to antennae that maintains the constraint that
no adjacent antennae share a frequency.

b. (5 points) Rover scheduling. For this problem, we'll be using OR-tools to solve a rover scheduling problem. You will want to use the nurse scheduling problem as an example.

Let's suppose that we have five rovers, and we need to create a schedule for when they operate. We have the following setup:
- There are seven days in the week.
- There are three time blocks in each day. (morning, noon, night)
- For each time block, we want exactly one rover to be scheduled.
- A rover cannot run more than one shift in a day.
- A rover cannot do a night shift followed by a morning shift.
- All the rovers must have at least three slots.

Using the nurse scheduler as an example, use OR-tools to find a schedule for our rovers.

Question 5: (grad students only).

A problem that computer scientists and biologists have been working on for almost 50 years is the (protein folding)[https://www.youtube.com/watch?v=KpedmJdrTpY] problem.

It's a huge combinatorial search problem that was traditionally tackled using the search techniques we've 
been studying. 

Recently, researchers at DeepMind have developed a new approach to this problem, called (AlphaFold)[https://www.deepmind.com/research/highlighted-research/alphafold], which 
employs machine learning to attack the problem differently. In a nutshell, a neural network is used to learn a 
highly accurate evaluation function. This greatly reduces the size of the space that needs to be searched, allowing 
AlphaFold to identify almost any protein structure. 

Please take a look at the site linked above, watch the videos and read their descriptions, and prepare a short (2-3 paragraph)
response that answers the following questions:
- Why is protein folding so hard?
- What is CASP?
- How does AlphaFold enable scientific discovery? What's an example of a problem it's
been used to solve?