# Chatguy
Chatguy - The powerful NLP's dataset creator. <br><br>

[![](https://img.shields.io/github/workflow/status/Ilhasoft/chatguy-nlp/tests/main)]()
[![](https://img.shields.io/appveyor/tests/Ilhasoft/chatguy-nlp)](https://github.com/Ilhasoft/chatguy-nlp/tree/main/tests)
[![Tag Version](https://img.shields.io/badge/Last%20Tag%20version-v0.5.9-green)]()
[![](https://img.shields.io/badge/Contributors-4-informational)]()
[![](https://img.shields.io/github/issues-pr/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/badge/python-3.8-informational)]() 
  
## Overview
Chatguy is a Brazilian Portuguese dataset generator. Through natural language processing techniques it is possible to generate sentences from synonymous words and entity recognition. Its main functions can be divided between generating synonymous words and generating phrases or sentences.

### Requirements: <br>
Python 3.8 <br>
Docker <br>
Docker-compose <br>
Git <br>

## Get Started

First, clone the repo: <br>
```git clone https://github.com/Ilhasoft/chatguy-nlp.git  ``` <br>

Enter the main dir <br>
```cd chatguy-nlp  ``` 

Activate env <br>
```conda activate chatguy  ``` 

Install the required packages: <br>
``` sudo apt install requirements.txt  ``` 
or
``` pip install requirements.txt  ``` <br>

Run Docker image compose <br>
```sudo docker compose up -d ``` 


## Environment Variables
|Variables|------------|
|------------|------------|
|POSTGRES_USER|------------|
|POSTGRES_PASSWORD|------------|
|POSTGRES_HOST|------------|
|POSTGRES_PORT|------------|
|POSTGRES_ADAPTER|------------|

## Development Workflow

## API Reference <br>
```uvicorn --host=0.0.0.0 app:router --reload``` 

**POST /suggest_word** <br>
Json request:
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
Json request:
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
Json request:
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


