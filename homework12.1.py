import codecs
import re
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        result_file = open(result_file, "w")
        result_file.write(str(re.findall(r'<[^>]+>(.*?)<[^>]+>' ,html)))

delete_html_tags("draft.html")

