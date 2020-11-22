from flask import Blueprint, request

rpc_calls = Blueprint('rpc', __name__)

@rpc_calls.route("updateFeed", methods=["POST"])
def updateFeed():
    print(request.args.get('feedId'))
    return {'name': 'updateFeed'}
