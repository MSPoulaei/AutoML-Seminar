import re
import os

# Update the regular expression pattern to match the custom tag
pattern = re.compile(r'\\persianfootnote\{(.*?)\}(?:\\protect)?\\LTRfootnote\{(.*?)\}', re.MULTILINE | re.DOTALL | re.UNICODE)

# Specify the directory containing your LaTeX files
directory_path = './'

# Create empty lists to store word pairs
all_word_pairs = []

# Loop through all .tex files in the specified directory
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        if filename.endswith(".tex"):
            file_path = os.path.join(root, filename)
            
            # Read the LaTeX content from the file
            with open(file_path, 'r', encoding='utf-8') as file:
                latex_content = file.read()

            # Extract pairs of words using the updated pattern
            word_pairs = pattern.findall(latex_content)
            
            # Add the word pairs to the list
            all_word_pairs.extend(word_pairs)

# Sort the combined word pairs alphabetically
sorted_word_pairs = sorted(all_word_pairs, key=lambda x: x[0])

# Create the dictionary files
with open('dic/dicen2fa.tex', 'w', encoding='utf-8') as dict_file_en2fa:
    with open('dic/dicfa2en.tex', 'w', encoding='utf-8') as dict_file_fa2en:
        dict_file_en2fa.write(r"""
\chapter*{واژه‌نامه  انگلیسی به  فارسی}\markboth{واژه‌نامه  انگلیسی به  فارسی}{واژه‌نامه  انگلیسی به  فارسی}
\addcontentsline{toc}{chapter}{واژه‌نامه  انگلیسی به  فارسی}
\thispagestyle{empty}
""")
        dict_file_fa2en.write(r"""
\chapter*{واژه‌نامه فارسی به انگلیسی}\markboth{واژه‌نامه فارسی به انگلیسی}{واژه‌نامه فارسی به انگلیسی}
\addcontentsline{toc}{chapter}{واژه‌نامه فارسی به انگلیسی}
\thispagestyle{empty}
""")
        for pair in sorted_word_pairs:
            dict_file_en2fa.write(f'\\englishgloss{{{pair[1]}}}{{{pair[0]}}}\n')
            dict_file_fa2en.write(f'\\persiangloss{{{pair[0]}}}{{{pair[1]}}}\n')
