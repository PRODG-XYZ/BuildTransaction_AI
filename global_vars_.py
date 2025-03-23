import os


global DEFINED_CHAIN
DEFINED_CHAIN = "AirSwapFlare"

def modify_global_chain(
    new_value: str,
):
    """
    Modify the global chain variable
    :return:
    """
    global DEFINED_CHAIN
    DEFINED_CHAIN = new_value



tx_fetch_endpoints = {
    'ETH_MAINNET': 'https://mainnet.infura.io/v3/{}',
    'AVAX/USDT': 'https://api.avax.network/ext/bc/C/rpc',
    'FLARE': "https://flare-api.com/ftso/{}/price",
    'UNIV3': "https://api.solanabeach.io/v1/transactions/{}",
}

solidity_contracts_mapper = {
    'AirSwapFlare': {
        'verifier_source': 'contracts/TradeVerifierFlare.sol',
        'executor_source': 'contracts/TradeExecutorAvalanche.sol',
    },
    'UniV3LFJ': {
        'verifier_source': 'contracts/TradeVerifierUniV3.sol',
        'executor_source': 'contracts/TradeExecutorLFJ.sol',
    },
}

# Access environment variables
private_key = os.getenv("PRIVATE_KEY")
infura_project_id = os.getenv("INFURA_PROJECT_ID")
frontend_domain = os.getenv("FRONTEND_DOMAIN")
frontend_base_url = os.getenv("FRONTEND_BASE_URL")
deepseek_domain = os.getenv("DEEPSEEK_API_URL")
deepseek_key = os.getenv("DEEPSEEK_KEY")

model_specifications = {
    'infura_project_id': infura_project_id,
    'eth_mainnet_url': tx_fetch_endpoints['ETH_MAINNET'],
    'eth_method': 'eth_getTransactionByHash',
    'AVAX/USDT': {
        'tx_hash': 'FvwEAhmxKfeiG8SnEvq42hc6whRyY3EFYAvebMqDNDGCgxN5Z',
        'model': {
            'AirSwapFlare': {
                solidity_contracts_mapper['AirSwapFlare'],
            },
        },
        'tx_details': {
            'tx_fetch_url': tx_fetch_endpoints['AVAX/USDT'],
            'tx_fetch_price': tx_fetch_endpoints['FLARE'],
        },
    },
    'SOL/USDC': {
        'tx_hash': '',
        'model': {
            'UNIV3LFJ': {
                solidity_contracts_mapper['UniV3LFJ'],
            },
        },
        'tx_details': {
            'tx_fetch_url': tx_fetch_endpoints['FLARE'],
            'tx_fetch_price': tx_fetch_endpoints['UNIV3'],
        }
    }
}

default_payload_dict = {
    "jsonrpc": "2.0",
    "method": model_specifications['eth_method'],  # method function to call, e.g., eth_getTransactionByHash
    "params": [],  # tx_hash of the token pair
    "id": 1,
}

input_params = {
    'tx_pair': 'AVAX/USDT' ,
    'tx_hash': 'FvwEAhmxKfeiG8SnEvq42hc6whRyY3EFYAvebMqDNDGCgxN5Z',
    'fetch_tx_dict': None,
    'method_call': 'eth_getTransactionByHash',
    'payload_': default_payload_dict,
    'url_': tx_fetch_endpoints['avax_tx'],
}