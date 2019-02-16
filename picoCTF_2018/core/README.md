1. analyze disassembly

2. Set env variable SEED_ENV

3. Create flag file 

4. Run print_flag on gdb and search the heap for the flag written in 3. Found at 0x80610f0.

5. Search same memory address using core file. Run 'printf "picoCTF{%s}\n", 0x80610f0' to get flag.

picoCTF{c96bd0fa2da5c0853cf12c4f93fce288}