#!/usr/bin/env python3
# coding=UTF-8
import json
import re
FILES = ["array30.cin", "array-shortcode.cin", "array-special.cin"]
pattern = r"^([a-z,',.;/0-9]+)([\t ].+)$"
word = re.compile(pattern)
match_table = {}
# load mapping table
with open("mapping_table.json") as json_file:
    match_table = json.load(json_file)
print(match_table)
# handle array30.cin
for file_name in FILES:
    with open("new/%s" % file_name, "w") as writer:
        with open(file_name, "r") as reader:
            for line in reader.readlines():
                try:
                    is_word = True
                    code = word.match(line)[1]
                    new_code = ""
                    for alpha in code:
                        new_code += match_table[alpha]
                except Exception as e:
                    print("exception")
                    print(str(e))
                    is_word = False
                finally:
                    if is_word:
                        writer.writelines(re.sub(pattern, r"%s\2" % (new_code), line))
                    else:
                        print(line)
                        writer.writelines(line)
        
