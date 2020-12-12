"""
Created on Sat Dec 12 15:29:28 2020

@author: Dan Burns
"""

import numpy as np
import matplotlib.pyplot as plt
import re


def make_regular_expressions(nreps):
    '''
    Make a regular expressions that will identify all of the possible exchanges
    '''
    regexes = [r"Repl ex\s+0\s+x\s+1", ]
    
    template_expression_a = r'Repl ex.*'
    template_expression_b = '\s+x\s+'
    
    for i in range(1,nreps - 1):
        regex_a = template_expression_a + str(i) 
        regex_b = template_expression_b + str(i +1)
        regexes.append(regex_a + regex_b)
    
    return regexes
    
    
def make_exchange_lists(nreps):
    '''
    Make the list of lists that will record all the exchanges and initialize each list with 
    the replica id that it will follow as it traverses temperatures
    '''
    exchanges = [[] for i in range(nreps)]
    for i in range(nreps):
        exchanges[i].append(i)
    return exchanges


def find_next_exchange_line(line):
    '''
    Read the log file until the next record of exchanges
    '''
    if re.match(r"Repl ex\s+0",line):
        return True
    
    
def check_line_for_exchanges(regex_list, line):
    '''
    Determine if any exchanges happened on the current line. If none happened inform the loop so that the proper
    action can be taken.
    '''
    check_list = []
    for regex in regex_list:
        if re.match(regex, line):
            check_list.append('y')
    if 'y' in check_list:
        return True
    else:
        return False
    
def check_lists_for_last_exchange(exchange_lists, index):
    '''
    Used inside of record_exchanges()
    Go through the list of lists and find the list that
    contains the last exchange from the current replica
    '''
    for i, exchange_list in enumerate(exchange_lists):
        if exchange_list[-1] == index:
            return i
    
def record_exchanges(regex_list, exchange_lists, line):
    '''
    Go through the regular expressions and record each exchange that happened on the current log file line
    '''
    for r, regex in enumerate(regex_list):
        if re.match(regex, line):
            replica_a = check_lists_for_last_exchange(exchange_lists, r)
            replica_b = check_lists_for_last_exchange(exchange_lists, r+1)
            exchange_lists[replica_a].append(r+1)
            exchange_lists[replica_b].append(r)

def check_list_lengths(exchange_lists):
    '''
    Check the list that contains all the exchange lists and return how long the longest list is.  
    This will be used to tell the other lists to extend themselves out by appending their 
    current last element 
    '''
    lengths = []
    for exchange_list in exchange_lists:
        lengths.append(len(exchange_list))
        
    return max(lengths)

def update_static_lists(exchange_lists, current_length):
    '''
    any replicas that did not exchange on the current line get the last element of their list added on again
    so that all the lists reflect the same number of exchange attempts 
    '''
    for exchange_list in exchange_lists:
            if len(exchange_list) != current_length:
                exchange_list.append(exchange_list[-1])

def extend_all_lists(exchange_lists):
    '''
    In the event that no exchanges took place on the current line, extend all the lists by appending their 
    current last element
    '''
    for exchange_list in exchange_lists:
        exchange_list.append(exchange_list[-1])

def follow_exchanges(nreps, log_file):
    '''
    The main loop that records all of the exchanges in a list of lists.
    Each replica's unique walk through the temperature spaces is recorded in a list indexed by that replica's
    starting positon.  i.e. the replica that started in position 1 has it's temperature walk recorded in 
    the list exchanges[1].
    assign a variable to this function i.e. exchanges = follow_exchanges(number_of_replicas, path_to_log_file)
    '''
    # make the list of lists
    exchanges = make_exchange_lists(nreps)
    
    # make regexes to capture the log file's exchange lines (gromacs only)
    regexes = make_regular_expressions(nreps)
    
    # open the log file
    f = open(log_file, 'r')
    
    # go through the log file line by line
    for line in f.readlines():
        
        # check to see if the current line records exchanges instead of other md data
        if find_next_exchange_line(line) == True:
            # once on an exchange record line, check to see if any exchanges actually occur
            if check_line_for_exchanges(regexes,line) == True: 
                # if any exchanges occurred, record them
                record_exchanges(regexes,exchanges,line)
                # now find out how long the longest list is
                exchange_list_length = check_list_lengths(exchanges)
                # extend all the other lists by one respective duplicate terminal element so that they're all the same length
                update_static_lists(exchanges, exchange_list_length)
            else:
                # if no exchanges occurred, extend all lists by one respective duplicate terminal element
                extend_all_lists(exchanges)


        else:
            continue
    
    return(exchanges)

def make_exchange_graphs(rows, columns, exchange_lists, size=(20,16),):
    '''
    Make line plots showing how each replica travels through the temperatures
    rows*columns should be equal to or larger (if odd number of replicas) than the number of replicas
    in other words, it's the number of graphs to make
    '''

    fig, axs = plt.subplots(rows, columns, figsize=size)
    k=0
    for i in range(4):
        for j in range(5):
            axs[i,j].plot(exchange_lists[k])
            axs[i,j].set_title('replica ' + str(k))
            k+=1

    for ax in axs.flat:
        ax.set(xlabel='exchange', ylabel='temperature increment')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
    
    return axs
