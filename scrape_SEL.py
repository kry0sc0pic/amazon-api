from selenium import webdriver , common
from time import sleep
def getInfo(URL):
    option = webdriver.ChromeOptions()
    option.add_argument('-incognito')
    browser = webdriver.Chrome(options=option)
    browser.get(URL)
    sleep(1)
    try:
        price = browser.find_element_by_xpath(
            '//*[@id="priceblock_ourprice"]')
        price = price.text
    except common.exceptions.NoSuchElementException:
        price = '--'

    try:
        title = browser.find_element_by_xpath('//*[@id="productTitle"]')
        title = title.text
    except common.exceptions.NoSuchElementException:
        title = '-----'

    try:
        image = browser.find_element_by_xpath('//*[@id="landingImage"]')
        imgLink = image.get_property('src')
    except common.exceptions.NoSuchElementException:
        imgLink = ' '

    try:
        manufacturer = browser.find_element_by_xpath('//*[@id="bylineInfo"]')
        manufacturerName = manufacturer.text
        manufacturerLink = manufacturer.get_property('href')
    except common.exceptions.NoSuchElementException:
        manufacturer = ' '
        manufacturerLink = ' '
    try:
        availablility = browser.find_element_by_xpath('//*[@id="availability"]/span')
        availablility = availablility.text
    except common.exceptions.NoSuchElementException:
        availablility = 'Cannot be determined'


    try:
        n_ratings = browser.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
        n_ratings = n_ratings.text
        n_rate, _ = n_ratings.split(' ')
    except common.exceptions.NoSuchElementException:
        n_rate = '0'




    try:
        questions = browser.find_element_by_xpath('//*[@id="askATFLink"]/span')
        questions = questions.text
        n_questions, w1, w2 = questions.split(' ')
    except common.exceptions.NoSuchElementException:
        n_questions = '0'


    info = {'price':price , 'name':title , 'image_link':imgLink , 'manufacturer_name': manufacturerName , 'manufacturer_link': manufacturerLink ,  'availability': availablility , 'number_of_ratings': n_rate , 'questions_answered':n_questions}
    browser.close()
    return info


# print(getInfo('https://www.amazon.com/Splitter-Bluesky-Powered-Distributor-Amplifier/dp/B075CXPCQY/ref=pd_sbs_23_1
# /139-3597627-4491969?_encoding=UTF8&pd_rd_i=B075CXPCQY&pd_rd_r=afe227de-26c7-48a4-855a-ce8d48f3ea30&pd_rd_w=0zrea
# &pd_rd_wg=kmtqg&pf_rd_p=d9804894-61b7-40b3-ba58-197116cffd9d&pf_rd_r=P3ME5WXA9N5WXETXD5TT&psc=1&refRID
# =P3ME5WXA9N5WXETXD5TT'))

