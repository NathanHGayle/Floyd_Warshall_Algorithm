from recursive_solution import floyd_recursive
from imperative_solution import floyd
from datetime import datetime
from config import graph_one
from config import graph_two
from config import graph_three
from config import graph_four
from config import graph_five
import pandas as pd

import sys

no_path = sys.maxsize


def floyd_runtime(graph, graph_name):
    """
    A function that records the runtime for the simple Floyd's algorithm script
    and stores results inside a DataFrame
    """
    script_start_time = datetime.now()
    # START
    floyd(graph)
    # END
    script_end_time = datetime.now()
    runtime = (script_end_time - script_start_time)
    # adding microseconds for more granularity
    runtime_microseconds = runtime.total_seconds() * 10 ** 6  # Convert seconds to microseconds
    results_dict = {'graph': graph_name, 'floyd_main_runtime': runtime_microseconds}
    df = pd.DataFrame([results_dict])
    return df


def floyd_recursive_runtime(graph, graph_name):
    """
    A function that records the runtime for the recursive implementation of Floyd's algorithm script
    and stores results inside a DataFrame
    """
    script_start_time = datetime.now()
    # START
    floyd_recursive(graph)
    # END
    script_end_time = datetime.now()
    runtime = script_end_time - script_start_time
    # adding microseconds for more granularity
    runtime_microseconds = runtime.total_seconds() * 10 ** 6  # Convert seconds to microseconds
    results_dict_rec = {'graph': graph_name, 'floyd_recursive_main_runtime': runtime_microseconds}
    df = pd.DataFrame([results_dict_rec])
    return df


def floyd_perf_test():
    """
    A function that calls floyd_runtimes for five different graphs
    and stores results inside an appended DataFrame.
    """
    one = floyd_runtime(graph_one, 'one')
    two = floyd_runtime(graph_two, 'two')
    three = floyd_runtime(graph_three, 'three')
    four = floyd_runtime(graph_four, 'four')
    five = floyd_runtime(graph_five, 'five')
    combined_df = pd.concat([one, two, three, four, five], ignore_index=True)
    return combined_df


def floyd_rec_perf_test():
    """
    A function that calls floyd_recursive_runtime for five different graphs
    and stores results inside an appended DataFrame.
    """
    one = floyd_recursive_runtime(graph_one, 'one')
    two = floyd_recursive_runtime(graph_two, 'two')
    three = floyd_recursive_runtime(graph_three, 'three')
    four = floyd_recursive_runtime(graph_four, 'four')
    five = floyd_recursive_runtime(graph_five, 'five')
    combined_df = pd.concat([one, two, three, four, five], ignore_index=True)
    return combined_df


def performance_test_df():
    """
    A function that joins the performance runtime results from both implementations of
    the algorithm and establishes two hypothesis to analysis the performances.
    """
    original = floyd_perf_test()
    recursion = floyd_rec_perf_test()
    performance_df = original.merge(recursion, 'left', left_on='graph', right_on='graph')
    # establish hypothesis that the recursive function will have a lower runtime then the original function
    performance_df['null_hypothesis'] = \
        performance_df['floyd_recursive_main_runtime'] != performance_df['floyd_main_runtime']
    performance_df['hypothesis_one'] = \
        performance_df['floyd_recursive_main_runtime'] < performance_df['floyd_main_runtime']
    performance_df['hypothesis_two'] = \
        performance_df['floyd_recursive_main_runtime'] > performance_df['floyd_main_runtime']
    return performance_df


def main():
    # create five performance tests per function, per graph
    df = performance_test_df()
    df.to_csv("csv_logs/pt_one.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_two.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_three.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_four.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_five.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_six.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_seven.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_eight.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_nine.csv", date_format='%Y-%m-%d %H:%M:%S.%f')
    df.to_csv("csv_logs/pt_ten.csv", date_format='%Y-%m-%d %H:%M:%S.%f')


if __name__ == "__main__":
   main()
