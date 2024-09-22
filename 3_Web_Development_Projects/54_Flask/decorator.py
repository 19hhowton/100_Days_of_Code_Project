import time

# Write your code below 👇

def speed_calc_decorator(function):
  """
  use *args, **kwargs
      - take current time 
      - run function
      - take new time 
      - subtract current time from new time
      return the result of running the function! That should not be lost :) 
    return the amount of time it took for the function to run 
  """
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = function(*args, **kwargs)
    end_time = time.time()
    diff = start_time - end_time
    print(f"{function.__name__} run speed: {end_time - start_time}s")
    return result
  return wrapper


  
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
