<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">jq-clone-tester</h3>

  <p align="center">
    A program for comparing the output of jq with the jq-clone
    <br />
    <br />
  </p>
</div>

<!-- GETTING STARTED -->
## Getting Started

Simply run main.py for some simple tests. More tests can (and should) be added under tests.py. In tests.py there is a brief explantation of how writing a test works. 
Adding new tests and test categories is hopefully pretty self explanatory. 
<br />
The generators (the thing that gives random ints, floats etc) are in the generators.py file. There is an example in the README under <a href="#usage">Usage</a>.
From this it should be clear how to make additional generators.

### Prerequisites
Only works on Windows 10 for now but setting this line (in runners.py)
```
    get_data_command = "type" if ".json" in data else "echo"
```
to 
```
    get_data_command = "cat" if ".json" in data else "echo"
```
might make it work on Linux and macOS. Not sure though.

Made with Python 12 but probably works for most, not too old, versions.

<a name="usage"></a>
<!-- USAGE EXAMPLES -->
## Usage
A very basic use case would be this:
<br />
<br />
This is how tests looks
<br />
![array tests examples](https://user-images.githubusercontent.com/95422056/222480399-cf39a339-a51d-4123-bcaf-fbe2bf31963f.png)
<br />  <br /> 
Which might lead to these results. The array index tests passed for 25 random integers and 25 random floats. The slice failed on the first test.
<br /> 
![array tests results](https://user-images.githubusercontent.com/95422056/222480432-2858c332-92b0-4bb8-bdfa-0a99b73bb229.png)
<br />
<br />
It is also possible to run a jq command on json files. New generators can easily be created in the generators.py file, or you can add a boolean condition
like the one QuickCheck. It is, however, just like in QuickCheck, recommended to make new generators instead of having conditions when the condition is not
very likely to happen (otherwise it takes a long time to test). 
<br />
<br />
Here are some example generators:
<br />
![image](https://user-images.githubusercontent.com/95422056/222484477-578a315e-985b-4603-b98a-a303363f37ab.png)
<br />
Here is an example of using a condition and reading input from a file:
<br />
![image](https://user-images.githubusercontent.com/95422056/222485244-a08f2619-3df5-4d44-b1bf-b789e2dd9155.png)
<br />

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Add a roadmap

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Emil Malmsten - e.l.malmsten@student.tudelft.nl

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

