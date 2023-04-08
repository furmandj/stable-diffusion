import speech_recognition as sr


def load_common_nouns(filename):
    with open(filename, "r") as f:
        nouns = set(line.strip().lower() for line in f.readlines())
    with open(filename, "r") as f:
        nouns_plural = set(line.strip().lower() + 's' for line in f.readlines())
    return nouns | nouns_plural

def find_nouns_and_sentences(text, common_nouns):
    words = text.split(' ')
    sentence_size = 10
    nouns_and_sentences = []

    word_index = sentence_size - 1
    while True:
        start_index = max([0, word_index - sentence_size + 1])
        end_index = min([len(words), word_index + 1])
        sentence = words[start_index: end_index]

        # Grab the last noun in the sentence
        word_sentence = None
        for word in sentence:
            if word.lower() in common_nouns:
                word_sentence = (word, ' '.join(sentence))
        if word_sentence is not None:
            nouns_and_sentences.append(word_sentence)

        word_index += sentence_size
        if word_index >= len(words):
            break

    return nouns_and_sentences


common_nouns = load_common_nouns("common_nouns.txt")

# Initialize recognizer
recognizer = sr.Recognizer()

if __name__ == "__main__":

    with sr.Microphone() as source:
        while True:
            # Obtain audio from the microphone
            print("Listening...")
            audio = recognizer.listen(source)

            # Recognize speech using Google Speech Recognition
            try:
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                nouns_and_sentences = find_nouns_and_sentences(text, common_nouns)
                print("You said: ", text)
                # Save sentences to transcript.txt
                with open("outputs/transcript.txt", "a") as f:
                    for noun, sentence in nouns_and_sentences:
                        f.write(sentence + "\n")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
