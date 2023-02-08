<div align="center">

# Chatguy <img src="https://user-images.githubusercontent.com/72058182/198705259-1aa1824b-f09b-4d4c-a697-65281856f0f5.png" width="auto" height="40px">
### The powerful NLP's dataset creator.  <br><br>

[![CI](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/ci-tests.yml/badge.svg)](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/ci-tests.yml)
[![Docker Image CI](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/docker-image.yml)
[![Tests](https://github.com/Ilhasoft/chatguy-nlp/actions/workflows/Tests.yml/badge.svg)]()
[![](https://img.shields.io/github/last-commit/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/contributors/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/issues-pr/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/v/tag/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/v/release/Ilhasoft/chatguy-nlp)]()
[![](https://img.shields.io/github/languages/top/Ilhasoft/chatguy-nlp)]()

  
</div>

## Overview
Chatguy is a Brazilian Portuguese dataset generator. Through natural language processing techniques it is possible to generate sentences from synonymous words and entity recognition. Its main functions can be divided between generating synonymous words and generating phrases or sentences.

### Requirements: <br>

[![](https://img.shields.io/badge/python-3.8.13-9cf)]()
[![](https://img.shields.io/badge/git-2.34.1-9cf)]()
[![](https://img.shields.io/badge/conda-4.5.11-9cf)]()
[![](https://img.shields.io/badge/docker-23.0.0-9cf)]()

## Get Started

1. First, clone the repo: <br>
```git clone https://github.com/Ilhasoft/chatguy-nlp.git  ``` <br>

2. Enter the main dir <br>
```cd chatguy-nlp  ``` 

3. Create a new env <br>
```conda create chatguy  ``` 

3. Activate env <br>
```conda activate chatguy  ``` 

4. Install requirements <br>
*you can use the ```ls``` command to check if the requirmenets.txt file is showing* <br>
```pip install requirements.txt ```


4. Run Docker file 'docker-compose.yml' <br>
```sudo docker compose up -d ``` 

> It is important that the execution dir is **chatguy-nlp** and that both docker and docker swarm are installed. <br> If there is an error with docker swarm, install it and start it with ``` docker swarm init ```. <br> Then run the file *docker-compose.yml* again. <br>

The docker compose file image will install all requirements and dependencies within the environment, as well as initialize the local postgres database.

## Environment Variables
After the creation of images by docker is finished, export the database credentials so that docker can connect to the application. <br>


6. Export database credentials in terminal <br>
``` 
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=docker
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_ADAPTER=postgresql
``` 

7. Run Redis image server <br>
``` docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest ```


## API Reference  <br>
After installing and configuring the environment and dependencies, the application is ready to run. <br>
*Make sure you are in the correct dir: ```chatguy-nlp/Chatguy```* <br>

The connection to the application is made by the FAST API by the following command: <br>
```
uvicorn --host=0.0.0.0 app:router --reload
``` 

Chatguy has 4 main endpoints: <br>
- /suggest_word <br>
- /suggest_sentences <br>
- /store_corrections <br>
- /recover_sentences <br>

> All of them receive textual content in json format as input. <br>

To perform and manage requests, the [![](https://img.shields.io/badge/Insomnia-5849be?style=for-the-badge&logo=Insomnia&logoColor=white)]() was used, but other platforms such as [![]( https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white )]() and similar can be used.

## Requests and expected responses/outputs <br>

<details> <summary> POST/suggest_words  </summary><br>
0.0.0.0:8000/suggest_words  | Description: Takes an input word and returns a list of synonymous words
<p>

![Suggest_words](https://user-images.githubusercontent.com/72058182/217551555-a29775c2-03a9-4cd2-bf82-41cc5f338667.png)

Request code:

``` 
{
	"texts": [
		{
			"word": "formiga",
			"generate": true,
			"entity": false,
			"local": true
		},
		{
			"word": "qual",
			"generate": true,
			"entity": false,
			"local": false
		},
		{
			"word": "café",
			"generate": false,
			"entity": true,
			"local": false
		},
		{
			"word": "árvore",
			"generate": false,
			"entity": false,
			"local": false
		},
		{
			"word": "pessoa",
			"generate": false,
			"entity": false,
			"local": true
		}
	]
}
```


</p>
</details>


<details> <summary> POST/suggest_sentences </summary><br>
0.0.0.0:8000/suggest_sentences | Description: Takes an input phrase and generates synonymous phrases based on tagged entities. It returns a str token.

<p>

![Suggest_sentences](https://user-images.githubusercontent.com/72058182/217324443-5b869415-fc76-40f2-9867-11db02ec511a.png)

Request code:

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

</p>
</details>


<details> <summary> POST/recover_sentences </summary><br>
0.0.0.0:8000/recover_sentences | Description: Receives the token generated by the 'generate_sentences' route and returns the generated phrases.
<p>


![Recover_sentences](https://user-images.githubusercontent.com/72058182/217324656-e928bf71-308f-4dba-8a64-234a32ae087b.png)

Request code:

```
{"token":"generated_token"}
```

</p>
</details>



<details> <summary> POST/store_corrections </summary><br>
0.0.0.0:8000/store_corrections | Description: Performs a sentence correction in the database.
<p>

![Store_corrections](https://user-images.githubusercontent.com/72058182/217324933-9585f9a3-078f-49a2-b630-2b3658b529e8.png)

Request code:

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

</p>
</details>



## Contributing
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request


