

import sys
import codecs
import shelve

import importlib
importlib.reload(sys)

db = shelve.open("simple_rules.db", flag = "c", writeback=True)

template = """<?xml version="1.0" encoding="UTF-8"?>
<aiml version="1.0">

<meta name="author" content="autogen"/>
<meta name="language" content="zh"/>
{rules}
</aiml>
"""
category_template = """
<category>
<pattern>{pattern}</pattern>
<template>
{answer}
</template>
</category>
"""

#print sys.argv
if len(sys.argv) == 3:
    _, rule, temp = sys.argv

    print(temp)
    db[rule] = temp
    db.sync()

    rules = []
    for r in db:

        rules.append(category_template.format(pattern=r,answer=db[r]))
        #print(rules)
        content = template.format(rules = '\n'.join(rules))
        #print(content)
        with open("auto-gen.aiml", 'w') as fp:
            fp.write(content)
