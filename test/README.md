# Test

 
### Download reactome reactions id and uniprotID link Database (UniProt2Reactome_PE_Reactions.txt 161 Mb).
```
curl -X GET "https://reactome.org/download/current/UniProt2Reactome_PE_Reactions.txt" -H "accept: text/plain" > UniProt2Reactome_PE_Reactions.txt
```


### Download organism Uniprot proteome. In this case we donwload all proteins of "Leishmania major" organism (taxonomic id: 5664)
```
url -X GET "https://www.uniprot.org/uniprot/?query=organism:5664&columns=id&format=list&compress=no" -H "accept: text/plain" > lmajor_id.txt
```


### After that we add an id tag to the each uniprotID.
```
awk '{print $0,"lm_"NR}' lmajor_id.txt > lmajor_id.tmp && mv lmajor_id.tmp lmajor_id.txt
```


### Run the core program

```
python main -f1 olmajor_id.txt -f2 UniProt2Reactome_PE_Reactions.txt
```
### You should have as result:

| Leishmania major protein id | Reactome reacton id |
| ------- | ----------------- |
| lm_7595 |R-LMA-9664404    |


