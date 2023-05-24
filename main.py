import openai


openai.api_key = '' #openAI_key


conversation_history = []

while True:
    user_input = input('Введіть повідомлення: ')
    conversation_history.append(user_input)
    context = ' '.join(conversation_history)

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=context,
        temperature=0.7,
        max_tokens=500,
        n=1,
        stop=None
    )

    model_reply = response.choices[0].text.strip()
    conversation_history.append(model_reply)

    print('Модель:', model_reply)
