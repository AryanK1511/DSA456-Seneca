# Assignment 1

## Due: June 18

### This assignment is worth 10% of your final grade

### Late penalties

* up to 1 week late - 10%
* 10% per day thereafter to a maximum of 50%

### Assignment Completion

In order to for this assignment to be considered completed you must submit:

* parts B, C and D that pass testing on github (Green check for each part in action tab)


Note: Assignment completion is the minimum requirement for your assignment to be considered complete.  It does not mean you will receive full marks.

Assignment completion is mandatory to pass dsa456


## Assignment Objectives

In this assignment we will:

*  draw diagrams of your implementation in order to gain a better insight as to how this is accomplished.
*  implement a linked list that we can use to create a disjoint set
*  implement a data structure
*  write a more complicated recursive function

NOTE: **as this assignment is about implementing data structures, you are not allowed to make use of any python libraries or use built-in python data structures and functions unless specified.  If you are not sure, please ask your professor.  Any use a built-in libraries or functions without approval will result in having to redo the assignment with a grade penalty of -50%**

## Group Creation

In this assignment you can choose to work in a group of two or three.  You have until June 2 to create a team of your choosing.  After this date, students not in a team will be teamed up together by their profs.  **Working alone is not an option.**  In general we will try not to make adjustments to teams that you put together but there may be situations where we have no other ways of placing every student into a team without making changes to existing teams.  Our preference will always be to add someone to a team rather than breaking a team up and thus a three person team is very unlikely to be altered where as a two person team may end up with an additional person (but we will try to avoid this).  

**Make sure you are clear how many people you are working with and who they are before using the appropriate link.  You will not be able to modify this once you have created the teams.  When you create your team, your team name will need to use every member's seneca user name**

* [Repo Creation for teams of 2](repo-creation-g2.md)
* [Repo Creation for teams of 3](repo-creation-g3.md)

Your team will last for only 1 assignment.  If you decide that you were not able to work together after assignment 1, you can find new partners for the other assignments.  

## Work Divsion

* Every member of the team must contribute to the coding portions (parts B, C and D) of the assignment.  As there are 3 coding components, we expect each member to be the lead author in one of the 3 sections.  It doesn't mean that other team members can't help ... but the lead should be the main contributer to that part of the assignment.
* Every member is expected to push their own code.
  * **it is NOT ok to use email or have just one person commit all the code. git/github is a professional tool that employers expect our graduates to know how to use, so learn it now.  If you aren't sure, check out the git tutorial listed in the resources section in course repo.**
* If we find that a member of the team did not author any code (according to commit records), that team member may be removed from the team and be required to redo the assignment with a grade deduction and late penalties.

## Part A: Drawings (5 marks)


In your repository you will find a pdf file containing some diagrams.

Read through the specs (parts B and C) first to get an idea of the functionalities asked for in Part A.
Then, modify each of the lists in the drawings to show what the result of the operation (mentioned in each of the drawings) is:

* Be clear about what is changing and how.  
* The diagrams do not need to be neat.. but they need to be understandable so clearly scribbling over a link that no longer exsists is perfectly acceptable.  The idea is to think through what you need to change to achieve your goals.
* You can modify the diagrams electronically using something like paint or other diagramming software 
* Alternatively you can print out the pdf and then hand draw on the printed diagrams. If you choose this method you must:
     * take a picture of each drawing and put them into word document in same order as original
     * convert that document to a pdf (print to a pdf) and name the pdf file the same as the original file.
     * Upload the file to your github repo.
     * A bunch of individual images will not be graded, it needs to be in one pdf file.


## Part B: Implementing our SetList (15 marks)

The class declarations have been created in the a1_partb.py starter file.  You are responsible to write all the listed functions.

You are allowed to add data members to both Node and SetList.

### Node

The Node class is declared within SetList.  It stores:
* a piece of data
* a reference to the next Node in the SetList (None if Node is last node)
* a reference to the previous Node in the SetList (None if Node is first node)
* a reference to the SetList.
    
When a Node is initialized, it is passed a data value and a reference to the SetList the Node belongs to.  Optionally it is also passed a reference to the next node and a reference to the previous node (in that order).  If the data values are not passed in, they are defaulted to None.

