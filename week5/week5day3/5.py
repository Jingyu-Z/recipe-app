# public static void PrintMultiples(int n)
# {
#     for (int i = 1; i <= 5; i++)
#     {
#         Console.Write(n * i + " ");
#     }
#     Console.WriteLine();
# }

def print_multiples(num):

    for i in range(1,6):
        print(num * i, end = " ")
    
    print()
