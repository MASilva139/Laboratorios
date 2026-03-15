from config import FILES, WAVELENGTHS_NM, COLUMN_MAP
from photoelectric_common import (
    load_csv_files,
    coerce_numeric_columns,
    add_real_stopping_voltage,
    get_reference_value,
    apply_reference_correction,
    build_results_table,
    fit_planck,
    plot_signal_vs_voltage,
    plot_combined_signal_vs_voltage,
    plot_vstop_vs_frequency,
    print_fit_summary
)

def main():
    colors = ['rojo', 'naranja', 'verde', 'azul', 'violeta']
    dfs = load_csv_files(FILES)
    dfs = coerce_numeric_columns(
        dfs,
        columns=[
            COLUMN_MAP['vf'],
            COLUMN_MAP['v_amp'],
            COLUMN_MAP['delta_uv'],
            COLUMN_MAP['ic']
        ]
    )

    # Como me indicaste que físicamente aplicaron voltaje negativo:
    dfs = add_real_stopping_voltage(dfs, vf_col=COLUMN_MAP['vf'], negate_vf=True)

    # Referencia usando corriente
    ic_ref = get_reference_value(dfs['referencia'], COLUMN_MAP['ic'])
    print(f"Referencia de corriente = {ic_ref}")

    color_dfs = apply_reference_correction(
        dfs=dfs,
        colors=colors,
        signal_col=COLUMN_MAP['ic'],
        ref_value=ic_ref,
        corrected_col='Ic_corr[mA]'
    )

    # Gráficas Ic vs Vf
    plot_signal_vs_voltage(
        color_dfs=color_dfs,
        xcol='Vf_real[V]',
        ycol='Ic_corr[mA]',
        title_prefix='Corriente corregida vs potencial de frenado'
    )
    plot_combined_signal_vs_voltage(
        color_dfs=color_dfs,
        xcol='Vf_real[V]',
        ycol='Ic_corr[mA]',
        title='Corriente corregida vs potencial de frenado para todos los colores'
    )

    # Potenciales de frenado
    results_df = build_results_table(
        color_dfs=color_dfs,
        wavelengths_nm=WAVELENGTHS_NM,
        xcol='Vf_real[V]',
        ycol='Ic_corr[mA]',
        method='fit'   # puedes cambiar a 'linear'
    )
    print("\n=== Potenciales de frenado ===")
    print(results_df)
    # Ajuste para h
    fit_data = fit_planck(results_df)
    print_fit_summary(fit_data)
    plot_vstop_vs_frequency(fit_data)

if __name__ == '__main__':
    main()