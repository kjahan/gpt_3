import time

import openai
import gpt


openai.api_key = 'sk-greLNH6eTGTIs9cPDZnjxvjR8Tjhg7AyDTUB3Q9g'


def text_completion(prompt, max_tokens):
    return openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=max_tokens)


def run_two_examples():
    max_tokens = 200
    prompt_1 = "You order a bowl of cold tomato soup in a restaurant. It looks delicious, but they forgot to bring you a spoon. You try to drink it with a fork, but"
    response_1 = text_completion(prompt_1, max_tokens)
    print("-------------------------")
    print(prompt_1)
    print(response_1)
    print("-------------------------")
    prompt_2 = "You are eight years old. When you were born, your mother was in Barcelona and your father was in Tokyo, so you were born in"
    response_2 = text_completion(prompt_2, max_tokens)
    print(prompt_2)
    print(response_2)
    print("-------------------------")


def run_text_compl_experiments(filename):
    max_tokens = 200
    with open(filename) as fp:
        for line in fp:
            prompt = line.strip()
            print(prompt)
            print("======================================== SAMPLE 1 ========================================")
            response_1 = text_completion(prompt, max_tokens)
            print(response_1["choices"][0]["text"])
            print("======================================== SAMPLE 2 ========================================")
            time.sleep(5)
            response_2 = text_completion(prompt, max_tokens)
            print(response_2["choices"][0]["text"])
            print("================================================================================")
            # break


if __name__ == "__main__":
    filename = "data/prompts.txt"
    run_text_compl_experiments(filename)
