"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
  """ done. """
  for i,v in enumerate(mylist):
    if v == key:
      return i
  return -1


def binary_search(mylist, key):
  """ done. """
  return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  if left > right:
    return -1
  middle = (left + right) // 2
  if mylist[middle] == key:
    return middle
  elif mylist[middle] > key:
    return _binary_search(mylist, key, left, middle - 1)
  else:
    return _binary_search(mylist, key, middle + 1, right)




def time_search(search_fn, mylist, key):
  start = time.time()
  search_fn(mylist, key)
  end = time.time()
  duration = (end - start) * 1000
  return duration

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  result = []
  for n in sizes:
    mylist = list(range(int(n)))
    linear_st = time_search(linear_search, mylist, -1)
    binary_st = time_search(binary_search,mylist,-1)
    result.append((n, linear_st, binary_st))
  return result


def print_results(results):
  """ done """
  print(tabulate.tabulate(results,
              headers=['n', 'linear', 'binary'],
              floatfmt=".3f",
              tablefmt="github"))

print_results(compare_search())