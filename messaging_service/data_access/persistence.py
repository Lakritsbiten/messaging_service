import sqlite3
import json
from datetime import datetime
from messaging_service.utils.singleton import Singleton


class MessageDatabase(metaclass=Singleton):

    def __init__(self):
        self.__connection = sqlite3.connect(":memory:")     # database in memory
        self.__cursor = self.__connection.cursor()
        self.__cursor.row_factory = self.__dict_factory
        self.setup()

        # insert first message into database for test purposes:
        self.insert_message(sender_id='Test Daemon', recipient_id='Test Customer',
                            message_body='This is the first message, and will have message_id = 1',
                            send_date='2021-05-01', is_read=False)

    def setup(self):
        message_table_stmt = 'create table message(' \
                             'message_id INTEGER PRIMARY KEY AUTOINCREMENT not null,' \
                             'sender_id TEXT not null,' \
                             'recipient_id TEXT not null,' \
                             'send_date TEXT not null,' \
                             'message_body TEXT not null,' \
                             'is_read INTEGER)'
        self.execute(message_table_stmt, tuple())

    @staticmethod
    def __dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def execute(self, statement, args):
        self.__cursor.execute(statement, args)
        result = self.__cursor.fetchall()
        return result

    def insert_message(self, sender_id, recipient_id, message_body,
                       send_date=datetime.today().strftime('%Y-%m-%d'), is_read=False):
        _is_read = 1 if is_read else 0
        stmt = 'insert into message(sender_id, recipient_id, send_date, message_body, is_read) values (?, ?, ?, ?, ?)'
        args = (sender_id, recipient_id, send_date, message_body, _is_read)
        return self.execute(stmt, args)

    def get_message_by_id(self, message_id):
        stmt = 'select * from message where message_id = ?'
        args = (message_id, )
        return self.execute(stmt, args)

    def get_messages_by_date(self, start, stop=datetime.today().strftime('%Y-%m-%d')):
        stmt = 'select * from message where send_date between ? and ?'
        args = (start, stop)
        return self.execute(stmt, args)

    def get_unread_messages(self):
        stmt = 'select * from message where is_read = 0'
        return self.execute(stmt, tuple())

    def delete_message(self, message_id):
        stmt = 'delete from message where message_id = ?'
        args = (message_id, )
        self.execute(stmt, args)

    def set_read_message(self, message_id):
        stmt = 'update message set is_read = 1 where message_id = ?'
        args = (message_id, )
        self.execute(stmt, args)

    def debug_content(self):
        stmt = 'select * from message'
        print('Debugging all content: {}'.format(self.execute(stmt)))


if __name__ == '__main__':
    db = MessageDatabase()
    print(db.get_message_by_id(1))
    print(db.get_message_by_id(2))
