```markdown
# AI Code Reviewer for git post-commit hook

[![Build Status](https://travis-ci.com/yourusername/ai-code-reviewer.svg?branch=master)](https://travis-ci.com/yourusername/ai-code-reviewer)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project uses OpenAI's GPT-3 model to provide code reviews for each git commit executed locally. The code review is performed by analyzing the git diff between the new commit and the previous one.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-code-reviewer.git
```

2. Navigate to the project directory:

```bash
cd ai-code-reviewer
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Usage

1. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-openai-api-key'
```

2.  Copy the `post-commit.sample` file to `.git/hooks/post-commit`:

```bash
cp post-commit.sample .git/hooks/post-commit
```


3. Run the Flask application:

```bash
python main.py
```

The application will start and be accessible at `http://localhost:8000`.

## Running Tests

To run the tests, execute the following command:

```bash
python -m unittest main-test.py
```

## Contributing

Contributions are welcome. Please open an issue to discuss your idea or submit a Pull Request.

## License

````
MIT License

Copyright (c) 2023 Hernan Seghetti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
```