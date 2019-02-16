Can write any value to any address. 
Idea is to overwrite the GOT table for puts and call win.

1. Determine GOT entry for puts. I used gdb. 
	puts = 0x804a00c

2. Determine address of win function. 
	win = 0x804854b

3. Connect to the service with the given netcat command.

4. Write win address in puts location. 

5. You get a shell. Use "cat flag.txt" to get the flag.