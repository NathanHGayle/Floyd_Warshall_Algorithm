# Timing Python Scripts
from datetime import datetime
from recursive_solution import floyd_recursive
from imperative_solution import floyd
import pandas as pd
from config import graph_one
from config import graph_two
from config import graph_three
from config import graph_four
from config import graph_five
import sys

no_path = sys.maxsize


def floyd_main(graph, graph_name):
    script_start_time = datetime.now()
    # START
    floyd(graph)
    # END
    script_end_time = datetime.now()
    runtime = script_end_time - script_start_time
    results_dict = {'graph': graph_name, 'floyd_main_runtime': f'{runtime}'}
    df = pd.DataFrame([results_dict])
    return df


def floyd_recursive_main(graph, graph_name):
    script_start_time = datetime.now()
    # START
    floyd_recursive(graph)
    # END
    script_end_time = datetime.now()
    runtime = script_end_time - script_start_time
    results_dict_rec = {'graph': graph_name, 'floyd_recursive_main_runtime': f'{runtime}'}
    df = pd.DataFrame([results_dict_rec])
    return df


def floyd_perf_test():
    one = floyd_main(graph_one, 'one')
    two = floyd_main(graph_two, 'two')
    three = floyd_main(graph_three, 'three')
    four = floyd_main(graph_four, 'four')
    five = floyd_main(graph_five, 'five')
    combined_df = pd.concat([one, two, three, four, five], ignore_index=True)
    return combined_df


def floyd_rec_perf_test():
    one = floyd_recursive_main(graph_one, 'one')
    two = floyd_recursive_main(graph_two, 'two')
    three = floyd_recursive_main(graph_three, 'three')
    four = floyd_recursive_main(graph_four, 'four')
    five = floyd_recursive_main(graph_five, 'five')
    combined_df = pd.concat([one, two, three, four, five], ignore_index=True)
    return combined_df


def performance_test_df():
    original = floyd_perf_test()
    recursion = floyd_rec_perf_test()
    performance_df = original.merge(recursion, 'left', left_on='graph', right_on='graph')
    # establish hypothesis that the recursive function will have a lower runtime then the original function
    performance_df['hypothesis'] = performance_df['floyd_recursive_main_runtime'] < performance_df['floyd_main_runtime']
    return performance_df


def main():
    # create five performance tests per function, per graph
    df = performance_test_df()
    df.to_csv("pt_six.csv")
    df.to_csv("pt_seven.csv")
    df.to_csv("pt_eight.csv")
    df.to_csv("pt_nine.csv")
    df.to_csv("pt_ten.csv")


if __name__ == "__main__":
    main()
