from opinionx.tfidf_shell import *
# run tf-idf and tf models for massive text files

run_tfidf_shell(input_folder="tfidf_folder/raw_data", # a list of text files
                output_folder="tfidf_folder/output", # output folder
                user_dict_path="tfidf_folder/user_dictionaries", # the folder contains csv files with each line as a word
                font_path="utils/fonts/SimHei.ttf",# use it when analysis Chinese text
                is_html=True
                )

