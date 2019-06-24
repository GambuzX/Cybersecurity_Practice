Just send a large amount of data to crash the program, 1000 characters worked with me.

To be able to control the crash, it was needed to know to which value the program was jumping to. For this I ran it as "qemu-mipsel-static -strace ./bof".

I wrote a script to automate it

Flag: CTF{Why_does_cauliflower_threaten_us}