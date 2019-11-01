from bert_serving.client import BertClient
bc = BertClient()
import numpy as np
import pandas as pd

# 'words' corresponds to the S&P 500 companies on Feb 2019.
#words = ['314808', '78239', '19617', '1035267', '704051', '914208', '1567892', '1087423', '1000697', '1137789', '707549', '920760', '1378946', '908255', '1039101', '1001250', '1070412', '87347', '728535', '899689', '1021860', '97745', '12659', '879101', '106535', '1578845', '58492', '10795', '875045', '740260', '1024478', '1163165', '12927', '750556', '808362', '315189', '764180', '788784', '899866', '310158', '1633917', '10456', '713676', '1666700', '1326801', '766704', '800459', '1274494', '732712', '769397', '1045609', '203527', '1571949', '886158', '6281', '865752', '92230', '1324424', '882835', '31462', '764622', '1065088', '812074', '77360', '1326380', '37785', '1645590', '1048695', '1041061', '1281761', '92122', '1015780', '277948', '49071', '36270', '72207', '816284', '51143', '1442145', '64803', '858877', '313616', '1613103', '47111', '1060391', '1022079', '822416', '1267238', '831001', '73124', '63908', '746515', '1070750', '27419', '14693', '20286', '827054', '935703', '721683', '882095', '1174922', '47217', '764478', '9389', '1014473', '4977', '1739940', '832988', '315852', '896159', '1099800', '89800', '1800', '1053507', '80661', '773910', '797468', '78814', '2969', '731766', '28412', '100493', '60667', '895126', '55067', '6951', '1489393', '1113169', '1099219', '1359841', '319201', '1116132', '36104', '1403161', '1140859', '851968', '4962', '1623613', '815097', '745732', '49826', '91440', '927653', '51434', '1050915', '97476', '773840', '1065280', '833444', '1105705', '1551152', '1285785', '31791', '866787', '107263', '93751', '821189', '1707925', '42582', '18926', '754737', '277135', '915389', '1308161', '1564708', '1324404', '50863', '109380', '1136893', '93410', '352915', '320335', '96021', '1437107', '1058090', '1396009', '93556', '1526520', '1101215', '1038357', '1156039', '49196', '1090872', '1555280', '1090727', '75362', '1108524', '85961', '55785', '1521332', '202058', '1058290', '1579241', '98246', '316709', '875320', '46080', '1467858', '1039684', '718877', '1530721', '811156', '896878', '796343', '4904', '865436', '14272', '106640', '1373835', '1130310', '26172', '1385157', '72333', '1652044', '79879', '96223', '885639', '1466258', '100885', '1032208', '1593034', '1067983', '354908', '885725', '109198', '886982', '63276', '27904', '922864', '5513', '59558', '51644', '54480', '1020569', '1110803', '1506307', '860730', '827052', '1013871', '4127', '38777', '1133421', '916076', '1510295', '40533', '66740', '1124198', '909832', '1770450', '715957', '816761', '920148', '1043604', '39911', '39899', '29905', '62709', '1339947', '350698', '1585364', '91419', '32604', '50104', '77476', '1141391', '927066', '1075531', '7332', '37996', '849399', '1452575', '46765', '1637459', '1341439', '72971', '24545', '794323', '813828', '29534', '80424', '1393612', '916365', '1593538', '791519', '33185', '717423', '895421', '936340', '920522', '875159', '40987', '1037540', '24741', '936468', '732717', '6201', '1451505', '723254', '104169', '743988', '1361658', '59478', '1467373', '1326160', '804328', '915912', '65984', '1744489', '912615', '1137411', '40545', '23217', '1109357', '310764', '315213', '1040971', '906107', '5272', '106040', '721371', '1037868', '701985', '318154', '18230', '1534701', '1090012', '92380', '101829', '200406', '861878', '68505', '1051470', '820027', '51253', '70318', '1047862', '1413329', '313927', '765880', '1018724', '7084', '1365135', '1004434', '820313', '1000228', '1045810', '100517', '315293', '9892', '1170010', '884887', '33213', '48465', '793952', '1121788', '927628', '52988', '4447', '64040', '753308', '1604778', '1551182', '1156375', '1002047', '1730168', '70858', '1126328', '891024', '789019', '726728', '1110783', '783325', '1601712', '1393311', '1011006', '1164727', '1646383', '1137774', '1035002', '723531', '16732', '1086222', '1140536', '21076', '794367', '1043277', '1031296', '1168054', '103379', '62996', '1002910', '72903', '912750', '63754', '1059556', '56873', '1364742', '21344', '21665', '1012100', '1063761', '949039', '73309', '60086', '1048286', '91576', '898173', '899051', '1336917', '702165', '712515', '858470', '791907', '1532063', '1275283', '40704', '1103982', '872589', '804753', '882184', '1101239', '1037038', '356028', '8670', '45012', '874761', '940944', '1650107', '8818', '1115222', '823768', '1048911', '1122304', '76334', '320193', '29989', '34088', '883569', '874766', '1158449', '30625', '1047122', '922224', '798354', '1618921', '320187', '72741', '1067701', '16918', '217346', '1166691', '1492633', '354950', '912242', '1430602', '815556', '1138118', '86312', '101778', '78003', '818479', '831259', '1524472', '6769', '1111711', '35527', '30554', '1120193', '723125', '1732845', '1390777', '1004980', '20520', '877890', '1136869', '814453', '829224']
words = ['2969', '4127', '4447', '4904', '4962', '4977', '5272', '5513', '6201', '6281', '6769', '6951', '7084', '8670', '8818', '9389', '10456', '10795', '12659', '12927', '14272', '14693', '16732', '16918', '18230', '18926', '19617', '20286', '21076', '21344', '21665', '23217', '24545', '24741', '26172', '27419', '27904', '28412', '29534', '29905', '29989', '30625', '31462', '31791', '32604', '33185', '34088', '35527', '36104', '36270', '37785', '37996', '38777', '39911', '40533', '40545', '40704', '40987', '45012', '46080', '46765', '47111', '47217', '48465', '49071', '49196', '49826', '50863', '51143', '51253', '51434', '51644', '52988', '54480', '55067', '55785', '56873', '58492', '59478', '59558', '60086', '60667', '62709', '62996', '63754', '63908', '64040', '64803', '65984', '66740', '68505', '70858', '72207', '72333', '72741', '72903', '72971', '73124', '73309', '75362', '76334', '77360', '77476', '78003', '78239', '79879', '80424', '80661', '86312', '87347', '89800', '91419', '91440', '91576', '92122', '92230', '92380', '93410', '93556', '93751', '96021', '96223', '97476', '97745', '98246', '100493', '100517', '100885', '101778', '101829', '103379', '104169', '106040', '106535', '106640', '107263', '109198', '109380', '200406', '203527', '217346', '277135', '277948', '310158', '310764', '313616', '313927', '315189', '315213', '315293', '316709', '318154', '319201', '320187', '320193', '352915', '354908', '354950', '701985', '702165', '707549', '712515', '713676', '715957', '718877', '721371', '723125', '723254', '723531', '726728', '728535', '731766', '732712', '732717', '740260', '743988', '745732', '746515', '750556', '753308', '764180', '764478', '764622', '765880', '766704', '769397', '773840', '783325', '788784', '789019', '793952', '794367', '796343', '797468', '798354', '804328', '804753', '811156', '813828', '814453', '815097', '815556', '816284', '818479', '820027', '820313', '821189', '822416', '823768', '827052', '827054', '829224', '831001', '831259', '833444', '849399', '851968', '858470', '858877', '860730', '865752', '866787', '872589', '874761', '874766', '875045', '875320', '877890', '879101', '882095', '882184', '882835', '884887', '885639', '885725', '886982', '895421', '896159', '896878', '898173', '899051', '899689', '899866', '906107', '908255', '909832', '912242', '914208', '915389', '915912', '916076', '916365', '920148', '920522', '920760', '922224', '922864', '927066', '927628', '927653', '935703', '936340', '936468', '940944', '1000228', '1000697', '1001250', '1002047', '1002910', '1004434', '1012100', '1013871', '1014473', '1015780', '1018724', '1020569', '1021860', '1022079', '1024478', '1031296', '1032208', '1035002', '1035267', '1037038', '1037540', '1037868', '1038357', '1039684', '1040971', '1041061', '1043277', '1043604', '1045609', '1045810', '1047122', '1047862', '1048286', '1048695', '1048911', '1050915', '1051470', '1053507', '1058090', '1058290', '1059556', '1060391', '1063761', '1065088', '1065280', '1067701', '1067983', '1070750', '1075531', '1086222', '1090012', '1090727', '1090872', '1099219', '1099800', '1101215', '1101239', '1103982', '1108524', '1109357', '1110803', '1111711', '1113169', '1116132', '1120193', '1121788', '1126328', '1130310', '1133421', '1136869', '1136893', '1137774', '1137789', '1138118', '1140536', '1140859', '1141391', '1156039', '1156375', '1158449', '1163165', '1164727', '1166691', '1168054', '1170010', '1174922', '1267238', '1281761', '1285785', '1324404', '1324424', '1326160', '1326801', '1336917', '1339947', '1341439', '1359841', '1364742', '1365135', '1378946', '1385157', '1390777', '1393311', '1393612', '1396009', '1403161', '1413329', '1437107', '1442145', '1466258', '1467373', '1467858', '1489393', '1492633', '1506307', '1510295', '1521332', '1524472', '1526520', '1530721', '1534701', '1551152', '1551182', '1555280', '1564708', '1571949', '1578845', '1579241', '1585364', '1601712', '1604778', '1613103', '1618921', '1623613', '1633917', '1637459', '1645590', '1652044', '1707925', '1730168', '1732845', '1739940', '1744489', '1770450']
ticker = ['APD', 'SWKS', 'HES', 'AEP', 'AXP', 'AFL', 'AIG', 'UNM', 'AAL', 'ADI', 'APA', 'AMAT', 'ADM', 'ADP', 'AVY', 'BLL', 'BAX', 'BDX', 'HRB', 'BA', 'BMY', 'BF.B', 'CPB', 'STZ', 'CAT', 'CTL', 'JPM', 'CINF', 'CLX', 'KO', 'CL', 'CAG', 'TAP', 'GLW', 'CMI', 'TGT', 'DAL', 'CMA', 'DG', 'DOV', 'OMC', 'FLS', 'ECL', 'PKI', 'EMR', 'EFX', 'XOM', 'FITB', 'USB', 'MTB', 'FMC', 'F', 'BEN', 'GPS', 'GD', 'GE', 'GIS', 'GPC', 'HAL', 'HAS', 'HP', 'HSY', 'HPQ', 'HRL', 'HUM', 'HBAN', 'ITW', 'INTC', 'IBM', 'IFF', 'IP', 'IPG', 'JEC', 'KSU', 'K', 'KMB', 'KR', 'LEG', 'LLY', 'LNC', 'L', 'LOW', 'MMC', 'MAS', 'MKC', 'MCD', 'SPGI', 'CVS', 'ETR', 'MMM', 'MSI', 'BAC', 'NBL', 'JWN', 'ES', 'XEL', 'WFC', 'NTRS', 'NUE', 'PCAR', 'PH', 'PNR', 'PEP', 'PFE', 'PVH', 'PPG', 'PG', 'PGR', 'TRV', 'SLB', 'SHW', 'SJM', 'SNA', 'KEY', 'SO', 'BBT', 'LUV', 'CVX', 'SWK', 'STT', 'SYY', 'JEF', 'TXN', 'TMO', 'TIF', 'TSN', 'UAL', 'UNP', 'MRO', 'UTX', 'VFC', 'WMT', 'WDC', 'WY', 'WHR', 'WMB', 'TJX', 'ZION', 'JNJ', 'VAR', 'TXT', 'GWW', 'CSX', 'MRK', 'SYK', 'DHR', 'CHD', 'DE', 'RHI', 'AON', 'SCHW', 'AMGN', 'KLAC', 'NKE', 'AAPL', 'UHS', 'FLIR', 'HD', 'LB', 'NSC', 'LRCX', 'EA', 'PNC', 'D', 'ATVI', 'CAH', 'MU', 'CTAS', 'PAYX', 'O', 'JBHT', 'UNH', 'VZ', 'T', 'VTR', 'XLNX', 'ROST', 'EXPD', 'STI', 'NEE', 'MO', 'BBY', 'PNW', 'HCP', 'WELL', 'ADSK', 'HON', 'WEC', 'PEG', 'MSFT', 'HOG', 'M', 'ADBE', 'OXY', 'FISV', 'QCOM', 'CERN', 'CMS', 'CBS', 'NWL', 'CCL', 'FAST', 'CELG', 'XRAY', 'AMP', 'APH', 'EOG', 'PHM', 'WM', 'EIX', 'MCHP', 'SBUX', 'C', 'FCX', 'JCI', 'SYMC', 'MHK', 'COG', 'CSCO', 'HCA', 'MNST', 'AZO', 'REGN', 'AES', 'HIG', 'BIIB', 'VRTX', 'CTXS', 'KIM', 'GILD', 'DHI', 'ROP', 'RCL', 'KSS', 'BSX', 'GS', 'MS', 'CB', 'INTU', 'ORLY', 'ALL', 'VNO', 'ALXN', 'EQR', 'BWA', 'COST', 'MAC', 'IVZ', 'EMN', 'AVB', 'MLM', 'TSCO', 'LH', 'ESS', 'LEN', 'PPL', 'AIV', 'DVA', 'COF', 'MCK', 'DLTR', 'DTE', 'LMT', 'DRI', 'HSIC', 'WAT', 'EL', 'NTAP', 'AEE', 'AMG', 'SEE', 'NRG', 'VRSN', 'ETFC', 'AMZN', 'IRM', 'NOV', 'DGX', 'ROK', 'FE', 'SRE', 'VLO', 'ISRG', 'RL', 'BXP', 'AME', 'PXD', 'OKE', 'SLG', 'YUM', 'CHRW', 'JNPR', 'PLD', 'NVDA', 'RTN', 'ED', 'MAR', 'FFIV', 'FDX', 'PWR', 'CCI', 'AMT', 'CMG', 'CTSH', 'MCO', 'RSG', 'SPG', 'EBAY', 'NFLX', 'URI', 'BRK.B', 'HST', 'BKNG', 'AKAM', 'DVN', 'UPS', 'A', 'MET', 'EW', 'ADS', 'EQIX', 'MDLZ', 'CRM', 'EXC', 'ILMN', 'NI', 'TROW', 'TPR', 'NDAQ', 'GRMN', 'PFG', 'CNP', 'NOC', 'ZBH', 'FIS', 'PRU', 'STX', 'CBRE', 'WLTW', 'ABC', 'MA', 'ANTM', 'CME', 'AAP', 'COP', 'NEM', 'CMCSA', 'XEC', 'KMX', 'WYNN', 'AIZ', 'RF', 'MOS', 'CF', 'EXPE', 'DUK', 'FB', 'UAA', 'VIAB', 'ORCL', 'HBI', 'BLK', 'WU', 'PBCT', 'TEL', 'BK', 'PSA', 'DFS', 'VMC', 'V', 'PM', 'DISCA', 'VRSK', 'IR', 'ACN', 'GM', 'LYB', 'NLSN', 'KMI', 'MPC', 'APTV', 'XYL', 'TRIP', 'CPRI', 'PSX', 'ABBV', 'ETN', 'ZTS', 'NWSA', 'ICE', 'AGN', 'ALLE', 'PRGO', 'SYF', 'QRVO', 'MDT', 'WBA', 'MYL', 'PYPL', 'KHC', 'HPE', 'GOOGL', 'LIN', 'AVGO', 'WRK', 'CI', 'DIS', 'XRX']

# Enter the target company
query = "320193"
query_vec = bc.encode([query])[0]
doc_vecs = bc.encode(words)
score = np.sum(query_vec * doc_vecs, axis=1) / np.linalg.norm(doc_vecs, axis=1)

# Top 10 related firms
topk_idx = np.argsort(score)[::-1][:11]

for i in range(len(topk_idx)):
    print(ticker[topk_idx[i]])
