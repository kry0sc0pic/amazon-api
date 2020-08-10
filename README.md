# Amazon API

An API to scrape details from the Amazon Website and return the details
in a json format.

This uses the selenium library to scrape the data.

### Setup Selenium

-   I have documented this in my [PokeVoter Repository](https://github.com/krishaayjois21/PokeVoter#get-started)

### Pre Requisites

-   Python 3
-   chromedriver

### Get Started

-   Install dependecies using `pip install -r requirements.txt`
-   open the `api.py` file
-   set you port number and host ip
-   It should look like this

```python
if __name__ == '__main__':
	app.run(host='<IP ADDRESS>' port=<PORT-NUMBER>)
```

### Request

Arguments:

-   `url` this is the link to amazon product page 

A Request looks like this

-   `http://<IP>:<PORT>/api/amazon?url=<PRODUCTURL>`

### Response

```json
{
	"price": 11.55,
	"name": "My Cool Product",
	"image_link": "Image Link",
	"manafacturer_name": "My Cool Product Inc.",
	"manafacturer_link": "MyCoolProcduct.com",
	"availability": "In Stock",
	"number_of_ratings": 43,
	"questions_answered": 23,
}
```
