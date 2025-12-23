from sqlalchemy import create_engine, Column, String, Integer, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class JobApplication(Base):
    __tablename__ = 'applications'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String, unique=True)
    description = Column(Text)
    match_score = Column(Float)
    status = Column(String)
    generated_cover_letter = Column(Text)

engine = create_engine('sqlite:///jobs.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)