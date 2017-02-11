import re
import fileinput
import logging


logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


LAQUO = '«'
RAQUO = '»'

def typograf(text):
    return re.sub(r'"', LAQUO, line.rstrip())

if __name__ == '__main__':
    for line in fileinput.input():
        line = re.sub(r'&', r'&amp', line.rstrip())
        line = re.sub(r'<', r'&lt', line.rstrip())
        line = re.sub(r'>', r'&gt', line.rstrip())
        line = re.sub(r'\s+', r' ', line.rstrip())
        line = re.sub(r' - ', r' – ', line.rstrip())
        while '"' in line:
            line = line.replace('"', LAQUO, 1)
            line = line.replace('"', RAQUO, 1)
        while "\'" in line:
            line = line.replace('\'', LAQUO, 1)
            line = line.replace('\'', RAQUO, 1)

        # result = True
        # while result:
        #     result = re.search(r'\"', line)
        #     print(result)
        # for m in re.finditer(r"\"", line):
        #     print(m.start(), m.end())
        print(line)