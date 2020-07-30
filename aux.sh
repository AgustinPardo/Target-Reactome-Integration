curl -X GET "https://www.uniprot.org/uniprot/?query=organism:5664&columns=id&format=list&compress=no" -H "accept: text/plain" > lmajor_id.txt
awk '{print $0,NR}' lmajor_id.txt > lmajor_id.tmp && mv lmajor_id.tmp lmajor_id.txt
