from rxnmapper import RXNMapper
from rdkit.Chem import rdChemReactions
from rdkit.Chem import AllChem
import rdkit

print(rdkit.__version__)

rxn_mapper = RXNMapper()
rxns = ['CC(C)S.CN(C)C=O.Fc1cccnc1F.O=C([O-])[O-].[K+].[K+]>>CC(C)Sc1ncccc1F',
        'C1COCCO1.CC(C)(C)OC(=O)CONC(=O)NCc1cccc2ccccc12.Cl>>O=C(O)CONC(=O)NCc1cccc2ccccc12']
results = rxn_mapper.get_attention_guided_atom_maps(rxns)
print(results)


def split_rxn_component(rxn, threshold=0.1):
    Rxn = AllChem.ReactionFromSmarts(rxn, useSmiles=True)
    Rxn.RemoveUnmappedProductTemplates(thresholdUnmappedAtoms=threshold, moveToAgentTemplates=True)
    Rxn.RemoveUnmappedReactantTemplates(thresholdUnmappedAtoms=threshold, moveToAgentTemplates=True)
    reaction = rdChemReactions.ReactionToSmiles(Rxn)
    return reaction

for case in results:
        mapped_rxn = case["mapped_rxn"]
        rxn1 = split_rxn_component(mapped_rxn)
        print(rxn1)
