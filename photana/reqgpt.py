import openai

openai.organization = "org-#####"
openai.api_key = "sk-#####"



def categorisation (argu):
    # Define the conversation with a system message followed by a user message
    conversation = [
        {"role": "system", "content": "You are a photo categorization bot."},
    ]


    # Additional context and instructions
    context = "Je vais donner des arguments d'une photo, et tu vas devoir classer dans l'une des catégories. La photo peut être dans une seule catégorie."
    categories = "Paysages ; Fleurs ; Animaux ; Voitures ; Bateaux ; Personnes ; Bâtiments ; Illustration ; Divers ; Nourriture ; Art abstrait ; Événements spéciaux ; Sport et loisirs ; Mode ; Musique ; Voyages"
    instruction = "Tu n'a le droit que de renvoyé la categorie, aucune phrase ne seras accepté, juste Voiture par exemple"

    # Add user message with context, categories, and instruction
    user_message = {
        "role": "user",
        "content": f"{context} Les catégories sont : {categories}. {instruction}, les arguments sont : {argu}",
    }

    # Add the user message to the conversation
    conversation.append(user_message)

    # Generate a response using the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=conversation,
    )

    # Print the assistant's response
    return(response['choices'][0]['message']['content'])
    

