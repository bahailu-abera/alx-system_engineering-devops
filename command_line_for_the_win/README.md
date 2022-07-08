# CMD CHALLENGE [link](https://cmdchallenge.com/)

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
     solution: pwd

task-3.
List names of all the files in the current directory, one file per line.
     solution: ls

task-4.
There is a file named access.log in the current directory. Print the contents.
      solution: cat access.log

task-5.
Print the last 5 lines of "access.log".
      solution: tail -n 5 acces.log
task-6.
Create an empty file named take-the-command-challenge in the current working directory.
       solution: touch take-the-command-challenge

task-7.
Create a directory named tmp/files in the current working directory
Hint: The directory "tmp/" doesn't exist, with one command you need to create both "tmp/" and "tmp/files"*
      solution: mkdir -p tmp/files

task-8.
Copy the file named take-the-command-challenge to the directory tmp/files.
     solution: cp take-the-command-challenge tmp/files

task-9.
Move the file named take-the-command-challenge to the directory tmp/files.
     solution: mv take-the-command-challenge tmp/files

### 1-next_9_tasks.png
task-10.
A symbolic link is a type of file that is a reference to another file.

Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.
       solution: ln -s tmp/files/take-the-command-challenge take-the-command-challenge

task-11.
Delete all of the files in this challenge directory including all subdirectories and their contents.
*Hint: There are files and directories that start with a dot ".", "rm -rf *" won't work here!*
       solution: rm -rf .[!.]* ..?* *

task-12.
There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
      solution: find . -name "*.doc" -type f -delete

task-13.
There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".
      solution: grep GET access.log

task-14.
Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".
      solution: grep -rl * -e 500

task-15.
Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.
      solution: find . -name "access.log*" -type f

task-16.
Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".

*Note that there are no files named access.log in the current directory, you will need to search recursively.*
      solution: grep -h 500 $(echo $(find . -name "access.log*" -type f))

task-17.
