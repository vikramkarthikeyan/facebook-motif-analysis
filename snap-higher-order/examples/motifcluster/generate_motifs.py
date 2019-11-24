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


def generate_motifs(univ):
    edgelist_file = "../../../data/" + univ + "/" + univ + "_bidirectional.edgelist"
    nodelist_file = "../../../data/" + univ + "/" + univ + ".nodelist"
    os.system("./motifclustermain -i:" + edgelist_file + "-m:M4 -n:" + nodelist_file)
    

for univ in univs:
    generate_motifs(univ)

# ./motifclustermain -i:../../../data/UCSD34/UCSD34.edgelist -m:M4 -n:../../../data/UCSD34/UCSD34.nodelist 