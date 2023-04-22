import requests


parameters={
"amount":10,
"type":"boolean",
}
question_link = requests.get(url="https://opentdb.com/api.php",params=parameters)
question_link.raise_for_status()
data= question_link.json()
question_data = data["results"]

