from flask import Flask, request
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
app = Flask(__name__)


@app.route('/post', methods=['POST'])
def post_json():
    data = request.get_json()
    commit_message = data['commit_message'] or ''
    commit_description = data['commit_description'] or ''
    commit_code_changes = data['commit_code_changes'] or ''
    files_changed = data['files_changed'] or ''

    chat_model = "gpt-3.5-turbo"
    prompt = '''
        Your task is to review pull requests as a senior software developer. Instructions:
        - Do not give positive comments or compliments.
        - Provide comments and suggestions ONLY if there is something to improve.
        - Please evaluate twice the suggestions given by the AI.
        - Write the comment in Markdown format like github. Group the comments by file in different sections.
        - It is very important the readability of the comments.
        - Use the given description only for the overall context and only comment the code.
        - IMPORTANT: NEVER suggest adding comments to the code.
        - and take the commit message and description into account when writing the response.
    '''
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Commit message: {commit_message}\n"
                                    f"Commit description: {commit_description}\n"
                                    f"Commit code changes: {commit_code_changes}\n"
                                    f"Files changed: {files_changed}"}
    ]

    response = client.chat.completions.create(
      model=chat_model,
      messages=messages
    )

    return response.choices[0].message.content


if __name__ == '__main__':
    app.run(port=8000, debug=True)
