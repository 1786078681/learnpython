# -*- coding: utf-8 -*-
# @Time    : 18-1-8 下午4:09
# @Author  : Gavin Gan
# @File    : db.py

from sqlalchemy import create_engine, Column, String, BigInteger, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine("mysql+pymysql://admin:admin123@127.0.0.1/testdb", encoding="utf8")
Base = declarative_base(bind=engine)

class Author(Base):
    __tablename__ = "author"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(32))
    age = Column(BigInteger)

    def __repr__(self):
        return "%s" % self.name

Base.metadata.create_all()

Session_cur = sessionmaker()
Session = Session_cur()

#
# author_obj_1 = Author(name="Py", age=11)
# author_obj_2 = Author(name="Py2", age=12)
# author_obj_3 = Author(name="Py3", age=15)
# author_obj_4 = Author(name="Py4", age=13)
#
# Session.add_all([author_obj_1, author_obj_2, author_obj_3, author_obj_4])
# Session.commit()
# data = Session.query(Author).filter(Author.name.like("%4")).count()
# print(data)

print(Session.query(func.count(Author.name), Author.name).filter(Author.id >0).group_by(Author.name).all())
