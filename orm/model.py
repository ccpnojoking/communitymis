from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://ccp:123456789@localhost/community",
                                    encoding='latin1', echo=True)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey

Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    username = Column(String(20),nullable=False)
    account = Column(String(20),nullable=False)
    pwd = Column(String(100),nullable=False)

class Service(Base):
    __tablename__ = "service"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    project = Column(String(100),nullable=False)
    describe = Column(String(100),nullable=True)
    building = Column(Integer, nullable=False)
    unit = Column(Integer, nullable=False)
    roomnum = Column(Integer, nullable=False)
    username = Column(String(100),nullable=False)
    tel = Column(String(100),nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)