# interactive-fluid-twitter

An implementation of [interactive-fluid-demo](https://github.com/ngcm/interactive-fluid-demo) which runs on a server monitoring a given Twitter account. Whenever a tweet is written mentioning that Twitter account and attaching an image, the software will instantly grab the image, run the fluid flow simulation on top of that image and tweet an animated GIF back.

![example1](https://user-images.githubusercontent.com/4785303/35059288-8757857c-fbb2-11e7-9b96-b0d32f02744f.gif)
![example2](https://user-images.githubusercontent.com/4785303/35060001-eb033510-fbb4-11e7-8d14-384632987b6b.gif)

## Requirements:

 * A Twitter account
 * A Twitter app linked to that account

Create a file called `credentials.txt` and place it in the main directory. First to fourth lines should contain the consumer key, the consumer secret, the access token and the access token secret, respectively.

## Installation in Linux
Can be easily run on any Linux box, just follow the [instructions here](https://github.com/ngcm/interactive-fluid-demo#installation).

## Using a virtual machine
Moreover, we provide [Vagrant](https://www.vagrantup.com/) recipe to create a virtual machine with all the necessary software installed. This is very convenient as it can be quickly deployed somewhere to run non-stop.

Inside the `vagrant` directory do `vagrant up` to download and setup an Ubuntu 16.04 virtual machine and install all the requirements. Once this is done, log in with `vagrant ssh`. Then just: `cd interactive-fluid-twitter-master` and `python serve.py`.
