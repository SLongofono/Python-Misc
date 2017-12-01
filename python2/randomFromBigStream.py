"""
This comes from the Daily Coding Problem blog at https://dailycodingproblem.com/

Given a very large stream of inputs, how can you select one at random without storing the entire stream?

We only want to traverse the data once, and we want to do this as quickly as possible.  In general, we want
the element picked to have a probability of 1/n, where n is the total number of elements in the stream.

Consider the base case: a stream with 1 element.  Our looping variable i=0, n=i+1.  We pick the 0th element.
  We have a 1/n = 1/(i+1) chance of selecting the element, so our problem is correctly solved.

Consider the n=1 case: we need to pick a number with 1/n probability, and again this is equivalent to picking
a number with a 1/(i+1) probability.  How to do so?  If we use a good random library, we can select from any
range of numbers with reasonably random distribution.  However, we don't know how many elements, so we can't
specify the proper bounds.  The key idea is to realize that for the ith element, we can select at random from
a sample space of i+1 elements.  If we pick a particular element in that sample space, it has the desired 1/n
probability, and we select the current stream element as our return value.  If we do so, every selection we make
is selected with 1/n probability, and as long as we repeat the process every time n increases (every time we
encounter a new element in the stream), we will have selected from all the numbers in the stream with equal
probability.

Digging a little deeper: consider drawing a card from a deck without revealing it.  We could say, if an ace of
spades is drawn from a second deck, we will replace the original card and select another without revelaing it.
If you draw another without revealing it, and put the first back, you have not changed the probability of either
card being drawn.  No new information was revealed for the first deck.  This is analogous to what we want to do
with the second random selection.

On to the code
"""

import random

def OMGSOMANYELEMENTS(ls):
  # Our return value will change many times
  retval = None
  
  # We will eventually visit each element in the stream, but only store one at a time
  for i, e in ls:
    
    # Make the random selection given the known number of elements i+1.
    # Using the second deck analogy above, 1 is the ace of spades.
    # Note that randint is inclusive on both bounds
    if 1 == random.randint(1, i+1):
      retval = e
      
  return retval
  
if __name__ == "__main__":
  with open("infilestream.dat", 'r') as infile:
    mySelection = OMGSOMANYELEMENTS(infile)
  print("Selected {}".format(mySelection))
