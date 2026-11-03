
import nltk
import string
import matplotlib.pyplot as plt

from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer


nltk.download("gutenberg")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")


print("=== Список текстів Project Gutenberg ===")
print(gutenberg.fileids())

emma = gutenberg.words("austen-emma.txt")

print("\n=== Перші 20 слів роману Емма ===")
print(emma[:20])


total_words = len(emma)

print("\n=== Загальна кількість слів ===")
print(f"Кількість слів у тексті: {total_words}")


unique_words = len(set(word.lower() for word in emma))

print("\n=== Кількість унікальних слів ===")
print(f"Кількість унікальних слів: {unique_words}")


percentage = unique_words / total_words * 100

print("\n=== Порівняння результатів ===")

print(
    f"У тексті всього {total_words} слів, "
    f"серед них {unique_words} унікальних."
)

print(
    f"Унікальні слова становлять {percentage:.2f}% "
    f"від загальної кількості слів."
)


fdist = FreqDist(emma)

top_ten = fdist.most_common(10)

print("\n=== 10 найбільш уживаних слів ===")

for word, count in top_ten:
    print(f"{word}: {count}")


words = [item[0] for item in top_ten]
counts = [item[1] for item in top_ten]

plt.figure(figsize=(12, 6))
plt.bar(words, counts)

plt.title("10 найбільш уживаних слів у романі Emma")
plt.xlabel("Слова")
plt.ylabel("Кількість повторень")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_10_words.png", dpi=150)

print("\nПершу діаграму збережено: top_10_words.png")

plt.show()


stop_words = set(stopwords.words("english"))

without_stop_words = [
    word for word in emma
    if word.lower() not in stop_words
]


table = str.maketrans("", "", string.punctuation)

stripped = [
    word.translate(table).lower()
    for word in without_stop_words
]

stripped = [
    word for word in stripped
    if word.isalpha()
]

print("\n=== Перші 20 слів після очищення ===")
print(stripped[:20])


fdist_clean = FreqDist(stripped)

top_ten_clean = fdist_clean.most_common(10)

print("\n=== 10 найбільш уживаних слів після очищення ===")

for word, count in top_ten_clean:
    print(f"{word}: {count}")


clean_words = [item[0] for item in top_ten_clean]
clean_counts = [item[1] for item in top_ten_clean]

plt.figure(figsize=(12, 6))
plt.bar(clean_words, clean_counts)

plt.title("10 найбільш уживаних слів після очищення тексту")
plt.xlabel("Слова")
plt.ylabel("Кількість повторень")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_10_words_clean.png", dpi=150)

print("\nДругу діаграму збережено: top_10_words_clean.png")

plt.show()


def get_wordnet_pos(word):

    tag = nltk.pos_tag([word])[0][1][0].upper()

    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV
    }

    return tag_dict.get(tag, wordnet.NOUN)


lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word, get_wordnet_pos(word))
    for word in stripped
]


fdist_lemmas = FreqDist(lemmatized_words)

top_ten_lemmas = fdist_lemmas.most_common(10)

print("\n=== 10 найбільш уживаних слів після лематизації ===")

for word, count in top_ten_lemmas:
    print(f"{word}: {count}")

print("\nЛематизацію завершено!")