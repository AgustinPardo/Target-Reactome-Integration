import argparse
import os
import sys

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

    parser = argparse.ArgumentParser(description='Uniprot-TargetPathogen crosslink id')
    parser.add_argument("-f1", '--target_file', default=None, help="Input file of the organism. The file should have two colums: Uniprot id, prot_organismo id")
    parser.add_argument("-f2", '--reactome_file',  default="UniProt2Reactome_PE_Reactions.txt", help="Input file of reactome reactions id and uniprotID link: https://reactome.org/download/current/UniProt2Reactome_PE_Reactions.txt")

    return parser
    
def main():
    """Control de argumentos y funciones"""
    parser=parse_arguments()
    args=parser.parse_args()

    #Chequeo: Exitencia de archivos
    # if args.target_file and args.reactome_file:
    #     assert os.path.exists(args.target_file), f'{args.target_file} file does not exists'
    #     assert os.path.exists(args.reactome_file), f'{args.reactome_file} file does not exists'
    if args.target_file and args.reactome_file:
        if not(os.path.exists(args.target_file)) and os.path.exists(args.reactome_file):
            raise FileNotFoundError(f'{args.target_file} file does not exists')
        if os.path.exists(args.target_file) and not(os.path.exists(args.reactome_file)):
            raise FileNotFoundError(f'{args.reactome_file} file does not exists')
        if not(os.path.exists(args.target_file)) and not(os.path.exists(args.reactome_file)):
            raise FileNotFoundError(f'{args.target_file} and {args.reactome_file} file does not exists')
        
        #Chequeo: Archivos con contenido
        assert os.stat(args.target_file).st_size > 1, f'{args.target_file} is empty'
        assert os.stat(args.reactome_file).st_size > 1, f'{args.reactome_file} is empty'
    else:
        sys.stderr.write(
        f'error: You must specify target_file\n')
        parser.print_help(sys.stderr)
        sys.exit(1)



    id_cross(target_db_retrieve(args.target_file), reactome_db_retrieve(args.reactome_file))
    return 0

if __name__=='__main__':
    main()
