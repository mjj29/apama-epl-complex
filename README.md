# EPL complex numbers
Apama EPL Classes for handling complex numbers and quaternions from EPL

## Supported Apama version

This works with Apama 10.5 or later, and probably most of the earlier ones as well

## Using the classes from EPL

To use complex numbers from EPL, add Complex.mon to your project, or ensure you inject it before your EPL code. Then import the event into your file with:

	using com.apamax.Complex;

To use quaternions from EPL, add both Complex.mon and Quaternion.mon to your project, or ensure you inject both before your EPL code. Then import the event into your file with:

	using com.apamax.Quaternion;

## Running tests

To run the tests you will need to use an Apama command prompt to run the tests from within the tests directory:

    pysys run

## API documentation

API documentation can be found here: [API documentation](https://mjj29.github.io/apama-epl-complex/)
