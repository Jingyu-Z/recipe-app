# public static bool IsPrime(int number)
# {
#     if (number < 2) return false;
#     for (int i = 2; i <= Math.Sqrt(number); i++)
#     {
#         if (number % i == 0) return false;
#     }
#     return true;
# }

import math

def is_prime (num):

    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True