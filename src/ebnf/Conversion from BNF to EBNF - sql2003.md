# Conversion from BNF to EBNF - sql2003

1. Use `-{2,4}h3[\S\s]*?\n-{2,4}/h3\n` to remove `h3` headers
1. Use `-{2,4}p[\S\s]*?\n-{2,4}/p\n` to remove `p` paragraphs
1. Use `-{2,4}##.*$\n` to remove `html` code
1. Use `-{2,4}h2[\S\s]*?\n-{2,4}/h2\n` to remove `h2` headers. - Had manual fix, no close tag
1. Use `--.*$` to remove misc. comments headers. & manual cleanup
1. Replace `PL/I` with `PL_I`
1. Replace `(<.*):(.*>)` with `\1_\2` to remove colons
1. Replace `(<.*)-(.*>)` with `\1_\2` to remove hyphens- apply multiple times. note END-EXEC was mistakely changed. will fix later
1. use script from readme to remove all spaces from rule names
1. use `([^'<])\b(\w+)\b([^'>])` to quote with `\1'\2'\3` apply multiple times
1. manually quote symbols
1. add semicolong to defintions
1. add spaces between >< '< >'
1. remove <...> replace ::=
used `<(\w+)>` `\L$1` for lowercase and remove <>

# convert 2011

1. use `\d+.\d+.+\n\nFunction\n(.*\n)*?Format` to convert comments and headers
1. Replace `(<.*):(.*>)` with `\1_\2` to remove colons
1. Replace `(<.*)-(.*>)` with `\1_\2` to remove hyphens- apply multiple times. note END-EXEC was mistakely changed. will fix later
1. use (^\d+ .*) to format all headers
1. use to select words to put quotes around (?<!['<])\b([A-Z_\-]+)\b(?!['>])
1. (?<!::=\s)    continuetions
1. use (^[^\n#].*)\n\n to add ; to the end of defintnions with \1\n    ;\n\n
1. use <(\w+)> \.\.\. to select ellipses after a rule. use {\1}+ to replace it
1, use `<(\w+)>[\n\s]+\[[\n\s]+{[\n\s]+<comma>[\n\s]+<\1>[\n\s]+}[\n\s]+\.\.\.[\n\s]+\]` to replace list chains with `<comma>.{\1}`

1. use for more generic version of above `(.*)[\n\s]+\[[\n\s]+{[\n\s]+<comma>[\n\s]+\1[\n\s]+}[\n\s]+\.\.\.[\n\s]+\]`
1. but first format `\[\n\s+` with `[ `
1. use `(?<!\.){(.*?)}(?!\+)` to remove left over {}
`(?<!\.){([\w \|']+?)}(?!\+)`
1. remove rules that have no context anymomre (rules werent being used)


1. `        (.*)\n    \|   ` to `    |   \1\n    |   ` to add leading | to options
