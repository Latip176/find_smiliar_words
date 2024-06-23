def levenshtein_distance(a, b):
    if len(a) < len(b):
        a, b = b, a

    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def similarity_percentage(a, b):
    distance = levenshtein_distance(a, b)
    max_len = max(len(a), len(b))
    similarity = (1 - distance / max_len) * 100
    return similarity

def find_most_similar_words(target, words, top_n=3):
    similarities = [(word, similarity_percentage(target, word)) for word in words if similarity_percentage(target, word) > 50]
    sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    top_similar_words = sorted_similarities[:top_n]
    return top_similar_words


target_word = "jer"
word_list = ["gajah", "jerapah", "kucing", "anjing", "gajih", "badak", "harimau"]

top_similar_words = find_most_similar_words(target_word, word_list)


print(f"Kata-kata yang paling mirip dengan '{target_word}':")
for word, similarity in top_similar_words:
    print(f"{word} dengan kemiripan {similarity:.2f}%")