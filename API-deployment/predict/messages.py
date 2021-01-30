explain_expectations = """<h1> Welcome! </h1>
        This API has been built by the super team of Orhan Nurkan, Naomi Thiru, Christophe Giets and Sara Silvente.
        <h2> What is this? </h2>
        Our API receives data on features of properties for sale in Belgium in JSON format and returns a prediction of properties' price.
        <p>
        <h3> Tell me more! </h3>
        Below are the 16 keys you can use to send your data in the appropriate format. To get the prediction, you must enter a value for the features <code>area</code>, <code>property-type</code>, 
        <code>rooms-number</code> and <code>zip-code</code> (they are mandatory features). 
        The remaining features are optional.</p>
        <p> Each feature accepts a specific data type (<code>int</code>, <code>bool</code> and <code>str</code> stand for <i>integer</i>, <i>boolean</i> and <i>string</i>, respectively). </p>
        <p> The features <code>property-type</code> and <code>building-state</code> accept only one of the values that are indicated (in capitals). </p>
        <xmp>
            {
        "data": {
                "area": int,
                "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
                "rooms-number": int,
                "zip-code": int,
                "land-area": Optional[int],
                "garden": Optional[bool],
                "garden-area": Optional[int],
                "equipped-kitchen": Optional[bool],
                "full-address": Optional[str],
                "swimmingpool": Optional[bool],
                "furnished": Optional[bool],
                "open-fire": Optional[bool],
                "terrace": Optional[bool],
                "terrace-area": Optional[int],
                "facades-number": Optional[int],
                "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
        }
    } </xmp>
        """
api_is_alive = """<h1>Alive!</h1> 
    <a href= '/predict'>Let's use this API!</a>"""
