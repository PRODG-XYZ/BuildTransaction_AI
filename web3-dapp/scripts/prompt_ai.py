import sys

import openai
from API_ENV import *
import os
from openai import OpenAI

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(
            __file__
        ),
        '..'
    )
)

sys.path.append(
    project_root
)
deepseek_domain = DEEPSEEK_API_URL
deepseek_key = DEEPSEEK_KEY
client = OpenAI(api_key=deepseek_key, base_url=deepseek_domain)


def send_prompt(
    position: str,
    amount: str,
    ticker: str,
    slippage: str,
    prompt: str = None,
):
    """
    
    :param prompt:
    :param position:
    :param amount:
    :param ticker:
    :param slippage:
    :return:
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": ''.join(
                    [
                        "Generate the structure of the process to execute a transaction on solana using the following format, where each component is represented as a shape. For each shape fill in the '[]' parts. '{shape: [], data: []}' ",
                        "for each step of the transaction, use these predefined shapes as aliases for the following steps: \n - rectangle: on-chain action for verification and validation, \n - diamond: real time data feed, \n - circle: user's interaction",
                        f"The transaction to build is {position}ing {amount} {ticker}, where the slippage is set as {slippage}%"]
                ),
            },
        ],
        stream=False,
        # response_format=
    )
    
    print(response.choices[0].message.content)
    return response.choices[0].message.content
    
def prompt_reformatter_(
    output: str,
):
    """
    
    :param output:
    :return:
    """
    split_out = output.split("`", -1)
    shapes_list = []
    info_list = []
    for i in range(
        len(
            split_out
        ) - 1
    ):
        if i % 2 != 0:
            print(
                i,
                split_out[i]
            )
            shapes_list.append(split_out[i])
        else:
            info_list.append(split_out[i])
    
    return shapes_list

if __name__ == '__main__':
    
    output = send_prompt(
        # prompt='Generate the structure of the process to execute a transaction on solana using the following format, where each component is represented as a shape. For each shape fill in the "[]" parts. "{shape: [], data: []};" for each step of the transaction, use these predefined shapes as aliases for the following steps: - rectangle: on-chain action for verification and validation - diamond: real time data feed - circle: user\'s interaction The transaction to build is buying 1 AVAX, where the slippage is set as 0.5%',
        position='buy',
        amount=1,
        ticker='SOL/USDC',
        slippage=1,
    )
    shapes_list = prompt_reformatter_(output)
    breakpoint()