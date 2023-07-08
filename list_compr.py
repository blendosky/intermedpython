#lists comprehensions

def increment_one_number(number):
    return 1+number


def is_consonant(lis_letters):
    vocals = 'aeiou'
    is_consonant = [consonant for consonant in lis_letters if consonant in vocals]
    print(is_consonant)




def run():
    paragraph = 'Lleno de palabras sirvio que bien una vaca'
    list_words = paragraph.split()
    for words in list_words:
        filter_word = [word for word in words]
        is_consonant(filter_word)
        
        
        



if __name__ == '__main__':
    run()






