

from IUPAC2Struct.function import iupac2smiles

if __name__ == '__main__':

    paragraph_sequence = ['MAKESOLUTION with N-benzylethanolamine (44.8 ml, 314 mmol) and '
                         '2-chloroacrylonitrile (25 ml, 314 mmol)',
                         'ADD SLN',
                         'STIR for 24 hours at room temperature',
                         'SETTEMPERATURE 0° C',
                         'ADD tetrahydrofuran (300 ml)',
                         'ADD potassium tert-butoxide',
                         'STIR for one hour at 0° C',
                         'ADD ethyl-ether',
                         'WASH with water',
                         'WASH with brine',
                         'DRYSOLUTION over magnesium sulfate',
                         'CONCENTRATE',
                         'PURIFY',
                         'YIELD 4-benzylmorpholine-2-carbonitrile']

    rts_type = ["MAKESOLUTION", "ADD"]
    pts_type = ["YIELD"]


    rts=[]
    pts=[]
    import re
    for sequence in paragraph_sequence:
        sequence = re.sub('\(.*?\)', '', sequence)
        word_sequence = sequence.split(" ")
        word_sequence = [x.strip() for x in word_sequence if x.strip() != '']

        print(word_sequence)
        action_type = sequence.split(" ")[0]
        # print(action_type)
        if action_type == rts_type[0]:
            for idx, word in enumerate(word_sequence):
                if word == "with":
                    compound = word_sequence[idx+1]
                elif word == "and":
                    compound = word_sequence[idx+1]
                else:
                    continue
                try:
                    print("compound:", compound)
                    smiles_pred, prob = iupac2smiles(compound, beam=1)
                    print("smiles_pred ", smiles_pred[0])
                    rts.append(smiles_pred[0])
                except Exception as E:
                    print(E)

        if action_type == rts_type[1]:
            for idx, word in enumerate(word_sequence):
                if word == "ADD":
                    continue
    #             if "(" or ")" in word:
    #                 continue
                try:
                    compound = word_sequence[idx]
                    print("compound:", compound)
                    smiles_pred, prob = iupac2smiles(compound, beam=1)
                    print("smiles_pred ", smiles_pred[0])
                    rts.append(smiles_pred[0])
                except Exception as E:
                    print(E)
                    continue

        if action_type == pts_type[0]:
            for idx, word in enumerate(word_sequence):
                if word == "YIELD":
                    continue
    #             if "(" or ")" in word:
    #                 continue
                try:
                    compound = word_sequence[idx]
                    print("compound:", compound)
                    smiles_pred, prob = iupac2smiles(compound, beam=1)
                    print("smiles_pred ", smiles_pred[0])
                    pts.append(smiles_pred[0])
                except Exception as E:
                    print(E)
                    continue

    print(rts)
    rxn = ".".join(rts)+">>"+".".join(pts)
    print(rxn)
    #
    #
    #

