#####################################################################################################################
#                                               World space data file                                               #
# Probabilities calculated as number of convoys that passed through this square/number of U-Boat encounters in this #
#square for each month from 06/1940 to 06/1941. If a square had any U-Boats in it in a given month, there is an     #
#encounter chance floor of 1%.                                                                                      #
# Data provided by scraping uboat.net and warsailors.com.                                                           #
#####################################################################################################################

from gridSquare import grid_square

AA = grid_square(
    ['AD', 'AH', 'AJ']
)
AD = grid_square(
    ['AJ', 'AK', 'AL', 'AE'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.08, 0.03, 0]
)
AE = grid_square(
    ['AD', 'AL', 'AM', 'AN', 'AF'],
    encounterProb=[0, 0, 0.03, 0.03, 0, 0.03, 0.04, 0.03, 0.10, 0.11, 0.09, 0.08, 0.03]
)
AF = grid_square(
    ['AE', 'AN'],
    encounterProb=[0, 0.04, 0.10, 0.07, 0.04, 0.05, 0.04, 0.03, 0.07, 0.06, 0.06, 0.08, 0.03]
)
AH = grid_square(
    ['AA', 'AH', 'AJ', 'BB'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01]
)
AJ = grid_square(
    ['AA', 'AH', 'BB', 'BC', 'AK', 'AD'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.09, 0.05]
)
AK = grid_square(
    ['AD', 'AL', 'AJ', 'BC', 'BD'],
    encounterProb=[0, 0, 0.03, 0, 0.02, 0, 0, 0, 0, 0.04, 0.11, 0.13, 0.03]
)
AL = grid_square(
    ['AD', 'AE', 'AK', 'AM', 'BD', 'BE'],
    encounterProb=[0, 0.1, 0.09, 0.16, 0.15, 0.12, 0.13, 0.12, 0.14, 0.15, 0.16, 0.08, 0.04]
)
AM = grid_square(
    ['AE', 'AL', 'AN', 'BE', 'BF'],
    encounterProb=[0.08, 0.17, 0.26, 0.26, 0.18, 0.14, 0.08, 0.09, 0.14, 0.12, 0.08, 0.10, 0.10],
    inUK=True
)
AN = grid_square(
    ['AE', 'AF', 'AM', 'BF'],
    encounterProb=[0.07, 0.13, 0.22, 0.12, 0.10, 0.09, 0.05, 0.03, 0.13, 0.09, 0.09, 0.12, 0.03],
    inUK=True
)
BA = grid_square (
    ['BB', 'CA', 'CB']
)
BB = grid_square(
    ['AH', 'AJ', 'BA', 'BC', 'CB', 'CC']
)
BC = grid_square(
    ['AJ', 'AK', 'BB', 'BD', 'CC', 'CD'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.03, 0.08]
)
BD = grid_square(
    ['AK', 'AL', 'BC', 'BE', 'CD', 'CE', 'CF'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0.04, 0.09]
)
BE = grid_square(
    ['AL', 'AM', 'BD', 'BF', 'CF', 'CG'],
    encounterProb=[0.09, 0.10, 0.06, 0.14, 0.14, 0.10, 0.11, 0.10, 0.11, 0.13, 0.13, 0.19, 0.13]
)
BF = grid_square(
    ['AM', 'AN', 'BE', 'CG'],
    encounterProb=[0.08, 0.14, 0.20, 0.26, 0.28, 0.14, 0.13, 0.15, 0.18, 0.19, 0.24, 0.24, 0.13]
)
CA = grid_square(
    ['BA', 'CB', 'DC']
)
CB = grid_square(
    ['BA', 'BB', 'CA', 'CC', 'DC', 'DD']
)
CC = grid_square(
    ['BB', 'BC', 'CB', 'CC', 'DC', 'DD'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.02]
)
CD = grid_square(
    ['BC', 'BD', 'CC', 'CE', 'DE', 'DF'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.02]
)
CE = grid_square(
    ['BD', 'CD', 'CF', 'DF', 'DG'],
    encounterProb=[0, 0, 0, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0]
)
CF = grid_square(
    ['BE', 'CE', 'CG', 'DG', 'DH'],
    encounterProb=[0, 0.01, 0.03, 0, 0.01, 0, 0.01, 0.01, 0, 0.01, 0.04, 0.01, 0.03]
)
CG = grid_square(
    ['BE', 'BF', 'CF', 'DH', 'DJ'],
    encounterProb=[0.02, 0.02, 0, 0, 0, 0, 0.01, 0.03, 0.02, 0.01, 0.05, 0, 0.03]
)
DA = grid_square(
    ['DB', 'DK', 'DL']
)
DB = grid_square(
    ['DA', 'DC', 'DL', 'DM']
)
DC = grid_square(
    ['CA', 'CB', 'DB', 'DD', 'DM', 'DN', 'DO']
)
DD = grid_square(
    ['CB', 'CC', 'DC', 'DE', 'DO', 'DP']
)
DE = grid_square(
    ['CC', 'CD', 'DD', 'DF', 'DP', 'DQ']
)
DF = grid_square(
    ['CD', 'CE', 'DE', 'DG', 'DQ', 'DR', 'DS']
)
DG = grid_square(
    ['CE', 'CF', 'DF', 'DH', 'DS', 'DT'],
    encounterProb=[0, 0, 0, 0, 0.01, 0, 0.01, 0, 0, 0, 0.02, 0.01, 0.01]
)
DH = grid_square(
    ['CF', 'CG', 'DG', 'DJ', 'DT', 'DU'],
    encounterProb=[0.01, 0.01, 0.01, 0, 0, 0, 0.01, 0.01, 0.01, 0.03, 0.04, 0, 0.04]
)
DJ = grid_square(
    ['CG', 'DH', 'DU'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0.01, 0, 0, 0]
)
DK = grid_square(
    ['DA', 'DB', 'DK', 'DL']
)
DL = grid_square(
    ['DA', 'DB', 'DK', 'DM', 'EA', 'EB']
)
DM = grid_square(
    ['DB', 'DC', 'DL', 'DN', 'EB']
)
DN = grid_square(
    ['DC', 'DM', 'DO', 'EC']
)
DO = grid_square(
    ['DC', 'DD', 'DN', 'DP', 'ED']
)
DP = grid_square(
    ['DD', 'DE', 'DO', 'DQ', 'EE']
)
DQ = grid_square(
    ['DE', 'DF', 'DP', 'DR', 'EF']
)
DR = grid_square(
    ['DF', 'DQ', 'DS', 'EG']
)
DS = grid_square(
    ['DF', 'DG', 'DR', 'DT', 'EH'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.04]
)
DT = grid_square(
    ['DG', 'DH', 'DS', 'DU', 'EJ'],
    encounterProb=[0, 0.03, 0.01, 0, 0.01, 0, 0, 0.01, 0, 0.03, 0.02, 0.01, 0.06]
)
DU = grid_square(
    ['DH', 'DJ', 'DT', 'EK'],
    encounterProb=[0, 0.01, 0, 0, 0.01, 0, 0.01, 0.01, 0, 0.02, 0.02, 0, 0]
)
EA = grid_square(
    ['DL', 'EB', 'DM']
)
EB = grid_square(
    ['DM', 'EA', 'EC', 'EL', 'DL', 'DN']
)
EC = grid_square(
    ['DN', 'EB', 'ED', 'DM', 'DO', 'EL']
)
ED = grid_square(
    ['DO', 'EC', 'EE', 'DN', 'DP']
)
EE = grid_square(
    ['DP', 'ED', 'EF', 'EO', 'DO', 'DQ']
)
EF = grid_square(
    ['DQ', 'EE', 'EG', 'EP', 'DP', 'DR', 'EO', 'EQ']
)
EG = grid_square(
    ['DR', 'EF', 'EH', 'EQ', 'DQ', 'DS', 'EP', 'ER']
)
EH = grid_square(
    ['DS', 'EG', 'EJ', 'ER', 'DR', 'DT', 'EQ', 'ES'],
    encounterProb=[0, 0.01, 0, 0, 0, 0.01, 0, 0, 0, 0, 0.02, 0.03, 0.06]
)
EJ = grid_square(
    ['DT', 'EK', 'EH', 'ES', 'DS', 'DU', 'ER', 'ET'],
    encounterProb=[0, 0.01, 0.10, 0, 0, 0.01, 0.02, 0.01, 0, 0.03, 0.03, 0.03, 0.03]
)
EK = grid_square(
    ['DU', 'EJ', 'ET', 'DT', 'ES'],
    encounterProb=[0, 0, 0, 0, 0.01, 0, 0, 0, 0, 0.02, 0, 0, 0.01]
)
EL = grid_square(
    ['EB', 'EC']
)
EO = grid_square(
    ['EE', 'EP', 'ED', 'EF']
)
EP = grid_square(
    ['EF', 'EO', 'EQ', 'FA', 'FB', 'EE', 'EG']
)
EQ = grid_square(
    ['EG', 'ER', 'EP', 'FB', 'EF', 'EH', 'FA', 'FC']
)
ER = grid_square(
    ['EH', 'EQ', 'ES', 'FC', 'EG', 'EJ', 'FB', 'FD'],
    encounterProb=[0, 0.01, 0, 0, 0, 0.01, 0.01, 0, 0, 0.03, 0.02, 0.06, 0.04]
)
ES = grid_square(
    ['ER', 'EJ', 'ET', 'FD', 'EH', 'EK', 'FC', 'FE'],
    encounterProb=[0, 0.01, 0, 0, 0, 0.01, 0.01, 0, 0, 0.01, 0.02, 0.05, 0.03]
)
ET = grid_square(
    ['EK', 'ES', 'FE', 'EU', 'EJ', 'FD', 'FF'],
    encounterProb=[0, 0.05, 0.05, 0, 0.05, 0.05, 0.05, 0, 0, 0.010, 0.10, 0.25, 0.20]
)
EU = grid_square(
    ['ET', 'EV', 'FE', 'FF', 'FG'],
    encounterProb=[0, 0, 0, 0, 0, 0.03, 0, 0, 0, 0, 0, 0.03, 0.03]
)
EV = grid_square(
    ['EU', 'EW', 'FF', 'FG', 'FH'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.02, 0.02]
)
EW = grid_square(
    ['EV', 'FG', 'FH']
)
FA = grid_square(
    ['EP', 'EQ', 'FB']
)
FB = grid_square(
    ['EP', 'EQ', 'ER', 'FA', 'FC']
)
FC = grid_square(
    ['EQ', 'ER', 'ES', 'FB', 'FD', 'FJ'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0.01, 0, 0, 0.01, 0.02, 0.01, 0]
)
FD = grid_square(
    ['ER', 'ES', 'ET', 'FC', 'FE', 'FK', 'FL'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0.01, 0, 0, 0, 0.02, 0, 0]
)
FE = grid_square(
    ['ES', 'ET', 'EU', 'FD', 'FF', 'FL', 'FM'],
    encounterProb=[0, 0, 0, 0, 0, 0.01, 0, 0, 0, 0, 0, 0, 0]
)
FF = grid_square(
    ['ET', 'EU', 'EV', 'FE', 'FG', 'FM', 'FN'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01]
)
FG = grid_square(
    ['EU', 'EV', 'EW', 'FF', 'FH', 'FN', 'FO'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0]
)
FH = grid_square(
    ['EV', 'EW', 'FG', 'FO', 'FP']
)
FJ = grid_square(
    ['FB', 'FC', 'FK', 'FQ', 'FR'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0]
)
FK = grid_square(
    ['FC', 'FD', 'FJ', 'FL', 'FQ', 'FR', 'FS'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.02, 0, 0]
)
FL = grid_square(
    ['FD', 'FE', 'FK', 'FM', 'FR', 'FS', 'FT'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0, 0]
)
FM = grid_square(
    ['FE', 'FF', 'FL', 'FN', 'FS', 'FT', 'FU']
)
FN = grid_square(
    ['FF', 'FG', 'FM', 'FO', 'FT', 'FU', 'FV']
)
FO = grid_square(
    ['FG', 'FH', 'FN', 'FP', 'FU', 'FV', 'FX']
)
FP = grid_square(
    ['FH', 'FO', 'FV', 'FX']
)
FQ = grid_square(
    ['FJ', 'FK', 'FR'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0.01, 0]
)
FR = grid_square(
    ['FJ', 'FK', 'FL', 'FQ', 'FS'],
    encounterProb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0, 0]
)
FS = grid_square(
    ['FK', 'FL', 'FM', 'FR', 'FT']
)
FT = grid_square(
    ['FL', 'FM', 'FN', 'FS', 'FU']
)
FU = grid_square(
    ['FM', 'FN', 'FO', 'FT', 'FV']
)
FV = grid_square(
    ['FN', 'FO', 'FP', 'FU', 'FX']
)
FX = grid_square(
    ['FO', 'FP', 'FV']
)

