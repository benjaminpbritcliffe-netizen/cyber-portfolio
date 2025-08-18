# The Algorithm and Design Model

Created: 17 March 2025 11:55
Class: 1
Is Completed: Yes

- What are the specific requirements and constraints of the lottery optimisation problem?
- What variables do we need to consider when formulating the problem (e.g., total candidates, selected numbers for each ticket, winning criteria)
- How can we model the problem in terms of combinatorial objects, such as sets or subsets?
- What parameters will you define for the candidate set, the number of slots on each ticket, and the criteria for winning?
- How can we efficiently generate all possible subsets of numbers from the candidate set? What strategies can we use to ensure that at least one ticket covers the winning combinations?
- Should we use a brute-force search, or another algorithmic approach? Why?
- How can we minimise the number of tickets while ensuring that all necessary combinations are covered?

## Problem:

You are working with a company that helps customers predict winning lottery numbers. The lottery ticket has six numbers selected from a pool of numbers, say from 1 to 44. After training, a customer is able to predict 15 possible numbers, out of which at least 4 are guaranteed to be on the winning ticket.

Your task is to model this scenario and design an algorithm that minimizes the number of lottery tickets the customer needs to buy to ensure at least one ticket contains at least three correct numbers.

### Problem Parameters:

- Total candidate numbers predicted: 15
- Numbers to choose per ticket: 6
- At least 4 correct numbers guaranteed in the predicted set
- You win if at least 3 numbers on the ticket match the winning numbers.

### Goal:

Develop a solution that minimizes the number of tickets needed to guarantee a win. Start by thinking about how you can generate the necessary subsets of tickets and how to cover all possible winning combinations.