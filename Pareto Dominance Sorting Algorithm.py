import random
import pandas as  pd
import time
import numpy as np
import string
def quick_sort(): # this algorithm uses a copy of the original Dataframe by default.
    # Changes to the dataframe are made by loading and saving from a pickle file.
    # Directory of pickle file is the root of the project
    df = pd.read_pickle(fileName)
    rec_quicksort(0, len(df.columns) - 1)

def short_sort(left,right,size):# This function hadles the differnt cornner cases of quicksort median of three
    """
    :param left: index of left collumn
    :param right: index of right collumn
    :param size: size of the current array
    :return: Nothing
    """
    df = pd.read_pickle(fileName)  # loading the dataframe to make changes
    if (size<=1): # no need to sort
        return
    if(size==2):# swap the left and right
        if (df.iloc[0,left] <df.iloc[0,right]):
            swap_col(left, right)
            return
    else:# size ==3
        Median_sort(left, right) #do a median of three sort


def rec_quicksort(left, right): # Method to do a recursive quicksort
    """
    :param left: index of the left side of the array
    :param right: index of the right side of the array
    """
    size = right-left+1 # the size of the partition
    if(size<=3): # at this point we are basically done with sorting that partition if it's less than 3
        short_sort(left,right,size) # Do a short sort if array size is les than 3
    else:
        median = medianOfThree(left, right) # value of the pivot position
        partition = sub_partition(left, right, median) # position of the next pivot
        rec_quicksort(left, partition - 1) # quicksort the left side
        rec_quicksort(partition + 1, right)# quicksort the right side



def swap_col(left, right): # swaps to collums in a dataframe given the indexes of the collums you want to swap
    """
    :param left: Index of the left column
    :param right: Index fo the right column
    """
    df = pd.read_pickle(fileName) # loading the dataframe to make changes
    cols = list(df) # get a list of all columns
    cols[right], cols[left] = cols[left], cols[right]#swap the two indicies by collum in the list of collums
    num_rows = df.shape[0]# The number of rows
    swapped=df.loc[df.index[list(range(0, num_rows))], cols]# reconstruct the atframe
    swapped.to_pickle(fileName)#save the modified dataframe


def sub_partition(left, right, pivot):# left bound of the array, right bound of the array, pivot of the array. Returnes the next pivot
   """
   :param left: The left bound of the array
   :param right: The right bound of the array
   :param pivot: The pivot position of the array
   :return: The pivot of the new array
   """
   leftpos=left+1 # Median of three says we start 1 after the left bound
   rightpos = right-2 # and 2 after the right bound
   while(True):
       df = pd.read_pickle(fileName)# loading the dataframe for any changes we made previously
       while (df.iloc[0,leftpos] > pivot): # looking for a number smaller than the pivot to put on the left
           leftpos+=1

       while (df.iloc[0,rightpos] <pivot):#looking for a number bigger than the pivot to put on the right
           rightpos-=1
       if (leftpos >= rightpos):# if we cross pivots then we are done searching
           break
       else:
           swap_col(leftpos,rightpos)# swap the collums (No need to load)

   swap_col(leftpos, right - 1) # Put the pivot back in the original position
   return leftpos

def medianOfThree(left,right):
    """
    :param left:  left bound of array
    :param right: right bound of array
    :return: value of the pivot
    """
    center = Median_sort(left, right)
    swap_col(center, right-1)# puts the pivot to the right
    df = pd.read_pickle(fileName) # loading all the changes from the dataframe
    return df .iloc[0,right-1]


def Median_sort(left, right):# sort the variables by median using the left and right bounds of the array and reruens the value of the median of the array
    """
    :param left: Left bound of array
    :param right: right bound of array
    """
    df = pd.read_pickle(fileName) # loading the dataframe to make changes
    center = (left + right) // 2  # finds the center of the array
    if (df.iloc[0,left] <df.iloc[0,center]): # order the left and center
        swap_col(left,center)
        df = pd.read_pickle(fileName) # if any changers where made, reload dataframe
    if (df.iloc[0,left] <df.iloc[0,right]): # order left and right
        swap_col(left, right)
        df = pd.read_pickle(fileName) # if any changers where made, reload dataframe
    if (df.iloc[0,center] < df.iloc[0,right]):
        swap_col(center, right) # changes were already made, no need to save again,

    return center #(basically did this function to avoid repeated code)
def isDominated(df1:pd.DataFrame, df2: pd.DataFrame): # checks if DF1 is dominate over df2. Returns true if DF1 is dominant over DF2
    """

    :param df1: is a column in the dataframe
    :param df2: another column in the dataframe
    :return: True if df1 is dominate over Df2. False otherwise
    """
    pos=0 # row position
    num_rows = df1.shape[0] # Number of rows in the DF(Both Df have the same number of rows)
    while(pos<num_rows): # iterate through both DF; Checking to see if every element in DF1 is bigger than DF2
        if(df1.iloc[pos,0] <df2.iloc[pos,0]):
            return False
        else:
            pos+=1
    return True

Raw_Data_file = pd.ExcelFile("port_sus_2_14_18.xlsx") # load in the entire excell file(File assumed to be in root directory)
Norm_Scores = Raw_Data_file.parse('test',skiprows=0)  # Data frame representing the normalized scores
fileName = 'Norm_Scores.pickle'  # file name of the pickle file if it ever needs to be changed
Norm_Scores.to_pickle(fileName) # saving the dataframe for modification later on
quick_sort() # quicksort the dataframe

Sorted_df = pd.read_pickle(fileName)  # loading the quicksorted dataframe

non_dominated_cols=[] # the list of non dominated columns

col_list = list(Sorted_df ) # list of columns, This might be used in a future revision bu probably not


col=0 # keeps track of the columns
# this is where we determine the non-dominated set of data
while(col< len(Sorted_df.columns)):# while we did not reach the end of the array
    if(len(non_dominated_cols)==0):# check if the nondominated set is empty
        col_1 = Sorted_df.iloc[:, 0:1] # if so check the first and the second item
        col_2 = Sorted_df.iloc[:, 1:2]
        if(isDominated(col_1,col_2)==True): # if col 1 dominates, add it to the dominate set
            non_dominated_cols.append(col_1)
            col+=1 # we already checked the first two columns

        else: # if not than add both to the non Dominated set

            non_dominated_cols.append(col_1)
            non_dominated_cols.append(col_2)
            col += 1 #we already checked the first two collums
    else:
        item_1 =Sorted_df[[col_list[col]]] # the column we want to compare in the dataframe
        pos = 0 #tracking the position of collumns

        while (pos < len(non_dominated_cols)): # comparing Item 1 to the non-dominated set
            if (isDominated(non_dominated_cols[pos], item_1) == True):
                break
            else:# if item 1 is non dominated, move onto the next Item in the list of non-Dominated items
                pos += 1
        if(pos>=len(non_dominated_cols)):
            non_dominated_cols.append(item_1)
    col += 1 # Move onto the next column in the dataframe


non_dominated_df=pd.concat(non_dominated_cols, axis=1) # Combine all the non-dominated columns into ome dataframe

writer = pd.ExcelWriter('Non_Dominated portfolio.xlsx') # initialize a new sheet
non_dominated_df.to_excel(writer,'Sheet1') # Add the non Dominated portfolios to the sheet
writer.save() # save the sheet










