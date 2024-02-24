def floyd_recursive(distance):

    def helper(start_node, end_node, intermediate):
        # Base case
        if start_node == end_node:
            return 0
        # recursive case
        return min(
            helper(start_node,end_node,intermediate),
            helper(start_node,intermediate,intermediate) + helper((intermediate,end_node,intermediate)
                                                                  )

            # recursive call
            for intermediate in range(MAX_LENGTH):
                for start_node in range(MAX_LENGTH):
                    for end_node in range(MAX_LENGTH)

        )