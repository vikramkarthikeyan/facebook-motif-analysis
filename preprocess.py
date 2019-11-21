import pandas as pd

universities = ["American75", "Amherst41", "Auburn71", "Baylor93", "BC17", 
"Berkeley13", "Bingham82", "Bowdoin47", "Brandeis99", "Brown11", "BU10", 
"Bucknell39", "Cal65", "Caltech36", "Carnegie49", "Colgate88", "Columbia2", 
"Cornell5", "Dartmouth6", "Duke14", "Emory27", "FSU53", "Georgetown15", 
"GWU54", "Hamilton46", "Harvard1", "Haverford76", "Howard90", "Indiana69", "JMU79", "Johns Hopkins55", "Lehigh96",
"Maine59", "Maryland58", "Mich67", "Michigan23", "Middlebury45", "Mississippi66", "MIT8",
"Northeastern19", "Northwestern25", "NYU9", "Oberlin44", "Oklahoma97", "Penn94", 
"Pepperdine86", "Princeton12", "Reed98", "Rice31", "Rochester38", "Rutgers89", "Santa74", "Simmons81", 
"Smith60", "Stanford3", "Swarthmore42", "Syracuse56", "Temple83", "Tennessee95", "Texas80",
"Texas94", "Trinity100", "Tufts18", "Tulane29", "UC33", "UC61", "UC64", "UCF52", "UChicago30", "UCLA26"
"UConn91", "UCSB37", "UCSC68", "UCSD34", "UF21", "UGA50", "UIllinois20", "UMass92", "UNC28",
"UPenn7", "USC35", "USF31", "USFCA72", "UVA16", "Vanderbilt48", "Vassar85", "Vermont70",
"Villanova62", "Virginia63", "Wake73", "WashU32", "Wellesley22", "Wesleyan43", "William77",
"Williams40", "Wisconsin87", "Yale4"]

gender_map = {
    "unknown": 0,
    "male": 1,
    "female": 2
}

JSON_RESULT = "result.json"

def process(folder_name, gender):
    FILE = folder_name+ "/" + folder_name + ".edgelist"
    OUTFILE = folder_name + "/" + folder_name + "_bidirectional_" + gender + ".edgelist"
    METADATA = folder_name + "/" + folder_name + ".nodelist"


    with open(FILE, "r") as f:
        edges = f.readlines()

    with open(METADATA, 'r') as f:
        nodes = f.readlines()
    
    nodes = pd.read_csv(METADATA, delimiter="\t")

    print("FOR ", folder_name)
    total_nodes = len(nodes)
    print(gender)
    print("---")
    count = len(nodes[nodes["gender"] == gender_map[gender]])
    
    with open(OUTFILE, "w") as f:
        for edge in edges:
            edge_split = edge.split()
            left = int(edge_split[0])
            right = int(edge_split[1])
            if nodes.loc[left, :]["gender"] == gender_map[gender] and nodes.loc[right, :]["gender"] == gender_map[gender]:
                f.write(edge_split[0]+"\t"+edge_split[1]+"\n")
                f.write(edge_split[1]+"\t"+edge_split[0]+"\n")
    
    with open(JSON_RESULT, "a") as f:
        f.write(folder_name + "\t" + gender + "\t" + str(count) + "\t" + str(total_nodes) + "\n")


for university in universities:
    for gender in gender_map:
        process(university, gender)