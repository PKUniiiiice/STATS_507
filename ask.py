from openai import OpenAI

client = OpenAI(api_key='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')
import sys

def get_chatgpt_response(question):
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",  # Specify the model here
          messages = [ # Change the prompt parameter to messages parameter
                {'role': 'user', 'content': f'{question}'}
    ],
        temperature=1,
        max_tokens=1000)
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py 'your question'")
    else:
        question = sys.argv[1]
        answer = get_chatgpt_response(question)
        print(answer)

