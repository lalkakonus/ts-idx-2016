#!/bin/bash
# if [[ $1 == "varbyte" ]] || [[ $1 == "simple9" ]]
# then
#     python2 index.py $1 $2
# else
#     echo "Unkown indexing type"
#     exit 1
# fi
#fi
python2 index.py $@
#python2 index.py  varbyte dataset/1.gz
