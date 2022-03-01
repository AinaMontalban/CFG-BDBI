#!/usr/bin/env python

#Script used to obtain orthologs using a species overlap algorithm.
#It will take a file where the first column is the gene of interest and 
#the second column is the newick tree

import ete3
import argparse

#Loads trees into memory
def load_trees(fileName):
	trees = {}
	for line in open(fileName):
		line = line.strip()
		dades = line.split("\t")
		trees[dades[0]] = dades[1]
	return trees

def load_species_name(node):
	return node.split("_")[1]

#Extracts orthologs for the species of interest
def get_orthologs(tree_newick,code):
	orthologs = set([])
	#Create phylogenetic tree object, it needs the function load_species_name to know which part of the code belongs to the species
	t = ete3.PhyloTree(tree_newick,sp_naming_function=load_species_name)
	#Checks whether the tree is rooted and else it will set a midpoint rooting
	if len(t.get_children()) != 2:
		t.set_outgroup(t.get_midpoint_outgroup())
	#Locate the protein of interest within the tree after making sure it's there
	if code in t.get_leaf_names():
		seed_node = t.get_leaves_by_name(code)[0]
		#Apply species overlap algorithm in the lineage leading to the sequence of interest
		events = seed_node.get_my_evol_events()
		#The returning events can be either duplications or speciations therefore we have to filter them out
		for ev in events:
			if ev.etype == "S":
				#If the node indicates a speciation event, get the orthologs to your seed protein
				for c in ev.out_seqs:
					orthologs.add(c)
	return orthologs

def print_orthologs(all_orthologs):
	for code in all_orthologs:
		codes = list(all_orthologs[code])
		codes = sorted(codes,key=lambda x:x.split("_")[1])
		if len(codes) == 0:
			print (code+"\tNo orthologs")
		else:
			print (code+"\t"+";".join(codes))

parser = argparse.ArgumentParser(description="Get orthologs for trees")
parser.add_argument("-i","--tree_file",dest="treeFile",action="store",required=True,help="File where the trees and their proteins of interest can be found")
args = parser.parse_args()				

trees = load_trees(args.treeFile)
all_orthologs = {}
for code in trees:
	all_orthologs[code] = get_orthologs(trees[code],code)
print_orthologs(all_orthologs)
