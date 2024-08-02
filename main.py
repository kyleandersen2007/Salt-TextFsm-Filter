import readmodemdata

modem = '''
adsl: ADSL driver and PHY status
Status: Showtime
Last Retrain Reason:    8000
Last initialization procedure status:   0
Max:    Upstream rate = 6000 Kbps, Downstream rate = 800 Kbps
Bearer: 0, Upstream rate = 11321 Kbps, Downstream rate = 53951 Kbps

Link Power State:       L0
Mode:                   VDSL2 Annex A
VDSL2 Profile:          Profile 12a
TPS-TC:                 PTM Mode(0x0)
Trellis:                U:ON /D:ON
Line Status:            No Defect
Training Status:        Showtime
                Down            Up
SNR (dB):        9.9             6.7
Attn(dB):        8.9             0.0
Pwr(dBm):        14.2           -14.5

                        VDSL2 framing
                        Bearer 0
MSGc:           16              45
B:              239             240
M:              1               1
T:              64              22
R:              0               14
S:              0.1416          0.6764
L:              13560           3016
D:              1               1
I:              240             255
N:              240             255

                        Counters
                        Bearer 0
OHF:            922114295               187923376
OHFErr:         314             1
RS:             0               3811129764
RSCorr:         0               11921
RSUnCorr:       0               0

                        Bearer 0
HEC:            30              0
OCD:            0               0
LCD:            0               0
Total Cells:    2842236023              0
Data Cells:     6561361         0
Drop Cells:     0
Bit Errors:     0               0

ES:             227             2
SES:            0               1
UAS:            86              86
AS:             2097245

                        Bearer 0
INP:            0.00            0.00
INPRein:        0.00            0.00
delay:          0               0
PER:            2.27            11.20
OR:             77.38           36.41
AgR:            54028.94        11357.29

Bitswap:        70/493          220/220
'''

print(readmodemdata.getData(modem))