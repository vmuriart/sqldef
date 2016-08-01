import sql2003 as parser_base

parser = parser_base.SqlParser()
ast = parser.parse("""SELECT 1, bat FROM dual WHERE 1 = 4;""",
    trace=True,)
    # colorize=True)
print ast
ast = parser.parse("""
    -- comment
    SELECT a a,dual.b, triple.c as r, 2 b, 3 c, d
    FROM dual t, triple WHERE 1 = 4""")
print ast
