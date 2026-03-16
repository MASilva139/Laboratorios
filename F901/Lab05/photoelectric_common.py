import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from config import C, E_CHARGE, H_REAL
import os

def save_figure(fig, filename: str, folder: str = 'fig', save_pdf: bool = True, save_html: bool = False):
    os.makedirs(folder, exist_ok=True)
    # os.makedirs("fig", exist_ok=True)
    if save_pdf:
        fig.write_image(f'{folder}/{filename}.pdf')

    if save_html:
        fig.write_html(f'{folder}/{filename}.html')

def load_csv_files(files: dict) -> dict:
    dfs = {name: pd.read_csv(path) for name, path in files.items()}
    for name in dfs:
        dfs[name].columns = [col.strip() for col in dfs[name].columns]
    return dfs

def coerce_numeric_columns(dfs: dict, columns: list) -> dict:
    for name, df in dfs.items():
        for col in columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        dfs[name] = df.copy()
    return dfs

def add_real_stopping_voltage(dfs: dict, vf_col: str, negate_vf: bool = True) -> dict:
    for name, df in dfs.items():
        if negate_vf:
            df['Vf_real[V]'] = -df[vf_col]
        else:
            df['Vf_real[V]'] = df[vf_col]
        dfs[name] = df.copy()
    return dfs

def get_reference_value(df_ref: pd.DataFrame, signal_col: str) -> float:
    return df_ref[signal_col].mean()

def convert_signal_to_volts_from_column(
    df: pd.DataFrame,
    signal_col: str = 'V',
    unit_col: str = 'V_unit',
    output_col: str = 'V_signal[V]',
    default_unit: str | None = None # Se añade para la parte con incertezas
) -> pd.DataFrame:
    df = df.copy()
    def convert(value, unit):
        if pd.isna(value) or pd.isna(unit):
            return np.nan
        unit = str(unit).strip()
        if unit == 'V':
            return value
        elif unit == 'mV':
            return value * 1e-3
        elif unit in ['uV', 'µV']:
            return value * 1e-6
        elif unit == 'nV':
            return value * 1e-9
        elif unit == 'kV':
            return value * 1e+3
        elif unit == 'MV':
            return value * 1e+6
        elif unit == 'GV':
            return value * 1e+9
        else:
            raise ValueError(f'Unidad no reconocida para la señal: {unit}')

    df[output_col] = df.apply(lambda row: convert(row[signal_col], row[unit_col]), axis=1)
    return df

def convert_delta_to_volts(
    df: pd.DataFrame,
    delta_col: str = 'delta[uV]',
    output_col: str = 'delta[V]'
) -> pd.DataFrame:
    df = df.copy()
    if delta_col in df.columns:
        df[output_col] = df[delta_col] * 1e-6
    else:
        df[output_col] = np.nan
    return df

def get_reference_value(df_ref: pd.DataFrame, signal_col: str) -> float:
    return df_ref[signal_col].mean()

def apply_reference_correction(
    dfs: dict,
    colors: list,
    signal_col: str,
    ref_value: float,
    corrected_col: str
) -> dict:
    out = {}
    for color in colors:
        df = dfs[color].copy()
        df[corrected_col] = df[signal_col] - ref_value
        out[color] = df
    return out

def compute_frequencies(wavelengths_nm: dict) -> dict:
    """Convierte longitudes de onda a frecuencia."""
    freq = {}
    for color, lam_nm in wavelengths_nm.items():
        freq[color] = C / (lam_nm * 1e-9)
    return freq

def find_zero_crossing_linear(df: pd.DataFrame, xcol: str, ycol: str) -> float:
    """
    Encuentra el cruce por cero usando interpolación lineal entre dos puntos consecutivos.
    Retorna np.nan si no hay cruce.
    """
    temp = df[[xcol, ycol]].dropna().sort_values(xcol).reset_index(drop=True)
    # df = df.sort_values(xcol).reset_index(drop=True)
    x = df[xcol].values
    y = df[ycol].values
    # for i in range(len(df) - 1):
    for i in range(len(temp) - 1):
        x1, x2 = x[i], x[i + 1]
        y1, y2 = y[i], y[i + 1]
        # if pd.isna(y1) or pd.isna(y2):
        #     continue
        if y1 == 0:
            return x1
        if y2 == 0:
            return x2
        if y1 * y2 < 0:
            return x1 - y1 * (x2 - x1) / (y2 - y1)
    return np.nan

def find_zero_crossing_fit(df: pd.DataFrame, xcol: str, ycol: str, n_points: int = 4) -> float:
    """
    Estima el cruce por cero ajustando una recta a los puntos más cercanos al cero.
    n_points = cantidad de puntos cercanos al cero a usar.
    """
    temp = df[[xcol, ycol]].dropna().copy()
    if len(temp) < 2:
        return np.nan
    temp['abs_signal'] = temp[ycol].abs()
    temp = temp.sort_values('abs_signal').head(n_points).sort_values(xcol)
    if len(temp) < 2:
        return np.nan
    x = temp[xcol].values
    y = temp[ycol].values

    m, b = np.polyfit(x, y, 1)
    if m == 0:
        return np.nan
    return -b / m


