from config import FILES, WAVELENGTHS_NM, COLUMN_MAP, DEFAULT_SIGNAL_UNITS
from photoelectric_common import (
    load_csv_files,
    coerce_numeric_columns,
    add_real_stopping_voltage,
    get_reference_value,
    apply_reference_correction,
    convert_signal_to_volts_from_column,
    convert_delta_to_volts,
    build_results_table,
    fit_planck,
    plot_signal_vs_voltage,
    plot_combined_signal_vs_voltage,
    plot_vstop_vs_frequency,
    print_fit_summary,
    build_results_table_with_uncertainty,
    fit_planck_weighted,
    print_fit_summary_weighted
)

def main():
    colors = ['rojo', 'naranja', 'verde', 'azul', 'violeta']
    dfs = load_csv_files(FILES)
    dfs = coerce_numeric_columns(
        dfs,
        columns=[
            COLUMN_MAP['vf'],
            COLUMN_MAP['v_amp'],
            COLUMN_MAP['delta_uv']
        ]
    )
    # Como físicamente aplicaron voltaje negativo:
    dfs = add_real_stopping_voltage(dfs, vf_col=COLUMN_MAP['vf'], negate_vf=True)
    # Convertir la señal del amplificador a voltios usando V_unit
    for name, df in dfs.items():
        dfs[name] = convert_signal_to_volts_from_column(
            df,
            signal_col=COLUMN_MAP['v_amp'],
            unit_col=COLUMN_MAP['v_unit'],
            output_col='V_signal[V]',
            default_unit=DEFAULT_SIGNAL_UNITS[name]
        )

        dfs[name] = convert_delta_to_volts(
            dfs[name],
            delta_col=COLUMN_MAP['delta_uv'],
            output_col='delta[V]'
        )

    # Referencia del amplificador ya en voltios
    vref = get_reference_value(dfs['referencia'], 'V_signal[V]')
    print(f"Referencia del amplificador = {vref:.6e} V")

    color_dfs = apply_reference_correction(
        dfs=dfs,
        colors=colors,
        signal_col='V_signal[V]',
        ref_value=vref,
        corrected_col='Vcorr[V]'
    )

    # Gráficas Vcorr vs Vf
    plot_signal_vs_voltage(
        color_dfs=color_dfs,
        xcol='Vf_real[V]',
        ycol='Vcorr[V]',
        error_y='delta[V]',
        title_prefix='Voltaje (amplificador) vs Vf',
        save=True,
        folder='F901/Lab05/fig',
        file_prefix='P05_fig01'
    )

    plot_combined_signal_vs_voltage(
        color_dfs=color_dfs,
        xcol='Vf_real[V]',
        ycol='Vcorr[V]',
        error_y='delta[V]',
        title='Voltaje (amplificador) vs Vf',
        save=True,
        folder='F901/Lab05/fig',
        filename='P05_fig02'
    )

    # Potenciales de frenado
    results_df = build_results_table(
        color_dfs=color_dfs,
        wavelengths_nm=WAVELENGTHS_NM,
        xcol='Vf_real[V]',
        ycol='Vcorr[V]',
        method='fit'   # puedes cambiar a 'linear'
    )
    print("\n=== Potenciales de frenado ===")
    print(results_df)
    results_df['U0_V'] = -results_df['Vstop_V']

    # Ajuste para h
    fit_data = fit_planck(results_df, ycol='U0_V', signed_voltage=False)
    print_fit_summary(fit_data)

    plot_vstop_vs_frequency(
        fit_data=fit_data,
        save=True,
        folder='F901/Lab05/fig',
        filename='P05_fig03'
    )

    # Versión con incerteza
    results_df = build_results_table_with_uncertainty(
        color_dfs=color_dfs,
        wavelengths_nm=WAVELENGTHS_NM,
        xcol='Vf_real[V]',
        ycol='Vcorr[V]',
        dycol='delta[V]'
    )
    print("\n=== Potenciales de frenado e incertidumbres ===")
    print(results_df[['Color', 'lambda_nm', 'frecuencia_Hz', 'Vstop_V', 'sigma_Vstop_V', 'U0_V', 'sigma_U0_V']])

    # 10. Ajuste lineal ponderado
    fit_data = fit_planck_weighted(
        results_df,
        xcol='frecuencia_Hz',
        ycol='U0_V',
        sycol='sigma_U0_V'
    )
    print_fit_summary_weighted(fit_data)

if __name__ == '__main__':
    main()