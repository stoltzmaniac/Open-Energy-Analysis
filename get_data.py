from pyiso import client_factory
import pandas as pd


client = client_factory('EIA')

def bas():
    ba_list = ['AEC', 'AECI', 'AESO', 'AVA', 'AZPS', 'BANC', 'BCTC',
               'BPAT', 'CISO', 'CFE', 'CHPD', 'CISO', 'CPLE', 'CPLW',
               'DEAA', 'DOPD', 'DUK', 'EEI', 'EPE', 'ERCO', 'FMPP',
               'FPC', 'FPL', 'GCPD', 'GRID', 'GRIF', 'GRMA', 'GVL',
               'GWA', 'HGMA', 'HQT', 'HST', 'IESO', 'IID', 'IPCO',
               'ISNE', 'JEA', 'LDWP', 'LGEE', 'MHEB', 'MISO', 'NBSO',
               'NEVP', 'NSB', 'NWMT', 'NYIS', 'OVEC', 'PACE', 'PACW',
               'PGE', 'PJM', 'PNM', 'PSCO', 'PSEI', 'SC', 'SCEG',
               'SCL', 'SEC', 'SEPA', 'SOCO', 'SPA', 'SPC', 'SRP',
               'SWPP', 'TAL', 'TEC', 'TEPC', 'TIDC', 'TPWR', 'TVA',
               'WACM', 'WALC', 'WAUW', 'WWA', 'YAD']
    ba_list_of_dicts = []
    for ba in ba_list:
        tmp = {}
        tmp['label'] = ba
        tmp['value'] = ba
        ba_list_of_dicts.append(tmp)
    return ba_list_of_dicts


def load_forecast(ba):
    client.set_ba(ba)
    data = pd.DataFrame(client.get_load(forecast=True))
    return data

def generation_forecast(ba):
    client.set_ba(ba)
    data = pd.DataFrame(client.get_generation(yesterday=True))
    return data

def generation_split(ba):
    client.set_ba(ba)
    data = pd.DataFrame(client.get_generation(yesterday=True))
    return data



