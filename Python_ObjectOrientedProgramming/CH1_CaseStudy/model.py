# An implementation almost always needs to have an __init__() method.
# Ther's another special method that can really help: The __repr__() method is used to create a representation of the object.
# __repr__() method is used to createa representation of the object. The representations ia string that generally has the syntax of a python expression to rebuild the object.

"""
The representation is a string that generally has the syntax of a python expression to rebuild the object. For simple numbers, it's the number.

For a simple string, it will include the quotes.  for complex objects, it will have all the necessary 
python punctuation, including all the details of the class and the state of the object.mro

* We will often use an f-string with the class name and the attribute values.

Here's the start of a class, Sample, which seems to capture all the features of a single sample:

"""
from typing import Optional

class Sample:

    def __init__(
        self, 
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        species: Optional[str] = None,

    ) -> None:

        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification: Optional[str] = None
    
    def __repr__(self) -> str:
        if self.species is None:
            known_unknown = "UnknownSample"
        else:
            known_unknown = "knownSample"
        
        if self.classification is None:
            classification = ""
            print("classification value is set to None", classification)

        else:
            classification = f", {self.classification}"
            print("classification is assigned to", classification)
        
        return (
            f"{known_unknown}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length = {self.petal_length}, "
            f"petal_width = {self.petal_width}, "
            f"species={self.species!r}"
            f"{classification}"
            f")"
        )
    
    def classify(self, classification:str) -> None:
        self.classification = classification

    def matches(self) -> bool:
        return self.species == self.classification
    

if __name__ == "__main__":
    s2 = Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa")
    print(s2)