The Node function has the following member functions:

***

```python
def get_data(self)
```
function returns data stored in node

***

```python
def get_next(self)
```
function returns reference to next node in SetList

***

```python
def get_previous(self)
```
function returns reference to previous node in SetList
***

```python
def get_set(self)
```
function returns reference to the SetList



### SetList

A SetList is a doubly linked list that can be used to represent a single set of a disjoint set.  With a SetList, each node contains data and is linked to other nodes in the list.  The difference with a regular doubly linked list is that each node also contains a link to the SetList object.  The first node within the SetList contains the set's **representative**.

The following is a diagram of the set: {"cat", "fish", "dog"}.  Note that values within a set do not have any particular ordering and the exact ordering does not matter in your implementation.  This means that any of the 3 can be the representative..its simply a matter of which one is at the front of the list
![SetList](https://user-images.githubusercontent.com/1699186/214759162-b11c10bd-f188-4e7b-8275-1681d6ad79b1.png)

When a SetList is initialized, the SetList is empty.

The SetList has the following member functions

***
```python
def get_front(self)
```
This function returns a reference to the first node in the list

***

```python
def get_back(self)
```
This function returns a reference to the last node in the list

***

```python
def make_set(self, data)
```
This function adds the first value to the SetList object if the list is empty and returns a reference to newly created Node.  If the list is not empty, function does nothing and returns None. 

***

```python
def union_set(self, other_set)
```
This function is passed a SetList and performs a union with the current object.  This means that the elements of other_set are transfered to current object and other_set becomes empty in the process.  Function returns number of elements transferred.  Note, this process does not create or destroy any of the nodes.

***


```python
def find_data(self, data)
```
This function is passed a data value, the function returns the a reference to the Node containing data.  If data does not exist, function returns None

***

```python
def representative_node(self)
```

This function returns a reference to the node that holds the representative of the SetList.  If SetList is empty, function returns None

```python
def representative(self)
```

This function returns the data of the representative node of the SetList.  If SetList is empty, function returns None


***

```python
def __len__(self)
```
This function returns the number of items within the SetList.


***


## Part C - DisjointSet Class (15 marks)

Implementation of this class is done in a1_partc.py

A DisjointSet class represents a disjoint set which is a set of sets where every element can only belong to exactly one set.

When a DisjointSet class is instantiated it is passed nothing and contains no sets.  It creates an empty [Python dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) which will be used to store the elements of the DisjointSet.  You are welcome to add other data members to help you implement this data structures if you wish but the restriction on other python data structures remain.

The DisjointSet has the following member functions:

***

```python
def make_set(self,element)
```
If element already exists within the Disjoint set, the function does nothing and returns false.

If element does not exist in the DisjointSet, this function will add it to the DisjointSet by:
* creating a new SetList object containing only one node, with the element as only value in the SetList
* adding a new dictionary entry where element is the key and a reference to the node containing element as the value
* return true

Suppose we ran the following code:
```python
    ds = DisjointSet()
    ds.make_set("cat")
    ds.make_set("dog")
    ds.make_set("fish")
```
The following is what we would create:
![DisjointSet](https://user-images.githubusercontent.com/1699186/214759216-899b4334-bf04-4cea-8cdb-78f5f4a7e76f.png)

***

```python
def find_set(self, element)
```
Function returns the representative of the set containining element.

***

```python
def get_num_sets(self)
```
This function returns the number of sets in the DisjointSet.  Note that this is not the same as the number of elements.  You can start with 2 elements in unique sets and join them using the union_set() function.

***

```python
def __len__(self)
```
This function returns the number of elements in the DisjointSet.

***

```python
def get_set_size(self, element):
```
This function returns the size of the set containing element.  If element does not exist within the disjoint set, function returns 0

***

```python
def union_set(self, element1, element2)
```
Function performs a union of the two sets containing element1 and element2 respectively.  If the two elements are already in the same set or if either of the elements do not exist, function does nothing and returns false.  otherwise perform a union on the two sets, creating one set and return true

Example, suppose we ran the following code:
```python
    ds = DisjointSet()
    ds.make_set("cat")
    ds.make_set("dog")
    ds.make_set("fish")
    ds.union_set("cat","dog")
```

Our DisjointSet would look like:

![union_set](https://user-images.githubusercontent.com/1699186/216095712-b65af297-9c27-4a70-9e39-e806eff17a74.png)

***


## Part D - Maze Runner Function - Recursive (5 Marks):

Implementation of this function is done in a1_partd.py

We describe a maze as having row x col cells.  For example if row was 3, and col was 4, then we would have a grid of cells as follows.  We describe a wall by the two cell numbers the wall separates.  If every single wall existed, there would be (row-1)(col) + (col-1)(row) walls.  

```
  0 |  1 |  2 |  3 
-------------------  
  4 |  5 |  6 |  7
--------------------
  8 |  9 | 10 | 11
```


A Maze class (which you do not need to implement) describes a maze as mentioned above.  This class is defined in maze.py.  It has methods that you can use to travel through the maze (i.e. figure out where you are, find a neighbour cell etc.)

Write a **recursive** maze runner function:

```python
def find_path(maze, from_cell, to_cell);
```

The find_path function will find a path from cell number ***from_cell*** to cell number ***to_cell*** and will return it as a list containing all the cell numbers along the path, from the from_cell to the to_cell.

You are allowed to use this function as a wrapper to a recursive function that does the work, allowing for other arguments to your function prototype or additional processing.  However, the function that does the work to find the path must be recursive.

For example, suppose the from_cell was 0 and the to_cell was 3, using the maze below:

```
  0 |  1    2    3 
         ----------  
  4    5 |  6    7
----          
  8    9   10 | 11
```

The find_path function would return this path: [0, 4, 5, 1, 2, 3].
**_Note that in case there exists a path to the to_cell, that path is unique._**

### Online visualizer

To help you debug your program, when you run the tester, the tester will create a "path" file based on the path your find_path function generates (its return values.)  You can see what is happening by going to this site:

[Online Visualizer](https://seneca-dsa456.github.io/dsa456-s23/)

* Use the radio buttons to select the test in question (see your error message.)
* Then, load the corresponding testpath file.  


## Part E - Reflection: (5 marks)

This component is to be individually written and graded.  Please clearly put your name in the title of your reflection.

In your reflection include the following:

1. Please detail what exactly **you** did for the assignment.
2. What was one thing **you** learned when doing this assignment?
3. What was its most challenging aspect and what did **you** do to overcome this challenge?

This answer is not about what your team did as a whole.  It is about what each team member individually contributed.

## Submitting your assignment

* Push your diagram into your repo (remember you can always use the file upload button).  Make the commit message clear that it is the version you want us to mark.

* Push your code into your repo and ensure it passes all the testings by checking the actions tab.

* Push your updated a1.md file into your repo with your reflections, be careful not to overwrite your other teammates' writings for the reflection part.





## Rubrics:

This sections describes how your assignment will be graded:

### Drawing Rubric:

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Drawing completion | No diagrams present | Less than half the diagrams are completed without flaws | At least Half the diagrams are completed without flaws, but a signficant number are missing or has flaws  | Missing a diagram or one of the diagrams have flaws | All diagrams present and correctly drawn with clear changes to the list|


### Coding Rubric:

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW. "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns true if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling, same data member styling, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count at a minimum as two errors as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2)  These count as a major instance. Writing unnecessary code will also be counted as inefficient even if runtime is same, these are considered minor. 2 level deduction for major instance, 1 level for minor instance| some combination of multiple major/minor incidences of efficiency | 3 minor instance of inefficiency or 1 major and 1 minor instance | 2 instance of inefficiency or 1 major instance of inefficiency| 1 minor instance of inefficiency | Function is as efficient as possible |


### Reflection Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Reflection | No reflection written | Reflection has no specifics with generic statements that can apply to anything | Reflection lacks depth, only a brief description without any details | Reflection shows some depth with some descriptions.  It does not go far beyond the basic requirements | A clearly written reflection with clear thought that shows depth|