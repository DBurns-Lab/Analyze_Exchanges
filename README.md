# Analyze_Exchanges
Replica Exchange Analysis
From Track_exchanges import *

use follow_exchanges(nreps, log_file)

nreps = # of replicas from your replica exchange simulation

log_file must be gromacs format. Only need one of the log files.

Returns a list of list where each list contains a single replica's walk through the temperatures.  
