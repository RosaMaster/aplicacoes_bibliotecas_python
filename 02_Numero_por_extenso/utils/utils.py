from num2words import num2words

class NumberToWords:

    def convert_to_ordinal(number):
        num_ord = num2words(number, to='ordinal')
        return num_ord
    
    def convert_to_english(number):
        num_en = num2words(number, lang='en')
        return num_en

    def convert_to_portuguese(number):
        num_pt_br =  num2words(number, lang='pt-br')
        return num_pt_br
    
    def convert_to_portuguese_ordinal(number):
        num_pt_br_ord = num2words(number, lang='pt-br', to='ordinal')
        return num_pt_br_ord

