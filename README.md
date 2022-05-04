# DESAFIO: Medicar

[![N|Solid](https://raw.githubusercontent.com/Intmed-Software/desafio/master/assets/logo.png)](https://nodesource.com/products/nsolid)

## Requesitos
- Python 3.10.4
- Django 3.2.13
 
Instalação após o Python
```sh
 # Aqui será isntalado o Django
pip install django
 # E o não menos importante, o rest Framework
pip install djangorestframework
 # Procure por atualizações no banco de dados
py manage.py makemigrations
 # Atualize o banco de dados
py manage.py migrate
```

Após a confirmação de todos os requesitos, rode o seguinte comando
```sh
py manage.py runserver
```


## Medico
RETORNO
```sh
GET /medicos/
```
```sh
 1  {
 2      {
 3          "id": 1,
 4          "crm": 3711,
 5          "nome": "Drauzio Varella",
 6          "email": "drauzinho@globo.com"
 7      },
 8      {
 9          "id": 2,
 10         "crm": 2544,
 11         "nome": "Gregory House",
 12         "email": "greg@hbo.com.br"
 13     }
 14 }
```

Cadastrar medico
```sh
POST /medicos/
```
```sh
 1   {
 2      "crm": 3711,
 3      "nome": "Drauzio Varella",
 4      "email": "drauzinho@globo.com"
 5   }
```

## Agenda
RETORNO
```sh
GET /agendas/
```
```sh
 1  {
 2    	{
 3    		"id": 14,
 4    		"medico": {
 5    			"id": 1,
 6    			"crm": "126481",
 7    			"nome": "Rogerio Fernandes",
 8    			"email": "rogerio_medic@intmed.care"
 9    		},
 10    		"dia": "2022-05-25",
 11    		"horarios": [
 12   			"00:32:00",
 13   			"00:25:00"
 14   		]
 15   	},
 16 }
```

Cadastrar Agenda
```sh
POST /agendas/
```
```sh
 1  {
 2    	{
 3    		"medico": 1,
 4    		"dia": "2022-05-25",
 5    		"horarios": [
 6   			{ "horarios" : "00:32:00" }
 7   		]
 8   	},
 9 }
```

## Consulta
RETORNO
```sh
GET /consulta/
```
```sh
 1  {
 2      {
 3          "id": 14,
 4          "dia": "2022-05-25",
 5          "horarios": "00:32:00",
 6          "data_agendamento": "2022-05-04T14:26:22.063414-03:00",
 7          "medico": {
 8              "id": 1,
 9              "crm": "126481",
 10             "nome": "Rogerio Fernandes",
 11             "email": "rogerio_medic@intmed.care"
 12         },
 13     },
 14 }
```

Agendar Consulta
```sh
POST /consulta/
```
```sh
 2  {
 3      "agenda_id": 1,
 4      "horario": "07:57:00",
 8	},
```
Retorno do agendamento da Consulta
```sh
1   {
2	    "id": 6,
3	    "dia": "2022-05-20",
4	    "horario": "07:57:00",
5	    "data_agendamento": "2022-05-04T15:17:54.169909-03:00",
6	    "medico": {
7	"       id": 1,
8	        "nome": "Rogerio Fernandes",
9	        "crm": "126481",
10	        "email": "rogerio_medic@intmed.care"
11      }
12  }
```

Desmarcar Consulta
```sh
POST /consulta/<consulta_id>
```
