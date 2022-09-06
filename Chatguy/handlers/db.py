from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, Table, MetaData, ForeignKey, join
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_db(DATABASE_URL):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

class Words(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String)
    children = relationship("Suggestions", lazy="joined", innerjoin=True)

class Suggestions(Base):
    __tablename__ = 'suggestions'
    id = Column(Integer, primary_key=True)
    id_word = Column(Integer, ForeignKey('words.id'))
    suggestion = Column(String)

class Corrections(Base):
    __tablename__ = 'corrections'
    id = Column(Integer, primary_key=True)
    source_text = Column(String)
    target_text = Column(String)

def get_suggest_words(session, idx):
    return session.query(Suggestions.suggestion).join(Words, Suggestions.id_word == Words.id).filter(Suggestions.id_word==idx).all()

def get_word_index(session, _word):
    return session.query(Words.id).filter(Words.word==_word).all()

def create_word(session, word):
    try:
        db_user = Words(word=word)
        session.add(db_user)
        session.commit()
    except:
        session.rollback()

def create_suggestion(session, id_word, suggestions):
    for suggest in suggestions:
        db_user = Suggestions(id_word=id_word, suggestion=suggest)
        session.add(db_user)
        session.commit()

def insert_corrections(session, source_text, target_text):
    try:
        for i in range(len(source_text)):
            db_user = Corrections(source_text=source_text[i], target_text=target_text[i])
            session.add(db_user)
            session.commit()
    except Exception as e:
        session.rollback()
