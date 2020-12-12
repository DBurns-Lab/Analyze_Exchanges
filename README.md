# Analyze_Exchanges
Replica Exchange Analysis

from Track_exchanges import *

usage:
follow_exchanges(nreps, log_file)

Returns a list of list where each list contains a single replica's walk through the temperatures.

nreps = # of replicas from your replica exchange simulation.

log_file must be gromacs format. You only need one of the log files as they all contain the same information

  
