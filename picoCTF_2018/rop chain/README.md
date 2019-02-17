Exploited vulnerable buffer to create a stack frame where the functions 'ret' instructions jump to win_function1, win_function2 and flag, also inserting the correct arguments in the stack.

Stack frame:

|-----------------|

|      ...        |

|-----------------|

|     arg2        |

|-----------------|

|     arg1        |

|-----------------|

|     flag        |

|-----------------|

|  win_function2  |

|-----------------|

|  win_function1  | 

|-----------------|

|    padding      |

|-----------------|


flag: picoCTF{rOp_aInT_5o_h4Rd_R1gHt_718e6c5c}
