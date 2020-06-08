from flask import Flask, request
import scrape_SEL as scraper
import json
from datetime import datetime
app = Flask(__name__)


@app.route('/api/amazon')
def amazonAPI():
    response = {}
    URL = str(request.args['url'])
    productInfo = scraper.getInfo(URL)
    response = productInfo
    response['product_url'] = URL

    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='192.168.0.194', port=9200)