def estimate_vstop_and_uncertainty(df: pd.DataFrame, xcol: str, ycol: str, dycol: str, n_points: int = 4):
    """
    Estima el cruce por cero x0 y su incertidumbre aproximada:
        sigma_x0 ~ sigma_y / |m_local|

    Usa los n_points más cercanos al cero.
    """
    temp = df[[xcol, ycol, dycol]].dropna().copy()
    if len(temp) < 2:
        return np.nan, np.nan
    temp['abs_signal'] = temp[ycol].abs()
    temp = temp.sort_values('abs_signal').head(n_points).sort_values(xcol)
    if len(temp) < 2:
        return np.nan, np.nan
    x = temp[xcol].values
    y = temp[ycol].values
    dy = temp[dycol].values
    m, b = np.polyfit(x, y, 1)
    if m == 0:
        return np.nan, np.nan
    x0 = -b / m
    sigma_y = np.mean(dy)
    sigma_x0 = sigma_y / abs(m)
    return x0, sigma_x0

def build_results_table(
        color_dfs: dict, 
        wavelengths_nm: dict, 
        xcol: str, 
        ycol: str, 
        method: str = 'linear'
) -> pd.DataFrame:
    frequencies = compute_frequencies(wavelengths_nm)
    rows = []
    for color, df in color_dfs.items():
        if method == 'linear':
            vstop = find_zero_crossing_linear(df, xcol, ycol)
        elif method == 'fit':
            vstop = find_zero_crossing_fit(df, xcol, ycol)
        else:
            raise ValueError("method debe ser 'linear' o 'fit'")
        rows.append({
            'Color': color,
            'lambda_nm': wavelengths_nm[color],
            'frecuencia_Hz': frequencies[color],
            'Vstop_V': vstop
        })
    return pd.DataFrame(rows).sort_values('frecuencia_Hz').reset_index(drop=True)

def build_results_table_with_uncertainty(
    color_dfs: dict,
    wavelengths_nm: dict,
    xcol: str,
    ycol: str,
    dycol: str
) -> pd.DataFrame:
    frequencies = compute_frequencies(wavelengths_nm)
    rows = []
    for color, df in color_dfs.items():
        vstop, sigma_vstop = estimate_vstop_and_uncertainty(df, xcol, ycol, dycol)
        rows.append({
            'Color': color,
            'lambda_nm': wavelengths_nm[color],
            'frecuencia_Hz': frequencies[color],
            'Vstop_V': vstop,
            'sigma_Vstop_V': sigma_vstop
        })
    out = pd.DataFrame(rows).sort_values('frecuencia_Hz').reset_index(drop=True)
    # Si vas a usar magnitud positiva
    out['U0_V'] = -out['Vstop_V']
    out['sigma_U0_V'] = out['sigma_Vstop_V']
    return out

# def fit_planck(results_df: pd.DataFrame, ycol: str = 'Vstop_V', signed_voltage: bool = True) -> dict:
def fit_planck(results_df: pd.DataFrame, ycol: str = 'U0_V', signed_voltage: bool = True) -> dict:
    """Ajusta Vstop vs frecuencia y estima h."""
    fit_df = results_df.dropna(subset=['frecuencia_Hz', ycol]).copy()
    x = fit_df['frecuencia_Hz'].values
    y = fit_df[ycol].values

    m, b = np.polyfit(x, y, 1)
    # if signed_voltage:
    #     h_exp = -m * E_CHARGE
    # else:
    #     h_exp = m * E_CHARGE
    h_exp = m * E_CHARGE
    error_pct = abs(h_exp - H_REAL) / H_REAL * 100
    return {
        'fit_df': fit_df,
        'slope': m,
        'intercept': b,
        'h_exp': h_exp,
        'h_real': H_REAL,
        'error_pct': error_pct,
        'ycol': ycol
    }

def fit_planck_weighted(results_df: pd.DataFrame, xcol: str = 'frecuencia_Hz', ycol: str = 'U0_V', sycol: str = 'sigma_U0_V'):
    """
    Ajuste lineal ponderado de y = m x + b.
    Retorna m, b, sigma_m, sigma_b, h y sigma_h.
    """
    temp = results_df.dropna(subset=[xcol, ycol, sycol]).copy()
    x = temp[xcol].values
    y = temp[ycol].values
    sy = temp[sycol].values
    # pesos
    w = 1.0 / (sy ** 2)
    S = np.sum(w)
    Sx = np.sum(w * x)
    Sy = np.sum(w * y)
    Sxx = np.sum(w * x * x)
    Sxy = np.sum(w * x * y)
    Delta = S * Sxx - Sx**2
    m = (S * Sxy - Sx * Sy) / Delta
    b = (Sxx * Sy - Sx * Sxy) / Delta
    sigma_m = np.sqrt(S / Delta)
    sigma_b = np.sqrt(Sxx / Delta)
    h_exp = E_CHARGE * m
    sigma_h = E_CHARGE * sigma_m
    error_pct = abs(h_exp - H_REAL) / H_REAL * 100
    return {
        'fit_df': temp,
        'slope': m,
        'intercept': b,
        'sigma_slope': sigma_m,
        'sigma_intercept': sigma_b,
        'h_exp': h_exp,
        'sigma_h': sigma_h,
        'h_real': H_REAL,
        'error_pct': error_pct,
        'ycol': ycol
    }

