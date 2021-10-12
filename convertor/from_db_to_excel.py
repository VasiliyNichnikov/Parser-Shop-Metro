import pandas as pd
from database.ad_metro import AdMetro
from sqlalchemy.orm import Session


def create_excel(session: Session, path_excel, name) -> None:
    df = pd.DataFrame()

    df['№'] = [i[0] for i in session.query(AdMetro.ID).all()]
    df['Артикул'] = [' ' for i in session.query(AdMetro.ARTICLE_NUMBER).all()]
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

    writer = pd.ExcelWriter(path_excel + f'{name}.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
    df.to_excel(writer, sheet_name='Шаблон для поставщика', index=False)
    worksheet = writer.sheets['Шаблон для поставщика']

    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 20)
    worksheet.set_column('H:H', 100)
    worksheet.set_column('I:I', 100)
    worksheet.set_column('J:J', 30)
    worksheet.set_column('K:K', 30)
    worksheet.set_column('L:L', 20)
    worksheet.set_column('M:M', 30)
    worksheet.set_column('N:N', 10)
    worksheet.set_column('O:O', 30)
    worksheet.set_column('P:P', 30)
    worksheet.set_column('Q:Q', 100)
    worksheet.set_column('R:R', 100)
    worksheet.set_column('S:S', 100)
    worksheet.set_column('T:T', 100)
    worksheet.set_column('U:U', 100)
    worksheet.set_column('V:V', 100)

    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value)
    print('Файл сохранен в excel')
    writer.save()
