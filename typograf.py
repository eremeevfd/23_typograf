import re
import logging


logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


LAQUO = '«'
RAQUO = '»'
NBSP = '\u00A0'
NDASH = '–'
MDASH = '—'


def replace_quotes(text):
    return re.sub(r'(?<![=<])[\'\"](?![<>])(.*?)[\'\"](?!>)', r'{}\1{}'.format(LAQUO, RAQUO), text)


def binding_words_with_numbers(text):
    return re.sub(r'(\d)\s(\w)', r'\1{nbsp}\2'.format(nbsp=NBSP), text)


def replace_hyphens(text):
    return re.sub(r'(\s)-(\s)', r'\1{mdash}\2'.format(mdash=MDASH), text)


def bind_short_word_with_next_word(text):
    return re.sub(r'(\w{,2})\s(\w+)', r'\1{nbsp}\2'.format(nbsp=NBSP), text)


def delete_extra_spaces(text):
    return re.sub(r'[ ]+', r' ', text)


def replace_hyphens_in_phone_numbers(text):
    return re.sub(r'(\d+)-', r'\1{ndash}'.format(ndash=NDASH), text)


def delete_extra_lines(text):
    return re.sub(r'\s{2,}', r'\n', text)


def typograf(text):
    text = delete_extra_spaces(text)
    text = replace_hyphens_in_phone_numbers(text)
    text = replace_quotes(text)
    text = binding_words_with_numbers(text)
    text = replace_hyphens(text)
    text = bind_short_word_with_next_word(text)
    text = delete_extra_lines(text)

    return text


if __name__ == '__main__':
        print(typograf(input('text: ')))