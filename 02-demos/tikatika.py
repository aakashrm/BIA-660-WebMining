#!/usr/bin/env python

from tika import parser
parsed = parser.from_file('financials.pdf')

with open('financials_metadata.txt', 'w') as file:
    file.write(str(parsed["metadata"]))

with open('financials_content.txt', 'w') as file:
    file.write(parsed["content"])
