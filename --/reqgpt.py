import openai

openai.organization = "org-ec0bVXFOx1ccTsgi26QxvpR9"
openai.api_key = "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"



def categorisation (argu):
    # Define the conversation with a system message followed by a user message
    conversation = [
        {"role": "system", "content": "You are a photo categorization bot."},
    ]


    # Additional context and instructions
    context = "Je vais donner des arguments d'une photo, et tu vas devoir classer dans l'une des catégories. La photo peut être dans une seule catégorie."
    categories = "Paysages; fleur; animaux; voitures, bateaux, personnes, bâtiments, illustration"
    instruction = "La réponse doit être seulement la catégorie, juste Voiture par exemple "

    # Add user message with context, categories, and instruction
    user_message = {
        "role": "user",
        "content": f"{context} Les catégories sont : {categories}. {instruction}, les arguments sont : {argu}",
    }

    # Add the user message to the conversation
    conversation.append(user_message)

    # Generate a response using the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    # Print the assistant's response
    return(response['choices'][0]['message']['content'])
    

