import pandas as pd
from database.db_session import create_session
from database.ad_metro import AdMetro


def create_excel(path_excel, name) -> None:
    session = create_session()
    df = pd.DataFrame()

    df['№'] = [i[0] for i in session.query(AdMetro.ID).all()]
    df['Артикул'] = [i[0] for i in session.query(AdMetro.ARTICLE_NUMBER).all()]
    df['Название товара'] = [i[0] for i in session.query(AdMetro.NAME).all()]
    df['Цена, руб.'] = [i[0] for i in session.query(AdMetro.PRICE).all()]
    df['Цена без скидки, руб.'] = [i[0] for i in session.query(AdMetro.PRICE_WITHOUT_DISCOUNT).all()]
    df['Вес, г'] = [i[0] for i in session.query(AdMetro.WEIGHT).all()]
    df['Ширина упаковки, мм'] = [i[0] for i in session.query(AdMetro.PACKING_WIDTH).all()]
    df['Высота упаковки, мм'] = [i[0] for i in session.query(AdMetro.PACKING_HEIGHT).all()]
    df['Длина упаковки, мм'] = [i[0] for i in session.query(AdMetro.PACKING_LENGTH).all()]

    df['Ссылка на главное фото'] = [i[0] for i in session.query(AdMetro.MAIN_IMAGE).all()]
    df['Ссылки на дополнительные фото'] = [i[0] for i in session.query(AdMetro.ADDITIONAL_IMAGES).all()]
    df['Артикул фото'] = [i[0] for i in session.query(AdMetro.ARTICLE_IMAGES).all()]

    df['Тип продукта'] = [i[0] for i in session.query(AdMetro.TYPE_PRODUCT).all()]
    df['Тип упаковки'] = [i[0] for i in session.query(AdMetro.TYPE_OF_PACKAGING).all()]
    df['Минимальная температура хранения'] = [i[0] for i in session.query(AdMetro.MINIMUM_STORAGE_TEMPERATURE).all()]
    df['Максимальная температура хранения'] = [i[0] for i in session.query(AdMetro.MAXIMUM_STORAGE_TEMPERATURE).all()]
    df['Срок годности в днях'] = [i[0] for i in session.query(AdMetro.SHELF_LIFE).all()]
    df['Бренд'] = [i[0] for i in session.query(AdMetro.BRAND).all()]
    df['Состав'] = [i[0] for i in session.query(AdMetro.STRUCTURE).all()]
    df['Описание'] = [i[0] for i in session.query(AdMetro.ANNOTATION).all()]
    df['Страна изготовитель'] = [i[0] for i in session.query(AdMetro.COUNTRY).all()]
    df['Энергетическая ценность в 100г'] = [i[0] for i in session.query(AdMetro.ENERGY_VALUE).all()]

    writer = pd.ExcelWriter(path_excel + f'{name}.xlsx', engine='xlsxwriter',
                            engine_kwargs={'options': {"strings_to_urls": False}})
    df.to_excel(writer, sheet_name='Шаблон для поставщика', index=False)
    worksheet = writer.sheets['Шаблон для поставщика']

    worksheet.set_column('A:A', 10)  # №
    worksheet.set_column('B:B', 20)  # Артикул
    worksheet.set_column('C:C', 70)  # Название товара
    worksheet.set_column('D:D', 20)  # Цена, руб.
    worksheet.set_column('E:E', 20)  # Цена без скидки, руб.
    worksheet.set_column('F:F', 20)  # Вес, г
    worksheet.set_column('G:G', 20)  # Ширина упаковки, мм
    worksheet.set_column('H:H', 20)  # Высота упаковки, мм
    worksheet.set_column('I:I', 20)  # Длина упаковки, мм
    worksheet.set_column('J:J', 45)  # Ссылка на главное фото
    worksheet.set_column('K:K', 45)  # Ссылки на дополнительные фото
    worksheet.set_column('L:L', 20)  # Артикул фото
    worksheet.set_column('M:M', 30)  # Тип продукта
    worksheet.set_column('N:N', 30)  # Тип упаковки
    worksheet.set_column('O:O', 20)  # Минимальная температура хранения
    worksheet.set_column('P:P', 20)  # Максимальная температура хранения
    worksheet.set_column('Q:Q', 30)  # Срок годности в днях
    worksheet.set_column('R:R', 40)  # Бренд
    worksheet.set_column('S:S', 100)  # Состав
    worksheet.set_column('T:T', 100)  # Описание
    worksheet.set_column('U:U', 30)  # Страна изготовитель
    worksheet.set_column('V:V', 20)  # Энергетическая ценность в 100г

    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value)
    print(f'Файл сохранен в excel: {path_excel + f"{name}.xlsx"}')
    writer.save()
    session.close()
