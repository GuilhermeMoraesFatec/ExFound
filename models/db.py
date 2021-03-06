# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

db = DAL("sqlite://dbexfound.db")

db.define_table("login",
                   Field("nome"),
                   Field("email"),
                   Field("local"),
                   Field("senha"),
                   Field("especialidade"),
                   Field("cpf"),
                   Field("Administrador","boolean"))

db.define_table("leilao",
                Field("local"),
                Field("especialidade"),
                Field("preco_sugerido"),
                Field("preco_minimo"),
                Field("data_expiracao"),
                Field("descricao"))

db.define_table("lance",
                Field("valor"),
                Field("leilao","reference leilao"),
                Field("user","reference login"),
                Field("data","date",default=request.now))
