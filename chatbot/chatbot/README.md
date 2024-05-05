from this directory run

. ../env/bin/activate

to activate python venv

then run 

python manage.py runserver <PORT>

replcae <PORT> with actual port number you want to run applucation on


the api is listening on endpoint /prompt for example if port was given as 8080 then the url for chatbot will be http://127.0.0.1:8080/prompt

the api expects input in form of 
{
    "username": <USERNAME>,
    "prompt": <PROMPT>
}

where both fields are of type string