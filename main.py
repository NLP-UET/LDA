import os
import glob
import sys
from operator import itemgetter  # for sort
import lda

STOP_WORDS_SET = set()

def print_topic_word_distribution(corpus, number_of_topics, topk, filepath):
    """
    Print topic-word distribution to file and list @topk most probable words for each topic
    """
    print("Writing topic-word distribution to file: " + filepath)
    V = len(corpus.vocabulary)  # size of vocabulary
    assert(topk < V)
    with open(filepath, "w") as f:
        for k in range(number_of_topics):
            word_count = corpus.topic_word_counts[k, :]
            word_index_count = []
            for i in range(V):
                word_index_count.append([i, word_count[i]])
            word_index_count = sorted(word_index_count, key=itemgetter(1), reverse=True)  # sort by word count
            f.write("Topic #" + str(k + 1) + ":\n")  # Number topics starting from 1
            for i in range(topk):
                index = word_index_count[i][0]
                f.write(corpus.vocabulary[index] + " ")
            f.write("\n")

def print_document_topic_distribution(corpus, number_of_topics, topk, filepath):
    """
    Print document-topic distribution to file and list @topk most probable topics for each document
    """
    print("Writing document-topic distribution to file: " + filepath)
    if topk >= number_of_topics:
        topk = number_of_topics - 1  # Adjust topk to be within valid range

    with open(filepath, "w") as f:
        D = len(corpus.documents)  # number of documents
        for d in range(D):
            topic_count = corpus.document_topic_counts[d, :]
            topic_index_count = []
            for i in range(number_of_topics):
                topic_index_count.append([i, topic_count[i]])
            topic_index_count = sorted(topic_index_count, key=itemgetter(1), reverse=True)
            f.write("Document #" + str(d + 1) + ":\n")  # Number documents starting from 1
            for i in range(topk):
                index = topic_index_count[i][0]
                f.write("Topic #" + str(index + 1) + " ")  # Number topics starting from 1
            f.write("\n")

def main(argv):
    print("Usage: python ./main.py <number_of_topics> <alpha> <beta> <maxiteration>")
    # load stop words list from file
    with open("./LDA/stopwords/stopwords.txt", "r") as stopwordsfile:
        for word in stopwordsfile:  # a stop word in each line
            word = word.strip()
            STOP_WORDS_SET.add(word)

    corpus = lda.Corpus()  # instantiate corpus
    # iterate over the files in the directory.
    document_paths = ['./LDA/texts/grimm_fairy_tales', './texts/tech_blog_posts', './texts/nyt']
    for document_path in document_paths:
        for document_file in glob.glob(os.path.join(document_path, '*.txt')):
            document = lda.Document(document_file)  # instantiate document
            document.split(STOP_WORDS_SET)  # tokenize
            corpus.add_document(document)  # push onto corpus documents list

    corpus.build_vocabulary()
    print("Vocabulary size:" + str(len(corpus.vocabulary)))
    print("Number of documents:" + str(len(corpus.documents)))

    number_of_topics = int(argv[1])
    alpha = float(argv[2])
    beta = float(argv[3])
    max_iterations = int(argv[4])
    corpus.lda(number_of_topics, max_iterations, alpha, beta)

    print_topic_word_distribution(corpus, number_of_topics, 20, "./LDA/result/topic-word.txt")
    print_document_topic_distribution(corpus, number_of_topics, 10, "./LDA/result/document-topic.txt")

if __name__ == "__main__":
    main(sys.argv)