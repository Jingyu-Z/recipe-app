# public static int CountVowels(string input)
# {
#     string vowels = "aeiouAEIOU";
#     int count = 0;

#     foreach (char character in input)
#     {
#         if (vowels.Contains(character))
#         {
#             count++;
#         }
#     }

#     return count;
# }

def count_vowels (input):

    vowels = "aeiouAEIOU"
    count = 0

    for character in input:
        if character in vowels:
            count += 1
        
    return count