from sqlalchemy import Column, Integer, Float, String

from  model import Base

class Wines(Base):
    __tablename__ = 'wines'
    
    id = Column(Integer, primary_key=True)
    FA= Column("fixed_acidity", Float)
    VA = Column("volatile_acidity", Float)
    CA = Column("citric_acid", Float)
    RS = Column("residual_sugar", Float)
    CHL = Column("chlorides", Float)
    FSD = Column("free_sulfur_dioxide", Float)
    TSD = Column("total_sulfur_dioxide", Float)
    DENS = Column("density", Float)
    PH = Column("pH", Float)
    SLP = Column("sulphates", Float)
    ALC = Column("alcohol", Float)
    QLT = Column("quality", Integer)
    IS_RED = Column("is_red", Integer, nullable=True)
    
    def __init__(self, fa:Float, va:Float, ca:Float, rs:Float,
                 chl:Float, fsd:Float, tsd:Float, 
                 dens:Float, ph:Float, slp:Float, 
                 alc:Float, qlt:int, is_red:int):
        """
        Cria um Vinho na Base

        Arguments:
        fa:Float = Fixed acidity, 
        va:Float = volatile acidity, 
        ca:Float = citric acid, 
        rs:Float = residual Sugar,
        chl:Float = Chlorides, 
        fsd:Float = Free Sulfur Dioxide, 
        tsd:Float = Total Sulfur Dioxide, 
        dens:Float = Density, 
        ph:Float = PH, 
        slp:Float = Sulphates, 
        alc:Float = Alcohol, 
        qlt:int = Quality, 
        is_red: 1= Red, 0 = white
        """
        self.FA = fa
        self.VA = va
        self.CA = ca
        self.RS = rs
        self.CHL = chl
        self.FSD = fsd
        self.TSD = tsd
        self.DENS = dens
        self.PH = ph
        self.SLP = slp
        self.ALC = alc
        self.QLT = qlt
        self.IS_RED = is_red