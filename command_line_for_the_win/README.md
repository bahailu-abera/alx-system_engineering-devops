# [CMD CHALLENGE] (https://cmdchallenge.com/)

It is a pretty cool game challenging on Bash skills. Everything is done via the
command line and the questions are becoming increasingly complicated.
It’s a good training to improve command line skills!

The tasks and the solution are the following below
### 0-first_9_task.png
task-1.
Your first challenge is to print "hello world" on the terminal in a single command.

*Hint: There are many ways to print text on the command line, one way is with the 'echo' command. Try it below and good luck!

      solution: echo "hello world"*

task-2.
Print the current working directory.
     <ul> solution: pwd</ul>

task-3.
List names of all the files in the current directory, one file per line.
     <ul>solution: ls</ul>

task-4.
There is a file named access.log in the current directory. Print the contents.
      <ul>solution: cat access.log</ul>

task-5.
Print the last 5 lines of "access.log".
      <ul>solution: tail -n 5 acces.log</ul>
task-6.
Create an empty file named take-the-command-challenge in the current working directory.
       <ul>solution: touch take-the-command-challenge</ul?

task-7.
Create a directory named tmp/files in the current working directory
Hint: The directory "tmp/" doesn't exist, with one command you need to create both "tmp/" and "tmp/files"*
      <ul>solution: mkdir -p tmp/files

task-8.
Copy the file named take-the-command-challenge to the directory tmp/files.
     <ul>solution: cp take-the-command-challenge tmp/files</ul>

task-9.
Move the file named take-the-command-challenge to the directory tmp/files.
     <ul>solution: mv take-the-command-challenge tmp/files
