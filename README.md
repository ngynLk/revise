# A simple cli tool to revise your vocab or other stuff

### Usage:

```
usage: revise [-h] [-r] [-l LENGTH] file_path

positional arguments:
  file_path             The file to open with the definitions

optional arguments:
  -h, --help            show this help message and exit
  -r, --reverse         Reverse keys and definitions
  -l LENGTH, --length LENGTH
                        Length of the test (all of the definitions if not set)
```

The file to be used has: the meaning first then the definition (or the other way around, you can use the `-r` switch) separated by a colon `:`, line by line.

For example:
```
un pajaro:un oiseau
a pesar:malgré
la oficina:le bureau
recién:récent
acabar de:venir de
compartir:partager
una fuente:une fontaine
camino:chemin
```

### Installation:

Requires `python`.

+ Clone this repo
+ Link/Copy the `revise` file to somewhere in your `$PATH` or use the script directly (`./revise`)!
