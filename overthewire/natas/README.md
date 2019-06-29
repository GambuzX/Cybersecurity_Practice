0 -> 1
Just look at the source code of the page.

1 -> 2
Just look at the source code of the page again. But this time you cant open it with a right click.

2 -> 3 
Looking at the source code we notice an image coming from '/files'. We can access that directory and open the 'users.txt' file to find the next level password.

3 -> 4
Looking at the commentary left about Google I thought about Google bots and the 'robots.txt' file. By opening this file we notice a secret folder and can find the password inside.

4 -> 5
You must change the 'referer' http header to 'http://natas5.natas.labs.overthewire.org/' in order to get the password.
I wrote a python script for that.

5 -> 6
You must change the cookie 'loggedin' value to 1 and the password is shown.

6 -> 7
Looking at the source code you notice that a secret value is used to compare, coming from 'includes/secret.inc'.
Accessing that file you can get the secret. Use that in the input box and you get the password.

7 -> 8
Clicking on any of the given links you notice that a parameter 'page' is being used in the search bar. By trying an invalid input you notice that an in include() method is being called.
You can use directory traversal to make it read the file you want in '/etc/natas_webpass/natas8', by writing '../../../../etc/natas_webpass/natas8'.
That gives you the password.

8 -> 9
By looking at the source code you can see how the input is encrypted. You can just start with the target encrypted message and apply the inverse operations used to encrypt, leading to the code 'oubWYf2kBq'. Use that in the input box and you get the password.
I wrote a python script for the decryption.

9 -> 10
Looking at the source code you see that grep is being called with a passthru command. You can exploit this by chaining commands, inputting '; cat /etc/natas_webpass/natas10'. The password will be returned.

10 -> 11
You can take control of the grep function by commenting the rest of the command with '#'.
Just read everything from /etc/natas_webpass/natas11, with '.* /etc/natas_webpass/natas11 #' and you get the password.

11 -> 12
In this level we need to somehow set the value of 'showpassword' inside the 'data' cookie to 'yes'. 
We have access to the source code used to encrypt the data, as well as to the data used in the default encryption.
Since the encryption method is a XOR with a key (hidden), our objective is to find it.
We can do it by XORing the data cookie (encrypted with the key) with the original default data that was encrypted.
After getting the key, we can just change 'showpassword' to 'yes' and use the key to encrypt again.
After that change the cookie 'data' value and reload the page.
You should see the password.
I used python to help me with the encryption/decryption.

12 -> 13
In this level you can take advantage of a Unrestricted File Upload vulnerability. 
By uploading a php script which reads the password from the server and altering the extension of the saved file from .jpg to .php (there is an hidden input box), you can then access the password via the link which is provided after uploading.

13 -> 14
This level is similar to the previous one, only changing that one additional check is done to the uploaded file to see if it really is of an image format.
We can exploit this check by appending at the start of the php script the magic numbers of a gif file (for example), which are 'GIF87a'.
The server will accept the script and by visiting the given link you can read the password.

14 -> 15
This can be solved with a basic SQL injection, such as: '" OR 1=1 --'.
The server will give you the password.

15 -> 16
In this level you must perform a Blind SQL Injection to get the password.
You can not visualize any query result, but you get a message telling you if it found a user or not. You can also inject more SQL besides the username, as it is not checked.
You can exploit this by providing a combination of username and password. If you get the 'This user exists.' message, it means you have the right password.
You can get the password by incrementally guessing its symbols with a bruteforce attack, using the SQL 'LIKE BINARY' keywords and '%' string match operator.
I wrote a python script to automate this for me.