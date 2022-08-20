const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'db553e6076msh6431e04f8d54b9ep1c4067jsna3eb30d8d7c2',
		'X-RapidAPI-Host': 'healthgraphic-healthgraphic-v1.p.rapidapi.com'
	}
};

fetch('https://healthgraphic-healthgraphic-v1.p.rapidapi.com//api.healthgraphic.com/v1/conditions/vomit', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));