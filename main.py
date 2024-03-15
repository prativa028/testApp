import openai

openai.api_key = "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"
model_engine = "text-davinci-003"
prompt = str(input())


completion = openai.Completion.create(
    engine = model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temprature=0.5

)

response = completion.choices[0].text
print(response)
