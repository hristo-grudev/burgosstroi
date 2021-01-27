import sqlite3


class BurgosstroiPipeline:
    conn = sqlite3.connect('burgosstroi.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `burgosstroi` (
                                                            description text
                                                            )''')
        self.conn.commit()

    def process_item(self, item, spider):
        description = item['description'][0]

        self.cursor.execute(f"""select * from burgosstroi where description = '{description}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `burgosstroi` (`description`) values ('{description}')""")
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
