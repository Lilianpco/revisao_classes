class Pessoa:
    def __init__(self, nome, genero,idade):
        self.nome =nome
        self.genero= genero
        self.idade = idade


class Paciente(Pessoa):
    def __init__(self, nome, genero,idade, sintoma):
        super().__init__( nome, genero,idade) 
        self.sintoma =  sintoma   

    def imprimir_sintoma(self):        
        return print( f'Sintoma:{self.sintoma}/n')        

    def imprimir_dados(self):
        print( f'dados:{self.nome}')
        print( f'dados:{self.idade}')




class Medico(Pessoa):

    def __init__(self,nome,idade,genero,instituicao_de_ensino,ano_de_formacao,crm,carga_horaria, especialidade):
        super().__init__(nome,idade,genero)
        self.instituicao_de_ensino=instituicao_de_ensino
        self.ano_de_formacao=ano_de_formacao
        self.especialidade = especialidade   
        self.crm=crm 
        self.carga_horaria=carga_horaria

    def imprimir_crm(self):
        #return print('CRM:'+ self.crm)
        return print( f'CRM:{self.crm}/n')


    print('____paciente____')
    paciente = Paciente('Lilian','feminino','23','dor ocular')
    paciente.imprimir_sintoma()
  

        
