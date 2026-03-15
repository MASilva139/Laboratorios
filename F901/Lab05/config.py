# config.py

FILES = {
    'azul': 'F901/Lab05/csv/azul.csv',
    'rojo': 'F901/Lab05/csv/rojo.csv',
    'naranja': 'F901/Lab05/csv/naranja.csv',
    'verde': 'F901/Lab05/csv/verde.csv',
    'violeta': 'F901/Lab05/csv/violeta.csv',
    'referencia': 'F901/Lab05/csv/referencia.csv'
}

# Longitudes de onda.
# Ajusta estos valores si en tu laboratorio usaron otra identificación real.
WAVELENGTHS_NM = {
    'rojo': 620,
    'naranja': 578,
    'verde': 546,
    'azul': 436,
    'violeta': 405
}

C = 299792458               # m/s
E_CHARGE = 1.602176634e-19  # C
H_REAL = 6.62607015e-34     # J*s

COLUMN_MAP = {
    'index': 'n',
    'vf': 'Vf[V]',
    'v_amp': 'V',
    'v_unit': 'V_unit',
    'delta_uv': 'delta[uV]',
    'ic': 'Ic[mA]'
}

DEFAULT_SIGNAL_UNITS = {
    'azul': 'V',
    'rojo': 'mV',
    'naranja': 'mV',
    'verde': 'mV',
    'violeta': 'V',
    'referencia': 'mV'
}