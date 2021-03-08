# API-deployment
Update:
API: http://cnos.herokuapp.com/

Website built by Web Developer [Nelly Caballero](https://github.com/NeryCaballero) based on our [API](https://github.com/naomithiru/End-to-end-Machine-Learning-Project/blob/master/API-deployment/app.py)
https://nerycaballero.github.io/Bouman-Johnson-housing-project/housing-project.html

# 1. The Project
Following a succesful Data Scraping project of Real Estate websites of Belgium, Data Cleaning and Visualization project to clean, study and understand the data, and Machine Learning Project to apply Regression models to predict house prices, the team was challenged to create an API through which data can be received and predicted home prices can be outputted.

The API is to be used by the web developers to create a website around. This repository contains all the information and resources that went into achieving this.


## 1.1. The Team
This project was a collaborative effort between four members of the *Bouwman2* promotion at [BeCode](https://github.com/becodeorg), Brussels, in December 2020. The team comprised of [Orhan Nurkan](https://github.com/orhannurkan), [Christophe Giets](https://github.com/gietsc), [Sara Silvente](https://github.com/silventesa), and [Naomi Thiru](https://github.com/naomithiru)

# 2. Contents
For quick reference, the repository is divided into the relevant sections, each with it's own resources and outline.  
2.1. [The model](#model)  
2.2. [Preprocessing](#prep)  
2.3. [Prediction](#pred)  
2.4. [The API](#api)  
2.5. [Docker](#doc)  

<a name="model"></a>
## 2.1. The model
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Machine Learning model|Belgium Real Estate Dataset |Regression|`pandas`, `numpy`, `sklearn`, `pickle`|https://github.com/orhannurkan/API-deployment/blob/main/app/model/model.py|

The features used in this prediction model are:</br> `'house_is'`,`'property_subtype'`, `'postcode'`, `'area'`,`'rooms_number'`, `'equipped_kitchen_has'`, `'garden'`, `'garden_area'`,`'terrace'`, `'terrace_area'`, `'furnished'`, `'swimming_pool_has'`,`'land_surface'`, `'building_state_agg'`, `'open_fire'`, `'longitude'`,`'latitude'`

The `model.py` file contains all the code used to train the model. The dataset is available as well in [assets](https://github.com/orhannurkan/API-deployment/tree/main/assets)

The model is then [pickled](https://docs.python.org/3/library/pickle.html) to be used for prediction using the function `pickle.dump()`


<a name="prep"></a>
## 2.2. Preprocessing
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Data preprocessing |[JSON input](#input)|Function |`python`, `JSON Schema Validator`|https://github.com/orhannurkan/API-deployment/tree/main/preprocessing |

The input data is preprocessed according to the model requirements(formats, number of variables). The preprocessing function employs the use of [JSON Schema Validator](https://github.com/Julian/jsonschema) to define the variables and expected values. 

The expected **JSON_input** <a name="input"></a>, and the appropriate formats are: </br>
**Mandatory data:** {`"area":[int]`,`"property-type": ["APARTMENT" | "HOUSE" |  "OTHERS"]`,`"rooms-number":[int]`,`"zip-code":[int]`}

**Optional data:** {`"land-area":[int]`,`"garden":[bool]`,`"garden-area":[int]`,`"equipped-kitchen": [bool]`,`"full-address":[str]`,`"swimmingpool":[bool]`,`"furnished":[bool]`,`"open-fire":[bool]`,`"terrace":[bool]`,`"terrace-area":[int]`,`"facades-number":[int]`,`"building-state":["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]` }


- Each feature accepts a specific data type `int, bool and str` (for integer, boolean and string respectively).  
- The features property-type and building-state accept one value out of a list of options, in uppercase.  


**Important points to note:**  
* All optional features have a default null value, which is coverted to False or 0, for the prediction model.  
* The category names are converted to match the feature names of the training dataset to avoid conflicts.  
* Location data; Using Google APIs, the feature `full-address` is parsed and `longitude` & `latitude` fatures extracted, which are very important for better prediction accuracy. 
* Dummy values are created for catgorical and boolean values, for the prediction model.

The preprocessing step returns a `json_input_cleaned` output.

<a name="pred"></a>
## 2.3. Prediction
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Prediction|JSON_input_cleaned|Function|`python`, `pickle`| (https://github.com/orhannurkan/API-deployment/tree/main/predict)|

The prediction file `prediction.py` takes the `json_input_cleaned` and returns a [JSON output](#output), consisting of the house price prediction, and either an error message, or a success message.


<a name="api"></a>
## 2.4. The API
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Deployment|JSON_input|GET, POST|`Flask`, `request`, `jsonify`|(https://github.com/orhannurkan/API-deployment/blob/main/app.py)|

The API has been developed with [Flask](https://flask.palletsprojects.com/en/1.1.x/), one of the most popular Python web application frameworks.
The API gets [JSON_input](#input), which is [preprocessed](#prep) according to the model requirements, and returns a property price prediction based on this [model](#model).

The 16 keys to be used to send user data in the appropriate format are outlined [here](#input).  
To get the prediction, one must at minimum enter a value for the features `area`, `property-type`, `rooms-number` and `zip-code`.
The remaining features are optional and will use default values if none are provided.

### Outline

API Returns json data with predicted house price.
* **Url:**
    
    http://cnos6.herokuapp.com/

* **Method:**

  `GET`, `POST`
  
* **Data Params**
  
   [JSON_input](#input)

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `{"prediction": House price ",
                    "extra info": message }`
 
* **Error Response:**

  * **Code:** 406 Not Acceptable  <br />
    **Content:** `{ error : "Sorry, you should send minimum 4 mandatory features. You can GET more info by GET method to /predict link" }`



<a name="doc"></a>
## 2.5. Docker
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Environment|`Dockerfile`, `requirements.txt`,`Procfile`|||https://github.com/orhannurkan/API-deployment/blob/main/Dockerfile| |

The `Dockerfile` contains the code to start an environment from the latest version of Ubuntu. Once your environment is running on the latest Ubuntu version, it will install the latest version of Python (`python3.8.5`) and `pip` (packages installer for Python). Then with `pip`, it will install all the necessary packages located in the `requirements.txt` file.

If you are unfamiliar with some concepts on Docker, we recommend you to check this documentation on Docker : https://github.com/becodeorg/BXL-Bouman-2.22/tree/master/content/05.deployment/2.0.Docker 

## 2.6. Heroku
In case you would like to try our API and run on container on a Web Application Service, you can do this on Heroku.
The following documentation will help you to try our API with our environment prepared on Docker : https://github.com/becodeorg/BXL-Bouman-2.22/tree/master/content/05.deployment/4.Web_Application
