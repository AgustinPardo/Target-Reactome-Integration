import argparse

def target_db_retrieve(organismo):
    """Me conecto a la Target DB y obtengo la data del organismo (Uniprot id, organismo id, organismo Target DB id)"""
    return 0

def reactome_db_retrieve(input_file):
    #Archivo de entrada UniProt2Reactome_PE_Reactions.txt
    """Levanto la data de Reactome DB (Uniprot id ,Reactome id)"""
    return 0

def id_cross(organismo_data, reactome_data):
    """Curce de ids entre Reactome DB y Target DB"""
    return 0

def target_db_integration(cruce_ids_data, organismo_target_id):
    """Integro el cruce de ids a Target DB"""
    return 0

def mensaje(input1, input2):
    """Imprimo mensajes de resultados"""
    print(input1+" "+input2)
    return 0

def parse_arguments():
    """Parsea los argumentos de entrada"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest="AA", nargs='+', help="help1")
    parser.add_argument("-b", dest="BB", nargs="?", default="b_default", help="help2")

    return parser.parse_args()

def main():
    """Control de argumentos y funciones"""

    args=parse_arguments()
    print(args)
    mensaje(args.AA[0], args.BB)

    return 0

if __name__=='__main__':
    main()
