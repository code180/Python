import pytest
from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:1771@localhost:5432/postgres"

db = create_engine(db_connection_string)

userid = 5555
useremail = 'sasha111555@gmail.com'
subjectid = 2


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into users(\"user_email\") values (:email)")
    db.execute(sql, email=useremail)


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update users set subject_id = :subject_id where user_email = :email")
    db.execute(sql, subject_id=subjectid, email=useremail)

    sql2 = text("update users set user_id = :uid where user_email = :email")
    db.execute(sql2, uid=userid, email=useremail)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from users where user_id = :id")
    db.execute(sql, id=userid)
