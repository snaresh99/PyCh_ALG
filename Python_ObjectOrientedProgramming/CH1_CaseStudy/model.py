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
        s
        * Thelf.classification = classification

    def matches(self) -> bool:
        return self.species == self.classification
    
"""
It also seems clear the training data class is an acceptable place to record the various hyperparameter trials.
This means the training data class can identify which of the hyperparameter trials. This means the training data class can identify,
which of the hyperparameter instances has a value of k that classifies irises with the highest accuracy.

This means the training data class can identify which of the hyperparameter trials. This means the training data class can identify
which of the hyperaparameter instances has a value of k that classifies irises with the highest accuracy.
* There are multiple, related state changes here.
* In this case, both the hyperparameter and training data classes will do part of the work.
* The system as a whole will change state as individual elements change state.
* This is sometimes referred to as emergent behavior.

* Rather than writing a monster class that does many things, we've written smaller classes that collaborate to achieve the expected goals.

"""

class Hyperparameter:
    """ A hyperparameter value and the overall quality of the 
    classification."""

    def __init__(self, k:int, training: "TrainngData")-> None:
        self.k = k
        self.data = weakref.ReferenceType["TrainingData"] = weakref.ref(training)
        self.quality: float
    """
    Note: How we write type hints for classes not yet defined.
    When a class is defined later in the file, any reference ot hte yet to be defined class is a forward reference.
    The forward references to the not yet defined Training Data class are provided as strings, not the simple class name.
    When mypy is analyzing the code, it resolves the strings into proper class names.
    
    """

if __name__ == "__main__":
    s2 = Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa")
    print(s2)