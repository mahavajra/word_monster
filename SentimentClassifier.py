# Simple naive classifier that evaluates a sentence by
# checking the appearance of positive/negative keywords
class SentimentClassifier:
    # Take positive and negative word list
    def __init__(self, pos_wl, neg_wl):
        self.pos_wl = pos_wl
        self.neg_wl = neg_wl

    # Evaluate sentence
    # Output value is `# of positive words` - `# of negative words` in a given
    # sentence
    def evaluate(self, sentence):
        def count_appearance(sentence, wl):
            return sum(1 for word in wl if word in sentence)
        return count_appearance(sentence, self.pos_wl) - count_appearance(sentence, self.neg_wl)


if __name__ == "__main__":
    # Test utility function
    def run_test(sentence, is_positive):
        print("TEST SENTENCE:\t" + sentence)
        val = s.evaluate(sentence)
        result = (val > 0) if is_positive else (val < 0)
        print("EVALUATION:\t" + str(val))
        print("LABEL:\t\t" + ("positive" if val > 0 else "negative"))
        print("TEST RESULT:\t" + ("PASS" if result else "FAIL"))


    # initialize a SentimentClassifier
    s = SentimentClassifier(["good", "love", "pizza"], ["bad", "hate", "virus"])

    # define test sentences
    # sentences are a list of tuples of string and boolean that encode
    #    1) sentence
    #    2) expected output, true represents positive
    sentences = [
            ("pizzahut is a good place! i love it.", True),
            ("i hate that we've got a global pandemic going on. this virus is creating a havoc in the world.", False),
            ]

    # run the test
    for sentence, is_positive in sentences:
        run_test(sentence, is_positive)
        print()
