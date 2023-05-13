# Lab 0

## Due: May 14, 2023

This lab is not worth any marks but it will let you set up your repository for your labs and get familiar with some of the tools that we will use. This lab will do the following:

* create the repository for your labs for the semester.  This step is mandatory even if you do nothing else in the lab as it sets you up for other labs.
* get familiar with the various tools we will be using
* learn how to make a lab submission.

It is a good idea to do this lab to learn how to use the tools as it may be different than your previous courses.

## Create a private repository (repo for short) for the course.


Video instructions: https://web.microsoftstream.com/video/fbe5aced-5196-435f-ab0c-ddd0cb20dda0


1. If you do not have a github account, please create one first:
    * [get your github id](https://github.com)
    * You will use the same github account throughout this course and beyond.  Pick a userid that you can be ok with professionally.  
    * **Do not use private info like your student number in your github id.  We do not need it!**

2. Once you have your github id, go to https://classroom.github.com/a/3230mjgZ to create your private repository for the labs in this course course.  **FOR YOUR TEAM NAME USE YOUR SENECA USERNAME (the username part of your seneca email).  This is needed to find you in the grading roster.**.  

![](https://user-images.githubusercontent.com/1699186/166190371-b45631c1-4ad4-4933-9544-8842ff471956.jpg)

3. Go to https://github.com/seneca-dsa456
  * You will now see two repos, one for the course (dsa456-s23) and one named labs-***your name***.  The repo named after you, is your private repo.  This repository can not be seen by other students.  It is what you will use for this lab.  Each lab/assignment you do will have a similar repo.

NOTE: We will only look at work in the repos created through the method described above.  If you create your own repository under your account, we will not grade that work.  If you create public repository to host your work that will be a violation of academic policy (ie cheating) so don't do that.

## Checklists

Your lab and assignments will come with a check list that you can use to keep track of what it is that you need to do for the assessment.  Note that not everything on checklist is mandatory for completion, but it is a good way to know if you have finished everything.  To use this checklist go to the Issues tab in your repository, and create a new issue.  From the template choose the one labeled Lab 0 Tasks. 


### Task:

* Create a task list for this lab
* Check off task list as you complete the lab


## How to use Codespaces

* [Video Instructions and Explanation](https://web.microsoftstream.com/video/c3f41f80-94d1-4c9f-9e58-604de47bb2bb)

In this course, we will be turning on code spaces for your labs and assignments.  This means that you will be able to write and compile your program in the browser.  It also means that your computer doesn't have to be very good as the web browser is just a terminal into your code.  You will also be able to run this code space on devices like chromebooks making the code pretty much accessible anywhere.  Note, it is still recommended that you set up a local python dev environment.

### Task:

* Spin up a Codespaces for your lab.
* Write the Hello World program in python int the helloworld.py file.  Feel free to make it more interesting
* Run it in code space
* Once you are happy with result, add, commit and push the code into your repo from code space.  Note that code in your codespace is not in your repo until it is pushed and we do not have access to it.  Make sure you do the push!
* Check your file to see that it is correctly updated.
* It may be useful to do things like walk away from the file for a day in a changed state and see what happens.. do you need to spin up new code space? Are changes present when you go back?  You want to be familiar with the retention rules... when in doubt, add, commit and push.

## How to submit a lab and verify that it passes testing

[Video instructions](https://web.microsoftstream.com/video/499348a2-16e8-4a17-98fd-3f68c7d5c165)

Your labs are set up to test your programs every time you update the source files in your lab repository.  Please follow instructions in your lab about which files to modify.  You can update the files as many times as you like until you are happy with the results.

Everytime you push a file into your repository, it will trigger a github action.  Typically this action will get the files from your repo, an external tester and other related files then compile and run the program.  Looking at the action tab, you will see a process spin up and eventually a status of pass or fail (green check or red X).  If it passes, it means the program has met a minimum standard of compiling and passing the testing.  If it fails it means that the program either didn't compile or didn't pass testing.  If it is a yellow dot it means it is still running.  You can look at the details of any run by expanding the associated action run.  Just click and expand.  It will show you where it failed.

Always check the Action tab to ensure things are working and that you passed testing on the correct lab.

**Do Not touch anything in the .github folder**

The scripts used for testing are in the .github folder.  Changing them is not allowed. If there is a bug please inform your prof so that they can be fixed but you cannot alter the testing scripts yourself.  If you do it is considered an attempt to cheat the test and an academic integrity case will be filed.  This applies throughout the course.

### Task:

Become familiar with submitting a lab and learn how to know if it passes testing or not.  You can write the code locally on your computer or in code space, the choice is yours.


* In the file lab0.py there is a declaration for a function named sum(num1,num2) which will return the sum of the two numbers passed into the function
* Write the program with a mistake in it (for example: return num_1 * num_2).
* You can test it locally by using the command: python test_lab0.py.  At this point, the test should not pass.
* add, commit and push the file with error in your repo.
* Look at the action tab.  Wait for action to complete (should have a red X)
* Fix the function by writing the function correctly.
* Run the test locally to verify that it works
* add, commit and push the file into your repo
* Look at the action tab again.  Wait for action to complete (should see a green check)

## LaTex

In this course there will be times when you will need to write mathematical expressions.  It is fine if you want to keep the math ugly.  For example, here is the ugly math version of the quadratic formula:

```
x = [ -b +/- sqrt(b^2-4ac) ]/2a
```

However, some of you may wish to make it look like an actual mathematical expression.  To do this, you can make use of LaTex.  LaTex is widely used for producing beautiful math.  It is also used in academic circles for writing papers.  Last year, github added support of LaTex based mathematical expressions on their .md files.  To create a mathematical expression inline, delimit the expression with ```$```.  To put it by itself, delimit the expression with ```$$```.  For example:

Here is a sentence with the  quadratic formula $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$ embbed inline.

The above was created with this in the markdown file:

```
Here is a sentence with the  quadratic formula $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$ embbed inline.
```

This next bit, where the formula sits by itself:

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

was created using:

```
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$
```

### Task:

Write the formula for calculating the length of the hypothenus (c) given right angle triangle with side lengths a and b in LaTex.   

That is write the following formulas in latex: 

* hypotenus of a right angle triangle: c = sqrt(a^2 + b^2)
 <img width="474" alt="Screen Shot 2022-09-06 at 7 39 56 AM" src="https://user-images.githubusercontent.com/1699186/188627199-3f507415-d792-4b7c-9b32-4aa6ef4ae134.png">

* geometric series: sum from i=0 to n (ar^i)
 <img width="362" alt="Screen Shot 2022-09-06 at 7 40 00 AM" src="https://user-images.githubusercontent.com/1699186/188627355-28fd5df7-dba8-47c9-af03-fcd5418dcaea.png">

* arithmetic series closed form: sum from i = 1 to n (i) = 1 + 2 + 3 + 4...n=(n)(n+1)/2
<img width="925" alt="Screen Shot 2022-09-06 at 7 40 12 AM" src="https://user-images.githubusercontent.com/1699186/188627875-2f25a243-a06c-46a4-b7e5-aae2f842b9d7.png">


#### References

* [Video about LaTex](https://www.youtube.com/watch?v=NXW4cbHBthY)
* [Quick reference for LaTex](http://users.dickinson.edu/~richesod/latex/latexcheatsheet.pdf)
* and for those who really hate LaTex... word's equation editor can produce LaTex output of a formula entered into the equation editor.


## Graphs

From time to time you may be asked to produce a graph as part of an assessment.  This graph will need to be correctly placed into your .md so that it is part of the text. 

### Task:

Create a simple graph showing a fake survey results on favorite icecream flavours using any spreadsheet program you wish

If you are using excel to create the graph:
	- save the graph as an image
	- in github, click into the lab0.md file where you want graphic to go
	- click on pencil icon at top
	- position cursor to place where you want image to go
	- drag and drop image into browser window that has the file opened for editing
	- give it a few seconds and you should see some an image link text ```![](https://somegithubusercontenturl)```
	- move that around if it isn't in the correct place

If you are using googlesheets
	- get a shared (non-interactive) link.
	- in your lab0.md file add an image link using the url you got from the graph created by google sheet
	- alternatively get image and follow the same instructions as that for excel.

## Discussion Board

DSA456 has a discussion board for the course.  Every section will use the same discussion board.  To access the discussion board, click on the discussion tab of the dsa456 course organization.

### Task:

Add a post to the Welcome to dsa456 thread.  In your post introduce yourself for and tell us something about yourself.  Write a comment or two about other posts in the thread.


## Reflection:

### Task: 
Answer the following questions about your experience with the lab and put them into your lab0.md file

1. What aspect of the lab did you find to be the hardest?

2. What do you think about CodeSpaces? What did you like/not like about Codespaces?

