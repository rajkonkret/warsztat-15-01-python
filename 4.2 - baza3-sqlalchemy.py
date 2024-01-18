# ORM - Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM)
# sqlalchemy - system orm do współparacy z bazą danych
# pip install sqlalchemy  - instalowanie pakietów pythona poprzez menadżer pakietów
from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship('Address',
                             back_populates='person',
                             order_by='Address.email',
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


# encje

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

sesion = Session()

anakin = Person(name='Anakin', age=38)
obi = Person(name="Obi Wan Kenobi", age=45)
obi.addresses = [
    Address(email='obi@examplle.com'),
    Address(email='waaka@example.com')
]

obi2 = Person(name='obi', age=54)

sesion.add(anakin)
sesion.add(obi)
sesion.add(obi2)
sesion.commit()

all_ = sesion.query(Person).all()
print(all_)  # [Anakin (id=1), Obi Wan Kenobi (id=2), obi (id=3)]

an1 = sesion.query(Person).first()
print(an1)
print(type(an1))  # <class '__main__.Person'>
print(an1.id, an1.name, an1.addresses)  # 1 Anakin []

obi_list = sesion.query(Person).filter(
    Person.name.like('Obi%')
).all()
print(obi_list)  # [Obi Wan Kenobi (id=2), obi (id=3)]
for o in obi_list:
    print("id=", o.id, "name:", o.name, 'age:', o.age, "email:", o.addresses)
# id= 2 name: Obi Wan Kenobi age: 45 email: [obi@examplle.com, waaka@example.com]
# id= 3 name: obi age: 54 email: []
