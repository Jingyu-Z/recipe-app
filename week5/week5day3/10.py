# public static string ReverseWords(string sentence)
# {
#     string[] words = sentence.Split(' ');
#     Array.Reverse(words);
#     return string.Join(' ', words);
# }


def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)