import basedosdados as bd

billing_id = <seu_billing_id>

query = """
  WITH 
dicionario_Q05101 AS (
    SELECT
        chave AS chave_Q05101,
        valor AS descricao_Q05101
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q05101'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q09201 AS (
    SELECT
        chave AS chave_Q09201,
        valor AS descricao_Q09201
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q09201'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q09202 AS (
    SELECT
        chave AS chave_Q09202,
        valor AS descricao_Q09202
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q09202'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q094 AS (
    SELECT
        chave AS chave_Q094,
        valor AS descricao_Q094
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q094'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q09502 AS (
    SELECT
        chave AS chave_Q09502,
        valor AS descricao_Q09502
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q09502'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q098 AS (
    SELECT
        chave AS chave_Q098,
        valor AS descricao_Q098
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q098'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q10101 AS (
    SELECT
        chave AS chave_Q10101,
        valor AS descricao_Q10101
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q10101'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q10202 AS (
    SELECT
        chave AS chave_Q10202,
        valor AS descricao_Q10202
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q10202'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q105 AS (
    SELECT
        chave AS chave_Q105,
        valor AS descricao_Q105
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q105'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q106 AS (
    SELECT
        chave AS chave_Q106,
        valor AS descricao_Q106
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q106'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q10701 AS (
    SELECT
        chave AS chave_Q10701,
        valor AS descricao_Q10701
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q10701'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q109 AS (
    SELECT
        chave AS chave_Q109,
        valor AS descricao_Q109
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q109'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q11201 AS (
    SELECT
        chave AS chave_Q11201,
        valor AS descricao_Q11201
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q11201'
        AND id_tabela = 'microdados_2019'
),
dicionario_Q115 AS (
    SELECT
        chave AS chave_Q115,
        valor AS descricao_Q115
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'Q115'
        AND id_tabela = 'microdados_2019'
),
dicionario_T003 AS (
    SELECT
        chave AS chave_T003,
        valor AS descricao_T003
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'T003'
        AND id_tabela = 'microdados_2019'
),
dicionario_W001 AS (
    SELECT
        chave AS chave_W001,
        valor AS descricao_W001
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'W001'
        AND id_tabela = 'microdados_2019'
),
dicionario_VDD004A AS (
    SELECT
        chave AS chave_VDD004A,
        valor AS descricao_VDD004A
    FROM `basedosdados.br_ms_pns.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'VDD004A'
        AND id_tabela = 'microdados_2019'
)
SELECT
    dados.J007 as J007,
    dados.K045 as K045,
    dados.Q00201 as Q00201,
    dados.Q03001 as Q03001,
    descricao_Q05101 AS Q05101,
    dados.Q060 as Q060,
    dados.Q06306 as Q06306,
    dados.Q068 as Q068,
    dados.Q074 as Q074,
    dados.Q079 as Q079,
    dados.Q084 as Q084,
    dados.Q088 as Q088,
    dados.Q092 as Q092,
    descricao_Q09201 AS Q09201,
    descricao_Q09202 AS Q09202,
    dados.Q09301 as Q09301,
    descricao_Q094 AS Q094,
    descricao_Q09502 AS Q09502,
    dados.Q09605 as Q09605,
    dados.Q09606 as Q09606,
    dados.Q09607 as Q09607,
    descricao_Q098 AS Q098,
    dados.Q100 as Q100,
    descricao_Q10101 AS Q10101,
    descricao_Q10202 AS Q10202,
    dados.Q104 as Q104,
    descricao_Q105 AS Q105,
    descricao_Q106 AS Q106,
    descricao_Q10701 AS Q10701,
    descricao_Q109 AS Q109,
    dados.Q11006 as Q11006,
    dados.Q11007 as Q11007,
    dados.Q11008 as Q11008,
    dados.Q11009 as Q11009,
    dados.Q11010 as Q11010,
    dados.Q111 as Q111,
    descricao_Q11201 AS Q11201,
    dados.Q11405 as Q11405,
    dados.Q11406 as Q11406,
    dados.Q11407 as Q11407,
    dados.Q11408 as Q11408,
    descricao_Q115 AS Q115,
    dados.Q11604 as Q11604,
    dados.Q120 as Q120,
    dados.Q12102 as Q12102,
    dados.Q12104 as Q12104,
    dados.Q12105 as Q12105,
    dados.Q12106 as Q12106,
    dados.Q12107 as Q12107,
    dados.Q12108 as Q12108,
    dados.Q12109 as Q12109,
    dados.Q121010 as Q121010,
    dados.Q121011 as Q121011,
    dados.Q121012 as Q121012,
    dados.Q121013 as Q121013,
    dados.Q121014 as Q121014,
    dados.Q121015 as Q121015,
    dados.Q121016 as Q121016,
    dados.Q124 as Q124,
    dados.Q128 as Q128,
    descricao_T003 AS T003,
    descricao_W001 AS W001,
    dados.W00103 as W00103,
    dados.W00203 as W00203,
    descricao_VDD004A AS VDD004A,
    dados.VDF002 as VDF002,
    dados.VDF003 as VDF003
FROM `basedosdados.br_ms_pns.microdados_2019` AS dados
LEFT JOIN `dicionario_Q05101`
    ON dados.Q05101 = chave_Q05101
LEFT JOIN `dicionario_Q09201`
    ON dados.Q09201 = chave_Q09201
LEFT JOIN `dicionario_Q09202`
    ON dados.Q09202 = chave_Q09202
LEFT JOIN `dicionario_Q094`
    ON dados.Q094 = chave_Q094
LEFT JOIN `dicionario_Q09502`
    ON dados.Q09502 = chave_Q09502
LEFT JOIN `dicionario_Q098`
    ON dados.Q098 = chave_Q098
LEFT JOIN `dicionario_Q10101`
    ON dados.Q10101 = chave_Q10101
LEFT JOIN `dicionario_Q10202`
    ON dados.Q10202 = chave_Q10202
LEFT JOIN `dicionario_Q105`
    ON dados.Q105 = chave_Q105
LEFT JOIN `dicionario_Q106`
    ON dados.Q106 = chave_Q106
LEFT JOIN `dicionario_Q10701`
    ON dados.Q10701 = chave_Q10701
LEFT JOIN `dicionario_Q109`
    ON dados.Q109 = chave_Q109
LEFT JOIN `dicionario_Q11201`
    ON dados.Q11201 = chave_Q11201
LEFT JOIN `dicionario_Q115`
    ON dados.Q115 = chave_Q115
LEFT JOIN `dicionario_T003`
    ON dados.T003 = chave_T003
LEFT JOIN `dicionario_W001`
    ON dados.W001 = chave_W001
LEFT JOIN `dicionario_VDD004A`
    ON dados.VDD004A = chave_VDD004A
"""

bd.read_sql(query = query, billing_project_id = billing_id)
