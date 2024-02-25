# Timing Python Scripts
from datetime import datetime

import numpy as np
import pandas as pd
from recursive_solution import floyd_recursive
from imperative_solution import floyd
from config import graph_one
from config import graph_two
from config import graph_three
from config import graph_four
from config import graph_five
import sys

no_path = sys.maxsize

def log_update(entry):
    log = open('runtime_log.txt', 'a')
    log.write('\n' + entry)
    log.close()
    return print('successful')


def floyd_main(graph):
    script_start_time = datetime.now()
    # START
    floyd(graph)
    # END
    script_end_time = datetime.now()
    runtime = script_end_time - script_start_time
    log_update(f'algorithm: floyd main , graph: five, runtime: {runtime}')

def floyd_recursive_main(graph):
    script_start_time = datetime.now()
    # START
    floyd(graph)
    # END
    script_end_time = datetime.now()
    runtime = script_end_time - script_start_time
    log_update(f'algorithm: floyd recursive main , graph: four, runtime: {runtime}')

if __name__ == "__main__":
    # run through each graph by function
    # floyd_main(graph_five)
    # floyd_recursive_main(graph_five)
