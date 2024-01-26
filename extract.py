from sys import argv
from os import mkdir

class line_structure:
    def __init__(self, book_name, chapter_number, verse_number, text):
        self.book_name = book_name
        self.chapter_number = chapter_number
        self.verse_number = verse_number
        self.text = text.replace("\n", "")


file_name = argv[1]
directory_name = argv[2]
file_contents = ""
try:
    file_open = open(f"{file_name}", "r")
    file_contents = file_open.read()
except Exception as e:
    print(f"Error {e}")

unformatted_lines = file_contents.split("\n")
formatted_lines = []
book_name_list = []

for line in unformatted_lines:
    try:
        line_divided = line.split("|")
        formatted_lines.append(line_structure(line_divided[0], line_divided[1], line_divided[2], line_divided[3]))
        if not line_divided[0] in book_name_list:
            book_name_list.append(line_divided[0])
    except Exception as e:
        print(f"Error {e}")
        continue


print(len(book_name_list))

if len(book_name_list) == 0:
    print(f"No books found in file")
    exit()

mkdir(directory_name)

for book in book_name_list:
    output_file = open(f"{directory_name}/{book}.txt", "w")
    verses = [verse for verse in formatted_lines if verse.book_name == book]
    joined_verses = " ".join([verse.text for verse in verses])
    output_file.write(joined_verses)
    output_file.close()
