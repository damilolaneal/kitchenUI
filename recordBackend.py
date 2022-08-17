import sqlite3


class RecordBackend:
    def __init__(self):
        self.con = sqlite3.connect('example.db')
        self.cur = self.con.cursor()
        self.create_table("CREATE TABLE IF NOT EXISTS comment (subject_id text, capture_date text, begin_comment text, "
                          "end_comment text, PRIMARY KEY (subject_id, capture_date))")

    def create_table(self, query: str):
        try:
            self.cur.execute(query)
            self.con.commit()
        except sqlite3.Error as er:
            print(er)

    def insert_init_data(self, _id: str, capture_date: str, begin_comment: str) -> bool:
        try:
            data = (_id, capture_date, begin_comment, "")
            self.cur.execute("INSERT INTO comment VALUES(?, ?, ?, ?)", data)
            self.con.commit()
            return True
        except sqlite3.Error as er:
            print(er)
            return False

    def update_end_comment(self, end_comment: str, subject_id: str, capture_date: str) -> bool:
        try:
            data = (end_comment, subject_id, capture_date)
            self.cur.execute("UPDATE comment SET end_comment = ? WHERE subject_id = ? AND capture_date = ?", data)
            self.con.commit()
            return True
        except sqlite3.Error as er:
            print(er)
            return False

    def close_con(self):
        self.con.close()
