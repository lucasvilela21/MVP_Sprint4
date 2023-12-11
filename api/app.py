from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model import Session, Wines, Model_Wine
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
vinho_tag = Tag(name="Vinho", description="Adição, visualização, remoção e predição de vinhos vermelhos")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de vinhos
@app.get('/vinhos', tags=[vinho_tag],
         responses={"200": WineViewSchema, "404": ErrorSchema})
def get_vinhos():
    """Lista todos os vinhos cadastrados na base
    Retorna uma lista de vinhos cadastrados na base.
    
    Args:
        id (int): id do vinho
        
    Returns:
        list: lista de vinhos cadastrados na base
    """
    session = Session()
    
    # Buscando todos os pacientes
    vinhos = session.query(Wines).all()
    
    if not vinhos:
        logger.warning("Não há vinhos cadastrados na base :/")
        return {"message": "Não há vinhos cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d vinhos encontrados" % len(vinhos))
        return apresenta_vinhos(vinhos), 200


# Rota de adição de vinho
@app.post('/vinho', tags=[vinho_tag],
          responses={"200": WineViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: WineSchema):
    """Adiciona um novo vinho à base de dados
    Retorna uma representação dos vinhos vermelhos ou brancos.
        
    Returns:
        is_red: se o vinho é vermelho ou não
    """
    
    # Carregando modelo
    ml_path = 'ml_model/model_wine.pkl'
    modelo = Model_Wine.carrega_modelo(ml_path)

    # Carregando scaler
    ml_path = 'ml_model/scaler_wine.pkl'
    scaler = Model_Wine.carrega_modelo(ml_path)

    form_predict = WinePredictSchema()

    form_predict.vol_acid =form.VA
    form_predict.alcohol=form.ALC
    form_predict.free_diox=form.FSD
    form_predict.chlorides=form.CHL

    vinho = Wines(
        fa=form.FA,
        va=form.VA,
        ca=form.CA,
        rs=form.RS,
        chl=form.CHL,
        fsd=form.FSD,
        tsd=form.TSD,
        dens=form.DENS,
        ph=form.PH,
        slp=form.SLP,
        alc=form.ALC,
        qlt=form.QLT,
        is_red=Model_Wine.preditor(modelo ,scaler, form_predict)
    )
    logger.debug(f"Adicionando vinho de id: '{vinho.id}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Adicionando vinho
        session.add(vinho)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado vinho de id: '{vinho.id}'")
        return apresenta_vinho(vinho), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar vinho '{vinho.id}', {error_msg}")
        return {"message": error_msg}, 400
    
# Rota de busca de vinho por id
@app.get('/vinho', tags=[vinho_tag],
         responses={"200": WineViewSchema, "404": ErrorSchema})
def get_vinho(query: WineBuscaSchema):    
    """Faz a busca por um vinho cadastrado na base a partir do id

    Args:
        id (int): id
        
    Returns:
        is_red: se o vinho é vermelho ou branco
    """
    
    vinho_id = query.id
    logger.debug(f"Coletando dados sobre produto #{vinho_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinho = session.query(Wines).filter(Wines.id == vinho_id).first()
    
    if not vinho:
        # se o vinho não foi encontrado
        error_msg = f"Vinho id : {vinho_id} não encontrado na base :/"
        logger.warning(f"Erro ao buscar vinhi id: '{vinho_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Vinho encontrado: '{vinho_id}'")
        # retorna a representação do vinho
        return apresenta_vinho(vinho), 200