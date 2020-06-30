#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:29:28 2020

@author: danielburns
"""
import analyze_exchanges

replica = 8

if replica != 0:
    xp = replica - 1
else:
    replica = 0

walker.append(replica)

On = True



while result[0] != 2:
    
    result = find_next_xch(xp, master_index)
    """
    if replica == 0:
        if result[0] == 0:
            replica += 1
            master_index = result[1]
            walker.append(replica)
    """
    if result[0] == 2:
        On = False
        break
    elif result[0] == 0:
        if replica == 0:
            replica += 1
            master_index = result[1]
            walker.append(replica)
            continue
        else:
            replica -= 1
            walker.append(replica)
            master_index = result[1]
            if replica == 0:
                continue
            else:
                xp -= 1
                continue
            
    elif result[0] == 1:
        replica +=1
        walker.append(replica)
        master_index = result[1]
        xp += 1
        continue
    
    
    
print(len(walker))
print(walker)
    