def listar_professores(cursor):
    cursor.execute(f'SELECT professor.nome FROM faculdade.professor;')
    detalhar = cursor.fetchall()
    cursor.close()
    return detalhar

def exibir_professor(cursor, nome):
    cursor.execute(f'SELECT nome, datanasc, nomemae, titulacao '
                   f'FROM faculdade.professor '
                   f'where nome= "{nome}"')
    professor = cursor.fetchone()
    cursor.close()
    return professor

def consultarTitulacao(cursor, parametro):
    cursor.execute(f'select nome from faculdade.professor where titulacao = {parametro}')
    consulta = cursor.fetchall()
    cursor.close()

    return consulta

def consultarapenascomputacao(cursor):
    cursor.execute(f'select professor.nome from faculdade.disciplina, faculdade.professor '
                   f'where disciplina.curso = "Ciência da Computação" '
                   f'and disciplina.idprofessor = professor.idprofessor')
    curso = cursor.fetchall()
    cursor.close()
    return curso