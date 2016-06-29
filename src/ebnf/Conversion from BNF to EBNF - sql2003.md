# Conversion from BNF to EBNF - sql2003

1. Use `-{2,4}h3[\S\s]*?\n-{2,4}/h3\n` to remove `h3` headers
1. Use `-{2,4}p[\S\s]*?\n-{2,4}/p\n` to remove `p` paragraphs
1. Use `-{2,4}##.*$\n` to remove `html` code
1. Use `-{2,4}h2[\S\s]*?\n-{2,4}/h2\n` to remove `h2` headers. - Had manual fix, no close tag
1. Use `--.*$` to remove misc. comments headers. & manual cleanup

