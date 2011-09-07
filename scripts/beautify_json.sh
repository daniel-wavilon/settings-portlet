#!/bin/bash

tmp_dir=/tmp/beautify_json
mkdir -p $tmp_dir
lof=$tmp_dir/lof

beautify_json_ ( ) {
    local overwrite="$1"
    cat $lof | while read f ; do
        name=`echo $f | tr '/' '_'`
        tmp="$tmp_dir/$name"
        cat $f | python -mjson.tool > $tmp
        if [ "$overwrite" == "overwrite" ] ; then
            cp $tmp $f
            printf "File %-30s has been beautified\n" "$f"
        else
            printf "%-30s -> %s\n" "$f" "$tmp"
        fi
    done
}

overwrite="$1"
find . -name "*.json" | sed -e 's!^\./!!' > $lof
beautify_json_ $overwrite