def print_fit_summary_weighted(fit_data: dict):
    print("\n=== Ajuste lineal ponderado U0 = m*nu + b ===")
    print(f"Pendiente m       = {fit_data['slope']:.6e} ± {fit_data['sigma_slope']:.6e} V*s")
    print(f"Intercepto b      = {fit_data['intercept']:.6f} ± {fit_data['sigma_intercept']:.6f} V")
    print(f"h experimental    = {fit_data['h_exp']:.6e} ± {fit_data['sigma_h']:.6e} J*s")
    print(f"h aceptado        = {fit_data['h_real']:.6e} J*s")
    print(f"Error porcentual  = {fit_data['error_pct']:.2f} %")

def plot_signal_vs_voltage(
    color_dfs: dict,
    xcol: str,
    ycol: str,
    title_prefix: str,
    error_y: str | None = None,
    save: bool = True,
    folder: str = 'fig',
    file_prefix: str = 'grafica'
):
    for color, df in color_dfs.items():
        fig = px.scatter(
            df,
            x=xcol,
            y=ycol,
            error_y=error_y,
            title=f'{title_prefix} ({color})',
            labels={xcol: 'Vf [V]', ycol: 'V [V]'}
        )
        fig.add_trace(go.Scatter(
            x=df[xcol],
            y=df[ycol],
            mode='lines',
            name=color
        ))
        fig.add_hline(y=0, line_dash='dash')
        if save:
            save_figure(fig, filename=f'{file_prefix}_{color}', folder=folder, save_pdf=True, save_html=False)
        else:
            fig.show()

def plot_combined_signal_vs_voltage(
    color_dfs: dict,
    xcol: str,
    ycol: str,
    title: str,
    error_y: str | None = None,
    save: bool = True,
    folder: str = 'fig',
    filename: str = 'grafica_combinada'
):
    frames = []
    for color, df in color_dfs.items():
        temp = df.copy()
        temp['Color'] = color
        frames.append(temp)
    all_df = pd.concat(frames, ignore_index=True)
    fig = px.scatter(
        all_df,
        x=xcol,
        y=ycol,
        color='Color',
        error_y=error_y,
        title=title,
        labels={xcol: 'Vf [V]', ycol: 'V [V]'}
    )
    for color, df in color_dfs.items():
        fig.add_trace(go.Scatter(
            x=df[xcol],
            y=df[ycol],
            mode='lines',
            name=f'{color} (línea)'
        ))
    fig.add_hline(y=0, line_dash='dash')
    if save:
        save_figure(fig, filename=filename, folder=folder, save_pdf=True, save_html=False)
    else:
        fig.show()

def plot_vstop_vs_frequency(
    fit_data: dict,
    save: bool = True,
    folder: str = 'fig',
    filename: str = 'vstop_vs_frecuencia'
):
    fit_df = fit_data['fit_df']
    m = fit_data['slope']
    b = fit_data['intercept']
    # ycol = fit_data.get('ycol', 'Vstop_V')
    ycol = fit_data.get('ycol', 'U0_V')

    fig = px.scatter(
        fit_df,
        x='frecuencia_Hz',
        y=ycol,
        error_y='sigma_U0_V' if 'sigma_U0_V' in fit_df.columns else None,
        text='Color',
        title='Voltaje de frenado Vf vs Frecuencia v',
        labels={
            'frecuencia_Hz': 'v [Hz]',
            ycol: 'Vf [V]'
        }
    )
    x_line = np.linspace(fit_df['frecuencia_Hz'].min(), fit_df['frecuencia_Hz'].max(), 200)
    y_line = m * x_line + b

    fig.add_trace(go.Scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        name='Ajuste lineal'
    ))
    fig.update_traces(textposition='top center')
    if save:
        save_figure(fig, filename=filename, folder=folder, save_pdf=True, save_html=False)
    else:
        fig.show()

def print_fit_summary(fit_data: dict):
    print("\n=== Ajuste lineal Vstop = m*nu + b ===")
    print(f"Pendiente m      = {fit_data['slope']:.6e} V*s")
    print(f"Intercepto b     = {fit_data['intercept']:.6f} V")
    print(f"h experimental   = {fit_data['h_exp']:.6e} J*s")
    print(f"h aceptado       = {fit_data['h_real']:.6e} J*s")
    print(f"Error porcentual = {fit_data['error_pct']:.2f} %")
