#!/bin/bash

# This is a little script for refresh lzk_donatetip.pro and update .ts files.
# TRANSLATOR: You don't need to run it !

contents=""

this_script=`realpath "$0"`
locale_root=`dirname "$this_script"`
code_root=`dirname "$locale_root"`
cd "$code_root/resources/ui/"

for file in *.ui;do
    contents+="FORMS += ../resources/ui/$file
"
done


# for dir in daemon gui shared;do
    cd "$code_root/src/"
    
    for file in *.py;do
        [[ "$file" =~ ^"ui_" ]] && continue
        
        if cat "$file"|grep -q _translate;then
            contents+="SOURCES += ../src/${file}
"
        fi
    done
# done

contents+="
TRANSLATIONS += lzk_donatetip_en_US.ts
TRANSLATIONS += lzk_donatetip_fr_FR.ts
"

echo "$contents" > "$locale_root/lzk_donatetip.pro"

pylupdate5 "$locale_root/lzk_donatetip.pro"

