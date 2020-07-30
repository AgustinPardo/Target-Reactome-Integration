import argparse

def target_db_retrieve(input_file):
    """Levanto la data de archivo (Uniprot id, prot_organismo id)"""
    entrada = open(input_file)
    lines=entrada.readlines()
    entrada.close()
    dic_out={}
    for line in lines:
        line_split=line.split(" ")
        dic_out[line_split[0]]=line_split[1].rstrip()
    return dic_out

def reactome_db_retrieve(input_file):
    """Levanto la data de Reactome DB (Uniprot id, Reactome id)"""
    entrada = open(input_file)
    lines=entrada.readlines()
    entrada.close()
    dic_out={}
    for line in lines:
        line_split=line.split("\t")
        dic_out[line_split[0]]=line_split[1]
    return dic_out

def id_cross(organismo_data, reactome_data):
    """Curce de ids entre Reactome DB y Target DB"""
    reactome_dic_list=reactome_data.keys()
    organism_dic_list=organismo_data.keys()

    for llave in organism_dic_list:
        if llave in reactome_dic_list:
            print(organismo_data[llave]+"\t"+reactome_data[llave])
    return 0

# def target_db_integration(cruce_ids_data, organismo):
#     """Integro el cruce de ids a Target DB"""
#     return 0

def parse_arguments():
    """Parsea los argumentos de entrada"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", dest="target", nargs='+', help="help1")
    parser.add_argument("-r", dest="react", nargs="?", default="UniProt2Reactome_PE_Reactions.txt", help="help2")

    return parser.parse_args()

def main():
    """Control de argumentos y funciones"""
    args=parse_arguments()
    id_cross(target_db_retrieve(args.target[0]), reactome_db_retrieve(args.react))
    return 0

if __name__=='__main__':
    main()
