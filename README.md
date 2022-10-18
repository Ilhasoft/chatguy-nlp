# Chatguy 🤖
### Chatguy - The powerful NLP's dataset creator.  <br><br>


[![]()]()
[![CI](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/tests.yml/badge.svg)](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/tests.yml)
[![Docker Image CI](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/docker-image.yml)
[![](https://img.shields.io/appveyor/tests/Ilhasoft/chatguy-nlp)](https://github.com/Ilhasoft/chatguy-nlp/tree/main/tests)
[![](https://img.shields.io/github/last-commit/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/contributors/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/issues-pr/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/v/tag/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/v/release/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/languages/top/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/badge/python-3.8-informational)]()
[![](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/tests.yml/badge.svg)]()
[![]()]()
[![]()]() 

## Overview
Chatguy is a Brazilian Portuguese dataset generator. Through natural language processing techniques it is possible to generate sentences from synonymous words and entity recognition. Its main functions can be divided between generating synonymous words and generating phrases or sentences.

### Requirements: <br>
- Python 3.8 <br>
- Docker <br>
- Docker-compose <br>
- Docker swarm <br>
- Git <br>

## Get Started

1. First, clone the repo: <br>
```git clone https://github.com/Ilhasoft/chatguy-nlp.git  ``` <br>

2. Enter the main dir <br>
```cd chatguy-nlp  ``` 

3. Create a new env <br>
```conda create chatguy  ``` 

3. Activate env <br>
```conda activate chatguy  ``` 

4. Run Docker file 'docker-compose.yml' <br>
```sudo docker compose up -d ``` 

> It is important that the execution dir is **chatguy-nlp** and that both docker and docker swarm are installed. <br> If there is an error with docker swarm, install it and start it with ``` docker swarm init ```. <br> Then run the file *docker-compose.yml* again. <br>

The docker compose file image will install all requirements and dependencies within the environment, as well as initialize the local postgres database.

## Environment Variables
|Variables|Keys|
|------------|------------|
|POSTGRES_USER|postgres|
|POSTGRES_PASSWORD|docker|
|POSTGRES_HOST|127.0.0.1|
|POSTGRES_PORT|5432|
|POSTGRES_ADAPTER|postgresql|

After the creation of images by docker is finished, export the database credentials so that docker can connect to the application. <br>
6. Export database credentials in terminal <br>
``` 
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=docker
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_ADAPTER=postgresql
``` 

## API Reference <br>
After installing and configuring the environment and dependencies, the application is ready to run. <br>
The connection to the application is made by the FAST API by the following command: <br>
```
uvicorn --host=0.0.0.0 app:router --reload
``` 

Chatguy has 3 main endpoints: <br>
- /suggest_word <br>
- /suggest_sentences <br>
- /store_corrections <br>

> All of them receive textual content in json format as input. <br>

To perform and manage requests, the [![](https://img.shields.io/badge/Insomnia-5849be?style=for-the-badge&logo=Insomnia&logoColor=white)]() was used, but other platforms such as [![]( https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white )]() and similar can be used.

##
**POST /suggest_word** <br>
Takes an input word and returns a list of synonymous words <br>
**json request**:
``` 
{
	"texts": [
		{
			"word": "qual",
			"generate": true,
			"entity": false,
			"local": true
		},
		{
			"word": "o",
			"generate": true,
			"entity": false,
			"local": false
		},
		{
			"word": "limite",
			"generate": true,
			"entity": true,
			"local": false
		},
		{
			"word": "de",
			"generate": false,
			"entity": false,
			"local": false
		},
		{
			"word": "frases",
			"generate": true,
			"entity": false,
			"local": true
		}
	]
}
``` 

**POST /suggest_sentence** <br>
Takes an input phrase and generates synonymous phrases based on tagged entities. <br>
**json request**:
``` 
{
	"isquestion": true,
	"intent": "teste",
	"texts": [
		{
			"word": "existem",
			"generate": true,
			"entity": "existir",
			"suggestions": [
				"há",
				"existem"
			]
		},
		{
			"word": "muitas",
			"generate": true,
			"entity": false,
			"suggestions": [
				"diversas"
			]
		},
		{
			"word": "pessoas",
			"generate": true,
			"entity": "sujeito",
			"suggestions": [
				"homens",
				"mulheres",
				"crianças"
			]
		},
		{
			"word": "no",
			"generate": false,
			"entity": false,
			"suggestions": [
				"no"
			]
		},
		{
			"word": "mundo",
			"generate": true,
			"entity": false,
			"suggestions": [
				"planeta"
			]
		}
	]
}
```
**POST /store_corrections** <br>
Performs a sentence correction in the database <br>
**json request**:
```
{
	"texts": [
		[
			"olá tudo bem como você vai?1",
			"olá tudo bem como você vai?2",
			"olá tudo bem como você vai?3"
		],
		[
			"valeu demais, até!1",
			"valeu demais, até!2",
			"valeu demais, até!3"
		]
	]
}
```

## Contributing
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request


