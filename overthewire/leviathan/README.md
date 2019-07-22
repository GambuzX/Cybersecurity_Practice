0 -> 1
Found the hidden .backup folder with a 'bookmarks.html' file inside.
Used grep to search for 'password' and found it.


1 -> 2
Using gdb understood that the password was 'sex'. Could also have just skipped the line in the debugger.
Running the executable and inserting the password we get a shell, in which our uid is leviathan2.
After that you can just use 'cat /etc/leviathan_pass/leviathan2' to get 'ougahZi8Ta'.


2 -> 3
Analysing the executable with ltrace, we understand that there are 2 important function calls: access and cat.
Access is being called with the full path name. However, cat is not. If the input file has spaces, it will be interpreted as 2 separate files.
We can exploit this by creating a symbolic link to /etc/leviathan_pass/leviathan3 called 'pass' (for example) and creating a file 'test pass'.
When we run the executable in the 'test pass' file, it will check access to 'test pass', which is granted, and then cat files 'test' and 'pass'.


3 -> 4
Executing the file with ltrace we see that the password we enter is compared to 'snlprintf'. By executing the file again and entering this as a password we get a shell.
After that just use 'cat /etc/leviathan_pass/leviathan4' to get 'vuH0coox6m'.


4 -> 5
There is an hidden folder .thrash with a bin executable. Running it returns binary values which I assumed to be the password.
We can just assemble the password from the binary, for which I wrote a python script.


5 -> 6
The given program opens '/tmp/file.log' and reads it char by char, displaying its content on screen.
We can exploit this by creating a symbolic link to '/etc/leviathan_pass/leviathan6' in /tmp called 'file.log'.
The program reads the password and displays it for us.


6 -> 7
The given program expects a 4 digit code. On correct input it spawns a shell which can be used to cat the password.
I wrote a python script to bruteforce all codes.