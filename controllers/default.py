# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import datetime
def tela_detalhes_leilao():
    return dict()
def cad_leilao():
    return dict()
def tela_leilao():
    return dict()
def menu():
    session.email = request.post_vars["email"]
    return dict()
def cad_perito():
    return dict()
def tela_consulta():
    return dict()

def actionCadLance():
    sd = db(db.login.email == session.email).select(db.login.ALL)
    valor = request.post_vars.valor
    cdLeilao = request.vars.cdLeilao
    db.lance.bulk_insert([{'valor':valor, "leilao":cdLeilao, "user":sd[0].id, "data":datetime.datetime.now()}])
    db.commit()
    redirect(URL("tela_detalhes_leilao.html",vars=dict(id=cdLeilao)))
    return dict()
def actionCadLeilao():
    local = request.post_vars["local"]
    especialidade = request.post_vars["especialidades"]
    preco_sugerido = float(request.post_vars["preco_sugerido"])
    preco_minimo = float(request.post_vars["preco_minimo"])
    data = request.post_vars["data_expiracao"]
    desc = request.post_vars["descricao"]

    db.leilao.bulk_insert([{'local':local,'especialidade':especialidade,"preco_sugerido":preco_sugerido,"preco_minimo":preco_minimo,"data_expiracao": data,"descricao":desc}])
    db.commit()
    redirect(URL("cad_leilao.html"))
    return dict()

def actionCadPerito():
    nome = request.post_vars["nome"]
    especialidade = request.post_vars["especialidade"]
    cpf = request.post_vars["cpf"]
    endereco = request.post_vars["endereco"]
    db.login.bulk_insert([{'nome':nome,'especialidade':especialidade,"cpf":cpf,"local":endereco}])
    db.commit()
    redirect(URL("cad_perito.html"))
    return dict()
def index():
    
    return dict()


def user():

    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
