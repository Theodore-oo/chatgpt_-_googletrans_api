import openai

openai.api_key = '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'

aphayay = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "Where is Myanmar located?"}
    ]
)

aphayay_cleaned = aphayay.choices[0].message.content

print(aphayay_cleaned)

