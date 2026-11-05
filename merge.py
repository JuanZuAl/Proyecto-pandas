from pathlib import Path


PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    Revisar:
    - Que exista la columna "id_cliente" en los dos dataframes.
    - Que "id_cliente" no esté repetido en clientes.
    - Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    - Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    """
    # TODO 6: escribir las validaciones y devolver True o False.
    # Verificar que exista la columna "id_cliente" en ambos dataframes
    if "id_cliente" not in clientes.columns:
        print("Error: La columna 'id_cliente' no existe en el dataframe de clientes.")
        return False
    if "id_cliente" not in ventas.columns:
        print("Error: La columna 'id_cliente' no existe en el dataframe de ventas.")
        return False    

    # Verificar que "id_cliente" no esté repetido en clientes
    if clientes["id_cliente"].duplicated().any():
        print("Error: La columna 'id_cliente' tiene valores repetidos en el dataframe de clientes.")
        return False

    # Verificar que "id_cliente" tenga el mismo tipo en los dos dataframes
    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print("Error: La columna 'id_cliente' tiene tipos diferentes en los dataframes.")
        return False

    # Contar cuántas ventas no tienen cliente asociado
    sin_cliente = ventas[ventas["id_cliente"].isnull()].shape[0]
    print(f"Ventas sin cliente asociado: {sin_cliente}")

    print("Validación previa al merge completada correctamente.")
    return True


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    # TODO 7: validar con validar_premerge(), hacer el merge, guardar el CSV y devolver el dataframe.
    if not validar_premerge(clientes, ventas):
        print("Error: Validación fallida. No se puede realizar el merge.")
        return None

    # Realizar el merge
    merged_df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")

    # Guardar el resultado en un archivo CSV
    merged_df.to_csv(PROCESSED / "merge.csv", index=False)  

    print("Merge completado y resultado guardado.")
    return merged_df
