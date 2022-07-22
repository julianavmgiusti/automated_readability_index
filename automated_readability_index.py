def automated_readability_index(sentence):
    sentence_without_space = sentence.replace(' ','')
    letters_amount = len(sentence_without_space)
    words_amount = len(sentence.split())
    first_operation = (letters_amount/words_amount)
    second_operation = (0.5*(words_amount))
    result = math.ceil((4.71*(first_operation)) + (second_operation) - 21.43)
    if result < 1: 
        return 1
    if result > 14: 
        return 14
    return result
