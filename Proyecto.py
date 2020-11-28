from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String,Integer,Column,DateTime
from datetime import datetime

print("Número de contagiados en el Estado de Nuevo León")