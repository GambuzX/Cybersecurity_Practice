Connect with 'nc readme.ctfcompetition.com 1337'

I looked through all the binaries we could execute in '/bin', '/sbin', '/usr/bin' and '/usr/sbin', searching for something that could be used to read files.

Used this website as a guide https://gtfobins.github.io/

Eventually I came to try 'fold', using '/usr/bin/fold -w10000 README.flag'

**Flag: CTF{4ll_D474_5h4ll_B3_Fr33}**


###BONUS FLAG
This level has a bonus flag, the file ORME.flag.

However, this file has permissions 000, which means it cant be read by anyone. 

To change this we would have to execute chmod, but we don't have it.

However, in '/bin' we notice there is 'busybox', which bundles up all the binaries in the machine, including chmod and cat.

When we try to run it we get the message "busybox can not be called for alien reasons.", so we need another way.

We have access to the binary 'run-parts', which executes all the scripts in a directory.

We can copy busybox to /tmp and then run "run-parts /tmp --arg sh" to get a shell that allows to run busybox.

After that just use chmod and cat (through busybox) to read the flag.

**Flag: CTF{Th3r3_1s_4lw4y5_4N07h3r_W4y}**