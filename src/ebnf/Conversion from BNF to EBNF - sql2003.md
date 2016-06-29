# Conversion from BNF to EBNF - sql2003

1. Use `-{2,4}h3[\S\s]*?\n-{2,4}/h3\n` to remove `h3` headers
1. Use `-{2,4}p[\S\s]*?\n-{2,4}/p\n` to remove `p` paragraphs
1. Use `-{2,4}##.*$\n` to remove `html` code
1. Use `-{2,4}h2[\S\s]*?\n-{2,4}/h2\n` to remove `h2` headers. - Had manual fix, no close tag
1. Use `--.*$` to remove misc. comments headers. & manual cleanup
1. Replace `PL/I` with `PL_I`
1. Replace `(<.*): (.*>)` with `\1_\2` to remove colons
1. Replace `(<.*)-(.*>)` with `\1_\2` to remove hyphens- apply multiple times. note END-EXEC was mistakely changed. will fix later
1. use script from readme to remove all spaces from rule names
1. use `([^'<])\b(\w+)\b([^'>])` to quote with `\1'\2'\3` apply multiple times
1. manually quote symbols
1. add semicolong to defintions
1. add spaces between >< '< >'
1. remove <...> replace ::=
used `<(\w+)>` `\L$1` for lowercase and remove <>
