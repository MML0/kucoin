import time , requests , datetime


link="https://api.kucoin.com/api/v1/market/orderbook/level1?symbol="#BTC-USDT"

t=time.time()

all_data = [] 
csv_data = ''

coins=['BTC', 'ETH', 'BNB', 'XRP', 'BUSD', 'ADA', 'DOGE']#, 'SOL', 'MATIC', 'DOT', 'SHIB', 'LTC', 'TRX', 'AVAX', 'UNI', 'ATOM', 'LINK', 'XMR', 'ETC', 'TON', 'BCH', 'BCHSV', 'XLM', 'NEAR', 'CRO', 'LDO', 'APE', 'HBAR', 'FIL', 'ALGO', 'QNT', 'VET', 'ICP', 'MANA', 'AAVE', 'SAND', 'FLOW', 'EOS', 'LUNC', 'EGLD', 'XTZ', 'THETA', 'FTM', 'AXS', 'CHZ', 'USDP', 'HT', 'FXS', 'KCS', 'FTT', 'ZEC', 'GRT', 'BTT', 'USDD', 'CRV', 'MKR', 'SNX', 'CAKE', 'TWT', 'KLAY', 'XEC', 'RUNE', 'DASH', 'IOTA', 'NEO', 'OP', 'PAXG', 'IMX', 'ETHW', 'ZIL', 'ENJ', 'HNT', 'GMX', 'OSMO', 'KAVA', 'CSPR', '1INCH', 'COMP', 'CVX', 'LRC', 'RPL', 'BAT', 'STX', 'RVN', 'XDC', 'WOO', 'CELO', 'XEM', 'BAL', 'AR', 'ENS', 'KSM', 'GMT', 'ROSE', 'SUSHI', 'TFUEL', 'DCR', 'MV', 'XCH', 'DFI', 'YFI', 'LUNA', 'IOTX', 'DYDX', 'AGIX', 'WAVES', 'XCN', 'XYM', 'KDA', 'JASMY', 'ANKR', 'BNX', 'ONE', 'GLMR', 'GLM', 'USTC', 'JST', 'AMP', 'MASK', 'QTUM', 'T', 'FLUX', 'MAGIC', 'OMG', 'ICX', 'OCEAN', 'IOST', 'ELON', 'ONT', 'AUDIO', 'ASTR', 'TEL', 'RNDR', 'RSR', 'LPT', 'BDX', 'DGB', 'BICO', 'SXP', 'SKL', 'STORJ', 'SFP', 'ZEN', 'KNC', 'PEOPLE', 'ZRX', 'BRISE', 'RLC', 'UMA', 'SCRT', 'NFT', 'ANT', 'INJ', 'WEMIX', 'SRM', 'DAO', 'SLP', 'TRIBE', 'CTC', 'WAXP', 'ILV', 'PUNDIX', 'MC', 'CKB', 'ERG', 'XNO', 'API3', 'PYR', 'CELR', 'GAL', 'BAND', 'REQ', 'LOOKS', 'GTC', 'CHR', 'EWT', 'NMR', 'XPRT', 'SYS', 'LSK', 'METIS', 'FX', 'DEXE', 'ALPHA', 'LYXe', 'EVER', 'CTSI', 'WIN', 'ABBC', 'MXC', 'CEEK', 'COTI', 'XYO', 'ARRR', 'NKN', 'ORBS', 'CFG', 'REN', 'SNT', 'ACA', 'BFC', 'DAG', 'PROM', 'BSW', 'POND', 'MLK', 'ORC', 'RACA', 'UOS', 'VRA', 'WRX', 'REEF', 'VLX', 'CVC', 'STG', 'MNW', 'ALICE', 'DERO', 'MBOX', 'MTL', 'PHA', 'UQC', 'OGN', 'WMT', 'FET', 'DENT', 'POWR', 'ACH', 'CFX', 'TRAC', 'TLM', 'SPELL', 'OXT', 'BNT', 'DODO', 'SUN', 'MFT', 'DAR', 'AERGO', 'CQT', 'AMPL', 'ELF', 'FORTH', 'REP', 'MOVR', 'C98', 'EFI', 'RLY', 'DIVI', 'QKC', 'DUSK', 'YGG', 'SFUND', 'CCD', 'PERP', 'MTRG', 'MBL', 'ADS', 'CWEB', 'VEGA', 'ETN', 'QRDO', 'XCAD', 'MLN', 'UFO', 'BLOK', 'COCOS', 'REV', 'ASD', 'TIME', 'UTK', 'AOG', 'ARPA', 'SUPER', 'TT', 'FITFI', 'ATA', 'LIT', 'POLS', 'LOKA', 'GODS', 'STMX', 'GAFI', 'TLOS', 'WILD', 'WXT', 'BOBA', 'KMD', 'ALPACA', 'CULT', 'TVK', 'STRK', 'LTO', 'AVA', 'NOIA', 'TRU', 'LINA', 'KAI', 'BOND', 'DIA', 'EXRD', 'ORN', 'AKT', 'ERN', 'FORT', 'DATA', 'AIOZ', 'XPR', 'QUICK', 'CLV', 'ALPINE', 'GAS', 'LON', 'H2O', 'KLV', 'WAN', 'KP3R', 'DEGO', 'AURORA', 'QI', 'TRB', 'FSN', 'SWEAT', 'IDEX', 'BOSON', 'BCD', 'ROUTE', 'ALBT', 'VXV', 'UNFI', 'BAKE', 'HARD', 'RMRK', 'EPX', 'AGLD', 'XHV', 'CREAM', 'VOXEL', 'HERO', 'BURGER', 'OM', 'ADX', 'FIDA', 'ALEPH', 'SDAO', 'AMB', 'KEY', 'ELA', 'CRPT', 'PRQ', 'MAP', 'FRONT', 'ANC', 'SOS', 'PLU', 'PRE', 'SOUL', 'HEGIC', 'NULS', 'HTR', 'VELO', 'DC', 'KAR', 'SUKU', 'DG', 'OPUL', 'ZCX', 'STC', 'AKRO', 'DERC', 'CPOOL', 'SOLVE', 'HYDRA', 'OOKI', 'HAPI', 'GST', 'NAKA', 'MIR', 'RFOX', 'BEPRO', 'ALT', 'PNT', 'NIM', 'BOA', 'PDEX', 'YLD', 'SENSO', 'CERE', 'URUS', 'KRL', 'KOK', 'GARI', 'VEED', 'APL', 'XDEFI', 'DPR', 'SDN', 'PKF', 'OXEN', 'GOVI', 'LSS', 'NWC', 'NRG', 'BASIC', 'CUDOS', 'PUSH', 'LTX', 'TONE', 'HAI', 'WHALE', 'ORAI', 'XDB', 'PEEL', 'IHC', 'TITAN', 'KAT', 'FRA', 'SCLP', 'SHR', 'XED', 'NUM', 'PSTAKE', 'VR', 'ZBC', 'SWASH', 'GRIN', 'PCX', 'SPA', 'WNCG', 'POSI', 'OVR', 'NTVRK', 'EPIK', 'AURY', 'REAP', 'BUX', 'SHFT', 'SYLO', 'BNC', 'SHILL', 'GHX', 'CMP', 'NEER', 'DFYN', 'BONDLY', 'XAVA', 'KMA', 'SWFTC', 'POLK', 'DRGN', 'WOOP', 'DYP', 'GOM2', 'MTV', 'CARD', 'MAN', 'SLIM', 'UNO', 'CIRUS', 'CAS', 'PBR', 'DVPN', 'PSL', 'CGG', 'MOOV', 'GMM', 'TRVL', 'XTM', 'OGV', 'TRIAS', 'OOE', 'KYL', 'BAX', 'REVV', 'VID', 'EDG', 'FKX', 'GMEE', 'MITX', 'DFA', 'BIFI', 'VAI', 'SKEY', 'WOM', 'VEMP', 'LITH', 'VSYS', 'GLCH', 'SHX', 'JAM', 'EFX', 'GEEQ', 'COV', 'TARA', 'BOLT', 'ENQ', 'MODEFI', 'MHC', 'WSIENNA', 'IXS', 'BRWL', 'PMON', 'GLQ', 'DSLA', 'SRK', 'FRM', 'SIN', 'TOWER', 'SWINGBY', 'TRADE', 'UBX', 'AOA', 'SHA', 'CTI', 'UNIC', 'MAHA', 'MATTER', 'ISP', 'EOSC', 'RFUEL', 'KONO', 'TXA', 'PIAS', 'POLC', 'FLY', 'SLCL', 'XWG', 'LYM', 'WELL', 'LAYER', 'ZEE', 'REVU', 'NORD', 'BULL', 'OLT', 'SWP', 'TOKO', 'UNB', 'ACE', 'FCD', 'ACT', 'LABS', 'ERTHA', 'EPK', 'EQZ', 'NGM', 'NRFB', 'FEAR', 'XCV', 'SUTER', 'CWS', 'FLAME', 'MONI', 'BEAT', 'GMB', 'CPC', 'MARSH', 'ROOBEE', 'ONSTON', 'PLY', 'IOI', 'WEST', 'PHNX', 'XNL', 'OLE', 'WOMBAT', 'HOTCROSS', 'STRONG', 'HORD', 'ODDZ', 'DPET', 'BMON', 'NFTB', 'LIKE', 'HAWK', 'OPCT', 'LOCG', 'SKU', 'XTAG', 'KDON', 'LBP', 'HYVE', 'ARX', 'MNST', 'PUMLX', 'BUY', 'PBX', 'MTS', 'ROSN', 'LACE', 'PLAY', 'FTG', 'XCUR', 'JAR', 'STND', 'POLX', 'TCP', 'DAPPX', 'MVP', 'FRR', 'PEL', 'LAVAX', 'NAVI', '1EARTH', 'ADB', 'YOP', '2CRZ', 'XSR', 'TIDAL', 'IDEA', 'MAKI', 'HAKA', 'RED', 'FORM', 'FCL', 'FCON', 'CREDI', 'VISION', 'GEM', 'ROAR', 'CARE', 'BBC', 'SDL', 'YFDAI', 'FLR', 'AXPR', 'OAS', 'HIDOODLES', 'HIFIDENZA', 'HIMFERS', 'SON', 'CELT', 'BNS', 'ETH2', 'HIENS3', 'HIENS4', 'COOHA', 'GALA', 'SYNR', 'KICKS', 'VIDT', 'CAPP', 'HIVALHALLA', 'MELOS', 'HISQUIGGLE', 'GENS', 'ECOx', 'GGG', 'KOL', 'DAPPT', 'P00LS', 'CWAR', 'PLGR', 'TRIBL', 'ARKER', 'TEM', 'SURV', 'STORE', 'DREAMS', 'DMTR', 'RACEFI', 'CLH', 'HICLONEX', 'HIFLUF', 'CIX100', 'PIX', 'aUSD', 'PLD', 'KARA', 'POL', 'MPLX', 'SIMP', 'HBB', 'HIOD', 'SRBP', 'LMR', 'HIPENGUINS', 'HFT', 'LOC', 'AION', 'AI', 'HIAZUKI', 'HIPUNKS', 'FT', 'FORESTPLUS', 'UPO', 'STARLY', 'HIMEEBITS', 'ARNM', 'MEM', 'DOCK', 'MJT', 'EGAME', 'MLS', 'REV3L', 'STEPWATCH', 'PRMX', 'HIBIRDS', 'ILA', 'NHCT', 'ASTRA', 'RBP', 'HEART', 'DOSE', 'INDI', 'NDAU', 'HICOOLCATS', 'ACQ', 'HISAND33', 'PRIMAL', 'CHMB', 'CLUB', 'SQUAD', 'SOLR', 'AFK', 'RIF', 'EQX', 'H3RO3S', 'EUL', 'QUARTZ', 'NGC', 'NGL', 'AZERO', 'ACOIN', 'TAUM', 'APT', 'XETA', 'MNET', 'LPOOL', 'WBTC', 'HIODBS', 'RANKER', 'LOOM', 'WAL', 'MSWAP', 'HIBAYC', 'HIMAYC', 'HIGAZERS', 'LOVE', 'POKT', 'FALCONS', 'MARS4', 'ERSDL', 'NYM']
for i in range (5):
    prices = []
    for j in coins:
        print(j)
        try:
            res = requests.get(link+j+'-USDT')
            ptxt=res.json()['data']["price"]
            prices += [[j,ptxt]]
            csv_data += str(ptxt) + ','
            
        except BaseException as er:
            print(er,res.text)
    csv_data = str(datetime.datetime.now()) + ',' + str(time.time()-t) + ',' + csv_data + '\n'

        
    all_data += [prices,time.time()]
    
csv_data = ' time , time (s),' + str(coins)[1:-1]  + '\n' + csv_data



print(time.time()-t)

'''
a = open('data.txt','w')
a.write(str(coins)+'\n'+str(all_data)) 
a.close
'''
a = open('all_data-api.csv','w')
a.write(csv_data) 
a.close

print(len(coins))
print('set:',len(set(coins)))
#print(coins)
