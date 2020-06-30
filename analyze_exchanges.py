#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:22:33 2020

@author: danielburns
"""

import re

# regular expressions for each exchange pair
regexes = [r"Repl ex\s+0\s+x\s+1", r"Repl ex.*1\s+x\s+2", r"Repl ex.*2\s+x\s+3",
           r"Repl ex.*3\s+x\s+4", r"Repl ex.*4\s+x\s+5", r"Repl ex.*5\s+x\s+6",
           r"Repl ex.*6\s+x\s+7", r"Repl ex.*7\s+x\s+8", r"Repl ex.*8\s+x\s+9",
           r"Repl ex.*9\s+x\s+10", r"Repl ex.*10\s+x\s+11", r"Repl ex.*11\s+x\s+12",
           r"Repl ex.*12\s+x\s+13", r"Repl ex.*13\s+x\s+14", r"Repl ex.*14\s+x\s+15",
           r"Repl ex.*15\s+x\s+16", r"Repl ex.*16\s+x\s+17", r"Repl ex.*17\s+x\s+18",
           r"Repl ex.*18\s+x\s+19"]

# make lists for each exchange pair that will store the line numbers for each exchange that that pair makes
exchanges = [[] for i in range(19)]
# open the md.log file
f = open('/Users/danielburns/Desktop/md.log', 'r')


# go through the md.log file looking for every time a pair exchanges and add that line number to that exchange pair's list
for i, line in enumerate(f):
    for x in range(19):
        if re.compile(regexes[x]).match(line):
            exchanges[x].append(i)

# master list for all the exchange attempt lines 
xch_lines = []
# reset to beginning of log file
f.seek(0)
# append all the exchange attempt lines to the list
for j, line in enumerate(f):
    if re.compile(r"Repl ex\s+").match(line):
        xch_lines.append(j)
"""
# print list of exchange probabilities
for p in range(19):
    print(str(p) + " x " + str(p+1) + " : " + str(len(exchanges[p])/len(xch_lines)*100))


# starting replica
replica = 9
# current exchange pair list (i.e 0 x 1 or 1 x 2 ...) 
xp = 8

"""
nreps = 20
maxpair = nreps - 2
# List the replicas that the walker goes through
walker = []

master_index = -1



def find_next_xch(xp, master_index):
    """
    returns 0 if the next exchange is down and (unless current replica = 1)
    returns 1 if the next exchange is up 
    """
    li = 1
    while True:
        
        """
        if xch_lines[master_index + 1] >= xch_lines[-1]:
            return (2,)
            break
        """
        
        if xch_lines[li + master_index] >= exchanges[xp][-1]:
            return (2,)
            break
        
        elif xch_lines[master_index + li] in exchanges[xp]:
            master_index = master_index +li
            return (0, master_index)
            break
        elif xp == maxpair:
            li += 1
            continue
        elif xch_lines[master_index + li] in exchanges[xp + 1]:
            master_index = master_index +li
            return (1, master_index)
            break
        
        else:
            li += 1
        
            
        
            
    
    
    
    
    




















