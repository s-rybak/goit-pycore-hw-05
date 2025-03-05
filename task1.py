# Implementation of the Fibonacci sequence calculation with caching (memoization)
# to optimize performance by avoiding redundant calculations

def caching_fibonacci():
    # Dictionary to store previously calculated Fibonacci numbers
    cache = {}
    
    def fibonacci(n):
        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
            
        # Check if the result is already in cache
        if n in cache:
            return cache[n]
            
        # Calculate the Fibonacci number and store it in cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
        
    # Return the inner function that has access to the cache
    return fibonacci


# Create a callable function with persistent cache
fib = caching_fibonacci()

# Test the function with different values
print(fib(10))  # Output: 55
print(fib(15))  # Output: 610