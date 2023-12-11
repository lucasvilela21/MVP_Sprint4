from pydantic import BaseModel
from typing import List
from model.wines import Wines

class WineSchema(BaseModel):
    """ Define como um novo vinho deve ser representado
    """
    FA: float = 7
    VA: float = 0.27
    CA: float = 0.36
    RS: float = 20.7
    CHL: float = 0.045
    FSD: float = 45
    TSD: float = 170
    DENS: float = 1.001
    PH: float = 3
    SLP: float = 0.45
    ALC: float = 8.8
    QLT: int = 6
    

class WinePredictSchema(BaseModel):
    """ Define como um novo vinho deve ser enviado para o modelo
    """
    vol_acid: float = 0.27
    chlorides: float = 0.045
    free_diox: float = 45
    alcohol: float = 8.8
  
class WineViewSchema(BaseModel):
    """Define como um vinho será retornado
    """
    id: int = 1
    FA: float = 7
    VA: float = 0.27
    CA: float = 0.36
    RS: float = 20.7
    CHL: float = 0.045
    FSD: float = 45
    TSD: float = 170
    DENS: float = 1.001
    PH: float = 3
    SLP: float = 0.45
    ALC: float = 8.8
    QLT: int = 6
    IS_RED: int = None
    
class WineBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base nid cadastrado do vinho
    """
    id: int = 1

class ListaWinesSchema(BaseModel):
    """Define como uma lista de vinhos será representada
    """
    vinhos: List[WineSchema]

    
class WineDelSchema(BaseModel):
    """Define como um vinho será deletado
    """
    id: int = 1
    
# Apresenta apenas os dados de um paciente    
def apresenta_vinho(vinho: Wines):
    """ Retorna uma representação do vinho seguindo o schema definido em
        WineViewSchema.
    """
    return {
        "id": vinho.id,
        "FA": vinho.FA,
        "VA": vinho.VA,
        "CA": vinho.CA,
        "RS": vinho.RS,
        "CHL": vinho.CHL,
        "FSD": vinho.FSD,
        "TSD": vinho.TSD,
        "DENS": vinho.DENS,
        "PH": vinho.PH,
        "SLP": vinho.SLP,
        "ALC": vinho.ALC,
        "QLT": vinho.QLT,
        "IS_RED": vinho.IS_RED
    }
    
# Apresenta uma lista de pacientes
def apresenta_vinhos(vinhos: List[Wines]):
    """ Retorna uma representação do vinho seguindo o schema definido em
        WinesViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
            "id": vinho.id,
            "FA": vinho.FA,
            "VA": vinho.VA,
            "CA": vinho.CA,
            "RS": vinho.RS,
            "CHL": vinho.CHL,
            "FSD": vinho.FSD,
            "TSD": vinho.TSD,
            "DENS": vinho.DENS,
            "PH": vinho.PH,
            "SLP": vinho.SLP,
            "ALC": vinho.ALC,
            "QLT": vinho.QLT,
            "IS_RED": vinho.IS_RED
        })

    return {"vinhos": result}

