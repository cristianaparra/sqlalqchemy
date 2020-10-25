from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///insta.sqlite')
Session = sessionmaker(bin=engine)
session = Session()