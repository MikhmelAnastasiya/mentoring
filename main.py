import FileHandler as fh
import Parser as p
import SqlDatabase as sql
import os



dirname = os.path.dirname(__file__)


INPUT_FOLDER = os.path.join(dirname, 'folders/input_folder')
PROCESSED_FOLDER = os.path.join(dirname, 'folders/processed_folder')
INCORRECT_FOLDER = os.path.join(dirname, 'folders/incorrect_input')
DB_FOLDER = os.path.join(dirname, 'folders/db_folder')
DB_NAME = 'mpdatabase.db'



def main():
    handler = fh.FileHandler(INPUT_FOLDER, INCORRECT_FOLDER, PROCESSED_FOLDER)
    handler.remove_invalid_files_from_folder()
    parser = p.Parser(handler.get_fb2_file())
    bookname = parser.get_book_name()
    number_of_paragraph = parser.get_number_of_paragraph()
    number_of_words = parser.get_number_of_words()
    number_of_letters = parser.get_number_of_letters()
    word_Upper = parser.get_words_in_uppercase()
    word_lower = parser.get_words_in_lower()
    words = parser.get_words_stats()
    db = sql.SqlDatabase(DB_FOLDER, DB_NAME)
    db.create_book_stat_table()
    db.create_input_file_stat_table()
    db.insert_book_stat_values(bookname[0],number_of_paragraph[0], number_of_words[0], number_of_letters[0], word_Upper,
                               word_lower)
    for items in words.items():
        db.insert_input_file_stat_values(items[0], items[1][0], items[1][1])
    handler.remove_processed_files_from_input_folder()
    print("Ok")


if __name__ == '__main__':
    main()
   
