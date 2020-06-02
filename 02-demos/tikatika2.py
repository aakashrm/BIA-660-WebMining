#!/usr/bin/env python

import re

from tika import parser

parsed = parser.from_file('internet_research_agency_indictment.pdf')

lst = re.findall('\S+@\S+', parsed["content"])

print(lst)
