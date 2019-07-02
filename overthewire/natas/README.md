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

16 -> 17
In this level more characters are escaped, but the '$' is not. This means we can still execute commands and get its output like $(ls).
You must blindily test characters to guess the password.
By executing the command 'grep -E ^a.* /etc/natas_webpass/natas17', we will only get output if the password starts with an 'a'.
By chaining this with the word 'hello', like this: $(grep -E ^a.* /etc/natas_webpass/natas17)hello, we will get the word 'hello' if it is wrong and 'ahello' if it is correct. Using the grep of the webpage, if we guessed the start of the password correctly, there will be no output.
With this, by continuously storing the found characters and changing the regex expression, we can guess the password with a bruteforce attack.
I wrote a python script to automate this. The first part looks for characters that appear in any part of the password, so that the bruteforce only has to iterate over those characters and be more efficient.

17 -> 18
This level is like level 15, but you have no output regarding whether the user exists or not. As such, the approach here is to do a Time based attack.
By changing the query from 'username=natas18 and password LIKE BINARY %a%' to 'username=natas18 and if(password LIKE BINARY %a%, 2, 0)', if the credentials are valid, the server will take more time processing it (2 seconds in this case).
From this, we can change our script to measure the time the query takes to execute.
I updated the script to reflect this behaviour.

18 -> 19
A cookie is created with the value of your session ID (which is limited between 1 and 640). You just have to bruteforce all the session ids, sending requests with the cookie set, until you get the admin session ID.
Script: 'natas19.py'

19 -> 20
This level is similar to the previous one, but you may notice that the PHPSESSID is now different. It is an hexadecimal value and, decoding it, you notice that it is the result of hexing the following string: <session_id>-<username>.
I changed the previous script to reflect this, sending the cookie value of PHPSESSID as the hexadecimal of "<session_id>-admin" instead of just the session id.

20 -> 21
The vulnerability in this level is in the parsing of the 'myread' function. It reads the content from a file and, based on newlines and spaces, sets values in $_SESSION._
In the 'mywrite' function we can only write the value for 'name'. However, nothing prevents us from setting this value to 'admin\nadmin 1'. What this will do in the 'myread' function is: read the value for 'name' as 'admin'; read the value for 'admin' as 1.
With this the 'print_credentials' method will give us the flag.
I wrote a script to automate this.

21 -> 22
In the adjacent site you can set any value in Session that you want. You just have to set 'admin' to 1 and, since the 2 websites are colocated and the session from one is valid in the other, just reuse the session id to access the first site.

22 -> 23
Just access the website with the GET parameter 'revelio' and disabling redirects.

23 -> 24
You must input a string that contains 'iloveyou' and will be interpreted as a number above 10.
For example '11111111iloveyou'. 

24 -> 25
By making the strcmp return an error, the code below it will be executed (in this case getting the flag). To make it fail you can, for example, send the passwd as an array, with the following notation: <url>?passwd[]=h4ck3d