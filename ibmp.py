from pprint import pprint

api_key = ""
from rxn4chemistry import RXN4ChemistryWrapper

rxn4chemistry_wrapper = RXN4ChemistryWrapper(api_key=api_key, base_url='https://rxn.res.ibm.com')
# or set it afterwards
# rxn4chemistry_wrapper = RXN4ChemistryWrapper(api_key=api_key)
# rxn4chemistry_wrapper.set_base_url('https://some.other.rxn.server')

# results = rxn4chemistry_wrapper.paragraph_to_actions(
#     'To a stirred solution of '
#     '7-(difluoromethylsulfonyl)-4-fluoro-indan-1-one (110 mg, '
#     '0.42 mmol) in methanol (4 mL) was added sodium borohydride '
#     '(24 mg, 0.62 mmol). The reaction mixture was stirred at '
#     'ambient temperature for 1 hour.'
# )
""""""
result1 = rxn4chemistry_wrapper.paragraph_to_actions(
"A solution of the resulting 2-(5-phenyl-[1,2,4]oxadiazol-3-yl)-morpholine hydrochloride (intermediate 10 in tetrahydrofuran (6.0 ml) was added with 2-chloro-3-methyl-6-(pyrimidine-4-yl)pyrimidin-4-one (intermediate 1, 260 mg, 2.34 mmol) and triethylamine (1.81 ml, 13.0 mmol), and the reaction mixture was stirred at room temperature for 2 hours. The solution was partitioned between water and chloroform, and the organic layer was washed with water and brine, dried over magnesium sulfate, and concentrated in vacuo. The resulting residue was purified by column chromatography on silica gel (eluent; 5% methanol in chloroform) to afford 1-methyl-2-[2-(5-phenyl-[1,2,4]oxadiazol-3-yl)-morpholin-4-yl]-1H-[4,4′]bipyrimidinyl-6-one (compound 2 in Table 1, 749 mg, 64%, 2 steps) as solid"
)

result2 = rxn4chemistry_wrapper.paragraph_to_actions(
"A mixture of N-benzylethanolamine (intermediate 23, 44.8 ml, 314 mmol) and 2-chloroacrylonitrile (intermediate 24, 25 ml, 314 mmol) was stirred at room temperature for 24 hours. After the mixture was cooled to 0° C., tetrahydrofuran (300 ml) and then potassium tert-butoxide was added to the mixture, and the mixture was stirred at 0° C. for one hour. The mixture was diluted by ethyl ether, and then washed with water and brine and dried over magnesium sulfate. Solvent was removed under reduced pressure, and the residue was purified by silica gel column chromatography (eluent; 5% ethyl acetate in hexane) to afford 4-benzylmorpholine-2-carbonitrile (intermediate 25) as colorless oil."
)


pprint(result1['actions'])
pprint(result2['actions'])

# print(results['actions'])