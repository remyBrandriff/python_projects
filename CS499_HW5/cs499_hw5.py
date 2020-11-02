# Remy Brandriff
# CS499 - Bioinformatics
# Assignment 5

from ete3 import NCBITaxa, TreeStyle, AttrFace, faces


# Set the layout for the nodes, including name and ranks
def layout(node):
        N = AttrFace("sci_name", fsize=15)
        faces.add_face_to_node(N, node, 0, position="branch-right")
        N = AttrFace("rank", fsize=15)
        faces.add_face_to_node(N, node, 0, position="branch-right")


def taxonomic_tree(taxid):
    tree = ncbi.get_topology([taxid])
    print(tree.get_ascii(attributes=['sci_name', 'rank']))
    ts = TreeStyle()
    ts.layout_fn = layout
    ts.show_leaf_name = True
    tree.render("hw5.png", w=400, tree_style=ts)


if __name__ == '__main__':

    ncbi = NCBITaxa()

    id = ncbi.get_name_translator(['Bacillus'])
    print(id)
    # Got 55087 from the id
    taxonomic_tree(55087)