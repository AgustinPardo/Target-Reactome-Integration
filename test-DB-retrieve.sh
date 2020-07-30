#Download Reactome reactions uniprotID Database (UniProt2Reactome_PE_Reactions.txt 161 Mb).
curl -X GET "https://reactome.org/download/current/UniProt2Reactome_PE_Reactions.txt" -H "accept: text/plain"

# Download organism uniprotID proteome.
url -X GET "https://www.uniprot.org/uniprot/?query=organism:5664&columns=id&format=list&compress=no" -H "accept: text/plain" > lmajor_id.txt
# Add an id tag to the each uniprotID.
awk '{print $0,"lm_"NR}' lmajor_id.txt > lmajor_id.tmp && mv lmajor_id.tmp lmajor_id.txt
