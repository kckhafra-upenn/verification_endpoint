from flask import Flask, request, jsonify
from flask_restful import Api
import json
# import eth_account
# import algosdk
import json

app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False

@app.route('/verify', methods=['GET','POST'])
def verify():
    contents = request.get_json(silent=True)
    content = json.dumps(contents["payload"])
    #Check if signature is valid

    result = True #Should only be true if signature validates
    if content["platform"]=="Ethereum":
        result=True
        # eth_account.Account.enable_unaudited_hdwallet_features()
        # acct, mnemonic = eth_account.Account.create_with_mnemonic()

        # eth_pk = acct.address
        # eth_sk = acct.key

        # payload = content["payload"]

        # eth_encoded_msg = eth_account.messages.encode_defunct(text=payload)
        # eth_sig_obj = eth_account.Account.sign_message(eth_encoded_msg,eth_sk)
        
        # # print( eth_sig_obj.messageHash )  
        # if eth_account.Account.recover_message(eth_encoded_msg,signature=eth_sig_obj.signature.hex()) == eth_pk:
        #     result=True
        
    # elif content["payload"]["platform"]=="Algorand":
    #     payload = content["payload"]

    #     algo_sk, algo_pk = algosdk.account.generate_account()
    #     algo_sig_str = algosdk.util.sign_bytes(payload.encode('utf-8'),algo_sk)

    #     if algosdk.util.verify_bytes(payload.encode('utf-8'),algo_sig_str,algo_pk):
    #         print( "Algo sig verifies!" )
    #         result=True
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
