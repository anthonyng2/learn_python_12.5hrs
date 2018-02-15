# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:57:49 2018

@author: AnthonyN
"""

import fibo    # Import library

fibo.fib(1000)    # To access the fib function in the fibo module
fibo.fib2(100)    # To access the fib2 function in the fibo module
fibo.__name__

fib = fibo.fib    # assign a local name for a function
fib(500)



