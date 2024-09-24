import codecs
import re
def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_content = re.sub(r'<[^>]+>', '', html)

    cleaned_content_line = cleaned_content.splitlines()
    cleaned_content_line =[line.strip() for line in cleaned_content_line if line.strip()]   # убрав порожні рядки
    cleaned_content = '\n'.join(cleaned_content_line)

    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write(cleaned_content)

    print(f"Очищений текст записано в файл: {result_file}")

delete_html_tags('draft.html', 'cleaned.txt')

