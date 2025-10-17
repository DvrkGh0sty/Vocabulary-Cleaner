def vocab_cleaner(vocab):
    punctuation = ['!', ',', '.', '/']
    clean_vocab = ''.join([ch for ch in vocab if ch not in punctuation])
    return clean_vocab

def main():
    print(vocab_cleaner("Python!!! is... awesome, but sometimes confusing."))

main()

"""
def vocab_clean(vocab):
    for char in vocab:
        if char in [',', '!', '.']:
            char.split"""



    