world = {'AA' : AA, 'AD' : AD, 'AE' : AE, 'AF' : AF, 'AH' : AH, 'AJ': AJ, 'AK': AK, 'AL' : AL, 'AM' : AM, 'AN' : AN,
         'BA' : BA, 'BB' : BB, 'BC' : BC, 'BD' : BD, 'BE' : BE, 'BF' : BF, 'CA' : CA, 'CB' : CB, 'CC' : CC, 'CD' : CD,
         'CE' : CE, 'CF' : CF, 'CG' : CG, 'DA' : DA, 'DB' : DB, 'DC' : DC, 'DD' : DD, 'DE' : DE, 'DF' : DF, 'DG' : DG,
         'DH' : DH, 'DJ' : DJ, 'DK' : DK, 'DL' : DL, 'DM' : DM, 'DN' : DN, 'DO' : DO, 'DP' : DP, 'DQ' : DQ, 'DR' : DR,
         'DS' : DS, 'DT' : DT, 'DU' : DU, 'EA' : EA, 'EB' : EB, 'EC' : EC, 'ED' : ED, 'EE' : EE, 'EF' : EF, 'EG' : EG,
         'EH' : EH, 'EJ' : EJ, 'EK' : EK, 'EL' : EL, 'EO' : EO, 'EP' : EP, 'EQ' : EQ, 'ER' : ER, 'ES' : ES, 'ET' : ET,
         'EU' : EU, 'EV' : EV, 'EW' : EW, 'FA' : FA, 'FB' : FB, 'FC' : FC, 'FD' : FD, 'FE' : FE, 'FF' : FF, 'FG' : FG,
         'FH' : FH, 'FJ' : FJ, 'FK' : FK, 'FL' : FL, 'FM' : FM, 'FN' : FN, 'FO' : FO, 'FP' : FP, 'FQ' : FQ, 'FR' : FR,
         'FS' : FS, 'FT' : FT, 'FU' : FU, 'FV' : FV, 'FX': FX}