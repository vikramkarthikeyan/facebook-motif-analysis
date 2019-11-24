import pandas as pd
import os

univs = ["American75","Bowdoin47","Cornell5","Haverford76","Maine59","Notre Dame57","Rochester38","Tennessee95","UCF52","UIllinois20","Vassar85","Williams40",
"Amherst41","Brandeis99","Dartmouth6","Howard90","Maryland58","Oberlin44","Rutgers89","Texas80","UCLA26","UMass92","Vermont70","Wisconsin87",
"Brown11","Duke14","Indiana69","Mich67","Oklahoma97","Santa74","Texas84","UCSB37","UNC28","Villanova62","Yale4",
"Auburn71","Bucknell39","Emory27","JMU79","Michigan23","Penn94","Simmons81","Trinity100","UCSC68","UPenn7","Virginia63",
"BC17","Cal65","FSU53","Johns Hopkins55","Middlebury45","Pepperdine86","Smith60","Tufts18","UCSD34","USC35","Wake73",
"BU10","Caltech36","GWU54","Lehigh96","Mississippi66","Princeton12","Stanford3","Tulane29","UChicago30","USF51","WashU32",
"Baylor93","Carnegie49","Georgetown15","MIT8","NYU9","Swarthmore42","UC33","UConn91","USFCA72","Wellesley22",
"Berkeley13","Colgate88","Hamilton46","MSU24","Northeastern19","Reed98","Syracuse56","UC61","UF21","UVA16","Wesleyan43",
"Bingham82","Columbia2","Harvard1","MU78","Northwestern25","Rice31","Temple83","UC64","UGA50","Vanderbilt48","William77"]

def generate_edges(folder_name):

    PREFIX = "data/" + folder_name + "/" + folder_name
    FILE =  PREFIX + ".edgelist"
    OUTFILE = PREFIX + "_bidirectional.edgelist"

    os.system("rm -rf " + PREFIX + "_bidirectional_male.edgelist")
    os.system("rm -rf " + PREFIX + "_bidirectional_female.edgelist")

    with open(FILE, "r") as f:
        edges = f.readlines()

    result = ""

    for edge in edges:
        edge_split = edge.split()
        left = int(edge_split[0])
        right = int(edge_split[1])
        result += edge_split[0]+"\t"+edge_split[1]+"\n"
        result += edge_split[1]+"\t"+edge_split[0]+"\n"
    
    with open(OUTFILE, "w") as f:
        f.write(result)


for univ in univs:
    print(univ)
    generate_edges(univ)
