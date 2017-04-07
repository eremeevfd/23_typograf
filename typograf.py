import re
import fileinput
import logging


logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


LAQUO = '«'
RAQUO = '»'
NBSP = '\u00A0'
NDASH = '–'
MDASH = '—'


def replace_quotes(text):
    text = re.sub(r'(?<![=<])[\'\"](?![<>])(.*?)[\'\"](?!>)', r'{}\1{}'.format(LAQUO, RAQUO), text)
    return text


def binding_words_with_numbers(text):
    text = re.sub(r'(\d)\s(\w)', r'\1{nbsp}\2'.format(nbsp=NBSP), text)
    return text


def replace_hyphens(text):
    text = re.sub(r'(\s)-(\s)', r'\1{mdash}\2'.format(mdash=MDASH), text)
    return text


def bind_short_word_with_next_word(text):
    text = re.sub(r'(\w{,2})\s(\w+)', r'\1{nbsp}\2'.format(nbsp=NBSP), text)
    return text


def delete_extra_spaces(text):
    text = re.sub(r'[ ]+', r' ', text)
    return text


def delete_extra_lines(text):
    text = re.sub(r'\n{2,}', r'\n', text)
    return text


def typograf(text):
    text = replace_quotes(text)
    text = binding_words_with_numbers(text)
    text = replace_hyphens(text)
    text = bind_short_word_with_next_word(text)
    text = delete_extra_spaces(text)
    text = delete_extra_lines(text)
    return text


if __name__ == '__main__':
        print(typograf(input('text: ')))