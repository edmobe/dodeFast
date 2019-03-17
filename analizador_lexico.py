import ply.lex as lex
import re
import codecs
import os
import sys
tokens =  [
    'ID','DEFAULT','NUMBER', 'SEMICOLON', 'ASSIGNMENT', 'LPARENTESIS', 'RPARENTESIS', 'NE', 'LT', 'GT', 'ASSIGN', 
    'GTE', 'LTE', 'COMMA'
     
]
reservadas = { 
    'Entons':'ENTONCES', 
    'SiNo':'SINO', 
    'EnCaso':'ENCASO', 
    'FinEnCaso':'FINENCASO', 
    'Cuando':'CUANDO',
    'HastaEncontrar': 'WHILE',
    'Repita':'REPEAT', 
    'Desde':'Desde', 
    'Hasta':'TILL', 
    'Haga':'DO',
    'DCL':'DECLARATION', 
    'Inc':'INCREMENT', 
    'Dec':'DECREMENT', 
    'Ini':'INITIALIZE', 
    'Mover':'MOVER', 
    'Aleatorio':'Random', 
    'Proc':'PROCEDIMIENTO',  
    'Inicio':'BEGIN', 
    'Final':'END', 
    'Llmar':'CALL', 
    'AF':'ARRIBAFRENTE', 
    'F':'FRENTE', 
    'DFA':'DERECHAFRENTEARRIBA', 
    'IFA':'IZQUIERDAFRENTEARRIBA', 
    'DFB':'DERECHAFRENTEBAJO', 
    'IFB':'IZQUIERDAFRENTEBAJO', 
    'A':'ATRAS', 'DAA':'DERECHAATRASARRIBA',
    'IAA':'IZQUIERDAATRASARRIBA',
    'DAB':'DERECHAATRASBAJO', 
    'IAB':'IZQUIERDAATRASBAJO', 
    'AA':'ABAJOATRAS'
}

tokens = tokens + list(reservadas.values())

t_ignore = r'\t'
t_ASSIGN = r'='
t_GT = r'>'
t_LT = r'<'
t_NE = r'<>'
t_GTE = r'>='
t_LTE = r'<='
t_SEMICOLON = r';'
t_COMMA = r','
#t_ASSIGNMENT = r'DCL'
t_LPARENTESIS = r'{'
t_RPARENTESIS = r'}'


def t_ASSIGNMENT(t):
    r'DCL'
     return t

def t_ID (t):
    r'[a-zA-Z_][a-zA-Z0-9_@#]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print "Caracter invalido '%s' " %t.value[0]
    t.lexer.skip(1)

