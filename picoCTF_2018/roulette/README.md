1. Since the initial money is the seed used in srand(), we can extract it and predict which values will come out of rand()

I wrote a C piece of code to generate thoses numbers.

2. With those numbers we can guess 3 succesfull roulette spins, earning the 3 wins needed to get the flag.

3. To raise the money above 1 billion, you must wage a really large number that will be interpreted as a negative one.

I used 2684354560, which was subtracted from Current Balance and thus raised it.



I got the flag picoCTF{1_h0p3_y0u_f0uNd_b0tH_bUg5_25142e09} . 