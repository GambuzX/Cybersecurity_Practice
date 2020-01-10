#!/bin/bash

cmp cattos.jpg kitters.jpg -l | gawk '{printf "%c", strtonum(0$2)}' && echo 
