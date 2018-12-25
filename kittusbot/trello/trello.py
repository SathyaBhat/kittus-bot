from base.scaffold import trello_token, trello_api_key, trello_data, trello_api_url, querystring, log
from requests import post

def add_to_trello_list(list_name, what_to_add, update, data):
    url = "{}/{}".format(trello_api_url,what_to_add)
    log.debug("Got data: \n data: {}".format(data))
    if data != []:

        querystring['idList'] = trello_data['boards']['lists'][list_name]
        querystring['name'] = " ".join(data)
        querystring['desc'] = 'Created by {}'.format(update.message.from_user.username)
        request = post(url, data=querystring)
        status_code = request.status_cod
        log.info("POST to trello returned {} status".format(status_code))
        message = 'Card added to Trello'
    else:
        message = "Nothing to add, not creating a card"
        status_code = 400
    return message, status_code
