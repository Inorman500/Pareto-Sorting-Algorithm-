# Pareto-Sorting-Algorithm-
# Ivan Norman and Destenie Nock

# Introduction
In Nock’s research, a model was created to evaluate portfolios comprised of different energy sources. Here the goal is to identify which portfolios are the best. The solution to this is to create a model that would perform a non dominated pareto sort, to reveal which portfolios are the best. Given two portfolios A and B, A dominates B if A is better or equal to in every category, and strictly greater than B in at least one category. B is non-dominated by A if the previous rule is violated. The data for the portfolios are contained in a table where the columns contain a single portfolios and the rows contain the criteria. In this paper we will describe the method of determining the non-dominated set of portfolios, for seven criteria, using a quicksort implementation. 

# How it works
The algorithm for determining the non-dominated set of portfolios was developed using methods similar to Mishra and Harit(2010).The flowchart is presented in Figure 1. The first step is to convert the excel file of energy portfolios into a dataframe. Dataframes are part of a library called pandas, which makes it easy to manipulate an excel file within a python program. The columns are then sorted by the elements in the first row from largest to smallest. To complete this step quicksort is implemented. An example of how quicksort works can be seen in appendix A. Quicksort is an algorithm used to sort data quickly by using different pivot points.  A few methods to select pivot points include always picking the first element, middle element, or last element. In our implementation, we selected the median of these three elements as a pivot position. We do this by using the first, middle and last elements of the array, choosing the median of those three elements as the pivot in addition to rearranging the array. For example: if we have the following array [44,1,86,6,29], after choosing median of three, the array will be [86,1,44,6,29]. We then partition the entire array so that in the end, all the numbers greater than the pivot are on the left side of the array and all the numbers less than the pivot are on the right side of the array. This is done using recursive loops, and pivot is updated at each iteration until the list is in order from greatest to least. The final array is [86,44,29,6,1] 

Our algorithm to determine dominance uses two loops. First, we define list G, a list comprising of the sorted elements, and list D, which will hold the non dominated elements. In the inner loop, we take a portfolio c, from G compare it to every element, i, from list D. If i dominates c, then the model breaks from the inner loop and moves on to the next element in G. If i does not dominate c, the model checks if c was compared to every element in list D, and if so we add c to list D and move on to the next portfolio in G. If c was not compared to every portfolio in list D, the model increments i by 1, moving onto the next portfolio in D, and then the model performs another comparison. The outer loop checks if every portfolio in A had been compared to every portfolio in D. If this is true then D is exported to an excel file.
