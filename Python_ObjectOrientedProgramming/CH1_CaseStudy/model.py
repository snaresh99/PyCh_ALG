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
    When a class is defined later in the file, any reference ot the yet to be defined class is a forward reference.
    The forward references to the not yet defined Training Data class are provided as strings, not the simple class name.
    When mypy is analyzing the code, it resolves the strings into proper class names.
    
    """

    def test(self) -> None:
        """ Run the entire test suite. """
        training_data: Optional["TrainingData"] = self.data()
        if not training_data:
            raise RuntimeError("Broken weak reference")
        pass_count, fail_count = 0,0

        for sample in training_data.testing:
            sample.classification = self.classify(sample)
            if sample.matches():
                pass_count += 1
            else:
                fail_count += 1
        self.quality = pass_count / (pass_count + fail_count)

    """
    * We start by resolving the weak reference to the training data. This will raise an exception if there's a problem. 
    For each testing sample, we classify the sample setting the sample's classification attribute. 
    The matches method tells us if the model's classification matches the known species. 
    finally, the overall quality is measured by the fraction of tests that passed. 
    - we can use the integer count, or a floating point ratio of tests passed out of the total number of tests.

    """

"""
# Class Responsibilities
* Which class is responsible for actually performing a test?
* does the training class invoke the classifier on each knwon sample in a testing set?
or perhaps, does it provide the testing set to the hyperparameter class, delegating the testing to the hyperaparameter class?
Since, the hyperparameter class has responsibility for the k value, and the algorithm for locating the k- nearest neighbors,
it seems sensible for the hyperparameter class to run the test using its own k value and a list of knwon sample instances provided to it.

It seems sensible for the hyperparameter class to run the test using its own k value and a list of known sample instances provided to it.

* It also seems clear, the training data class is an acceptable place to record the various hyperparameter trials.
This means that training data class can identifywhich of the hyperparameter instances has a value of k that classifies irises with the highest accuracy.

There are multiple related state changs here. in this case, both the hyperaparmeter and training data classes will do part of the work.
* The system as a whole - will change state as individual elements change state. This is sometimes described as emergent behavior. 
* Rather than writing a monster class, that does many things, we've written smaller classes that collaborate to achieve the expected goals. 

"""

"""
# The training data class
* The training data class has lists with two subclasses of sample objects.
* The known sample and unknown sample can be implemented as extension to a common parent class, sample.
* The training data class has a list with hyperparameter instances.
* This class can have simple, direct references to previously defined classes.

This class has the two methods that initiate the processing:
a. the load() method reads raw data and partitions into training data and test data.
- Both of these are essentially knwonSample instances with different purposes.
-  the training subset is for evaluating the k-NN algorithm;
- the testing subset is for determining how well the k hyperparameter is working

b. the test() method uses a hyperparameter object, performs the test, and saves the result.

From chapter 1 we see three user stories:

1. Provide Training Data
2. Set Parameters
3. Test Classifier, and Make Classification Request

It seems helpful, to add a method to perform a classification using a given hyperparameter instance.

This would add a classify() method to the TrainingData class. Again, this was not clearly required at the beginning of our design work, 
but seems like a good idea now.

- We have defined a number of attributes to track the history of the changes to this class.
- the uploaded time, and the tested time, for example, provide some history. The training, testing, and tuning attributes have sample 
objects and hyperparameter objects.

- We won't write methods to set all of these. This is a python and direct access to attributes is a huge simplification to complex applications.
- The responsibilities are encapsulated in this class. 

The load() method is designed to process data given by another object. We could have designed the load() method to open and read a file, 
but then we'd bind the training data to a specific file format and logical layout. It seems better to isolate the details of the 
file format from the details of managing training data.

* We'll depend on a source of data. We've described the properties of theis source with a type hint, iterable [dict[str, str]].
The iterable states that the methods resuts can be used by a for statement or the list function.
This is true of collections like lists and files. It's also true of generator functions.

The result of this iterator need to be dictionaries that map strings to strings. Thisis a very general structure, and it allows us to require a 
dictionary that looks like this.

{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4
    "petal_width": 0.2
    "Species": "Iris setosa
}

* This required structure seems flexible enough that we can build some object that will produce it.

* The remaining methods delegate most of their work to the Hyperparameter class. Rather than do the work of classification, this class relies 
on another class to do the work.


"""

class TrainingData:
    """ A set of training data and testing data with methods to load and test the samples """

    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded: datetime.datetime
        self.tested: datetime.datetime
        self.training: List[Sample] = []
        self.teting: List[Sample] = []
        self.tuning: List[Hyperparameter] = []

    def load(self, raw_data_source: Iterable[dict[str,str]]) -> None:
        """ Load and partition the raw data """
        for n, row in enumerate(raw_data_source):
            # filter and extract subsets (see chapter 6)
            # create self.training and self.testing subsets
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)

    def test(self, parameter: Hyperparameter) -> None:
        """ Test this Hyperparameter value. """
        parameter.test()
        self.runing.append(parameter)
        self.tested = datetime.datetime.now(tz=datetime.timezone.utc)

    def classify(
            self,
            parameter: Hyperparameter,
            sample: Sample) -> Sample:
        """ classify this sample """
        classification = parameter.classify(sample)
        sample.classify(classification)

        return sample
    
"""
In both cases, a specific Hyperparameter object is provided as parameter. For testing, this makes sense because each test should 
have a distinct value. For classification however, the best hyperparameter object should be used for classification.

In both cases, a specific Hyperparameter object is provided as parameter. For testing, this makes sense because each test should 
have a distinct value. For classification however, the best hyperparameter object should be used for classification.

* This part of the case study has built class definitions for sample, known sample, trainingdata, and hyperparameter.
* These classes capture parts of the overall application. 

It's good to start  with things that are clear, identify behavior and state change, and define the responsibilities.

"""



if __name__ == "__main__":
    s2 = Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa")
    print(s2)