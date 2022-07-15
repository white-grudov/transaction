from web3 import Web3 

ADRESS_FROM = '0xD1BeCD7FF6D9Df82C81388fc9C617F78E4297B53'
ADRESS_TO = '0xc53D6C0148ddC28Efe623Ab3aD54da5C7779b25C'

PRIVATE_KEY = '675411650619921ca2e88d910a0831a40aed42f7bad1e9649e2f75a0b5f24683'

ENDPOINT = 'https://ropsten.infura.io/v3/9db3174e0d9340e9b5a6b8478bf457e4'
w3 = Web3(Web3.HTTPProvider(ENDPOINT))

tx = {
    'nonce': w3.eth.get_transaction_count(ADRESS_FROM),
    'to': ADRESS_TO,
    'value': w3.toWei(0.01, 'ether'),
    'gas': 100000,
    'gasPrice': w3.toWei('99', 'gwei'),
    'data': bytes('daniil_bilohrudov', 'utf_8')
}

signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(w3.toHex(tx_hash)) 
