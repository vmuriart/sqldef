# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 08:46:16 2016

@author: vmuriart
"""

import parser_base
parser = parser_base.UnknownParser(parseinfo=True)
ast = parser.parse('select 1 from dual where 1 = 1', rule_name='start')
print(type(ast), ast)   # 1
# <type 'list'> [u'SELECT', [u'1'], [u'FROM', [u'dual'], u'WHERE', [u'1', u'=', u'1']]]
print(type(parser.ast), parser.ast)   # 2
# <class 'grako.ast.AST'> AST({'start': [u'SELECT', [u'1'], [u'FROM', [u'dual'], u'WHERE', [u'1', u'=', u'1']]]})
print(parser.ast.parseinfo)  # 3
# None